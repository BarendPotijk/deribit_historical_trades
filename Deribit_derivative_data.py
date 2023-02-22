#!/usr/bin/env python
# coding: utf-8

# In[40]:


import json
import requests
import pandas as pd
from datetime import datetime as dt
from datetime import date, timedelta

# Define helper functions for converting between datetimes and timestamps
def datetime_to_timestamp(datetime_obj): 
    return int(dt.timestamp(datetime_obj)*1000)

def timestamp_to_datetime(timestamp): 
    return dt.fromtimestamp(timestamp/1000)

def derivative_data(currency, kind, start_date, end_date):
    derivative_list = []
    params = {
        "currency": currency, 
        "kind": kind,
        "count": 10000,
        "include_old": True,
        "start_timestamp": datetime_to_timestamp(start_date),
        "end_timestamp": datetime_to_timestamp(end_date)
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
            if params["start_timestamp"] >= datetime_to_timestamp(end_date):
                break
                
    print(derivative_list)
    # Create a pandas dataframe from the derivative trade data
    derivative_data = pd.DataFrame(derivative_list)
    if len(derivative_data) == 0:
        return derivative_data
    derivative_data["timestamp"] = derivative_data["timestamp"].apply(lambda x: timestamp_to_datetime(x))
    derivative_data.rename({"timestamp":"date_time"}, axis=1, inplace = True)
    return derivative_data

