<a name="readme-top"></a>
<br />
<div align="center">
  <a href="https://github.com/BarendPotijk/Deribit_historical_option_trades/">
    <img src="deribit.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Historical Crypto trades</h3>

  <p align="center">
    Gather Cryptocurrency derivative trades using Deribit API v2
    <br />
    <a href="https://github.com/BarendPotijk/Deribit_historical_option_trades/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/BarendPotijk/Deribit_historical_option_trades/tree/main/Deribit_derivative_data.py">See code </a>
  </p>
</div>

## Project description ##
The Deribit_historical_trades repository gathers cryptocurrency (BTC, ETH, SOL, USDC) derivatives traded on the cryptocurrency derivative platform Deribit. 
All crypto derivatives trades since the start of the platform are publicly available in the Deribit API v2.1.1 under 'https://history.deribit.com/api/v2/public/get_last_trades_by_currency' using REST requests. 
For further information and the documentations see https://docs.deribit.com/#public-get_last_trades_by_currency_and_time. 

## Getting Started ##
To use this script, you will need to have Python 3 and the following libraries installed:

  * json
  * requests
  * pandas
  * datetime

## Running the Script ##

  1. Open the script in your preferred Python editor.
  2. Ensure that the required libraries are installed.
  3. Set the query parameters for the API endpoint in the function derivative_data(`currency`, `start_date`, `end_date`, `kind`, `count`).
  4. Run the script.

## Parameters ##

| Parameter | Required | Type | Enum | Description |
| --- | --- | --- | --- | --- |
| currency | true | string | `BTC`<br /> `ETH` <br /> `SOL` <br /> `USDC`| The currency symbol|
| start_date | true | datetime object | | The earliest datetime object to return result for. When param is provided trades are returned from the earliest |
| end_date | true | datetime object | | The most recent datetime object to return result for. Only one of params: start_date, end_date is truly required |
| kind | false | string  | `future`<br /> `option` <br /> `future_combo` <br /> `option_combo` <br /> `combo` <br /> `any` | Instrument kind, `combo` for any combo or `any` for all. If not provided instruments of all kinds are considered |
| count | false | integer | | Number of requested items, default - `10000` |

## Contributing ##
If you find a bug or would like to suggest an enhancement, please create an issue or submit a pull request. We welcome any contributions or feedback to make this script more useful and user-friendly for the cryptocurrency community.
