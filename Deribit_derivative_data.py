import json
import requests
import pandas as pd
from datetime import datetime as dt
from datetime import date, timedelta

def datetime_to_timestamp(datetime_obj): 
    """Converts a datetime object to a Unix timestamp in milliseconds."""
    return int(dt.timestamp(datetime_obj)*1000)

def timestamp_to_datetime(timestamp): 
    """Converts a Unix timestamp in milliseconds to a datetime object."""
    return dt.fromtimestamp(timestamp/1000)

def derivative_data(currency: str, kind: str, start_date: date, end_date: date, count: int = 10000) -> pd.DataFrame:
    """Returns derivative trade data for a specified currency and time range.

    Args:
        currency (str): The currency symbol, e.g. 'BTC'.
        kind (str): The type of derivative, either 'option' or 'future'.
        start_date (date): The start date of the time range (inclusive).
        end_date (date): The end date of the time range (inclusive).
        count (int, optional): The maximum number of trades to retrieve per request. Defaults to 10000.

    Returns:
        pandas.DataFrame: A dataframe of derivative trade data for the specified currency and time range.
    """

    # Validate input arguments
    assert isinstance(currency, str), "currency must be a string"
    assert isinstance(start_date, date), "start_date must be a date object"
    assert isinstance(end_date, date), "end_date must be a date object"
    assert start_date <= end_date, "start_date must be before or equal to end_date"

    derivative_list = []
    params = {
        "currency": currency, 
        "kind": kind,
        "count": count,
        "include_old": True,
        "start_timestamp": datetime_to_timestamp(dt.combine(start_date, dt.min.time())),
        "end_timestamp": datetime_to_timestamp(dt.combine(end_date, dt.max.time()))
    }

    url = 'https://history.deribit.com/api/v2/public/get_last_trades_by_currency_and_time'

    # Use a session object to make requests to the API endpoint in a loop, paging through results until all data has been retrieved
    with requests.Session() as session:
        while True:
            response = session.get(url, params=params)
            response_data = response.json()
            if len(response_data["result"]["trades"]) == 0:
                break
            derivative_list.extend(response_data["result"]["trades"])
            params["start_timestamp"] = response_data["result"]["trades"][-1]["timestamp"] + 1
            if params["start_timestamp"] >= datetime_to_timestamp(dt.combine(end_date, dt.max.time())):
                break
                
    # Create a pandas dataframe from the derivative trade data
    derivative_data = pd.DataFrame(derivative_list)
    if len(derivative_data) == 0:
        return derivative_data
    derivative_data["date_time"] = pd.to_datetime(derivative_data["timestamp"], unit='ms')
    return derivative_data
