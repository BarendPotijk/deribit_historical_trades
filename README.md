<a name="readme-top"></a>
<br />
<div align="center">
  <a href="https://github.com/BarendPotijk/Deribit_historical_option_trades/">
    <img src="deribit.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Gather historical Crypto Option trades</h3>

  <p align="center">
    Gather Cryptocurrency option trades using Deribit API v2
    <br />
    <a href="https://github.com/BarendPotijk/Deribit_historical_option_trades/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/BarendPotijk/Deribit_historical_option_trades/tree/main/Jupyter%20Notebook.ipynb">See code </a>
  </p>
</div>

## Project description ##
The Deribit_historical_option_trades repository gathers cryptocurrency (BTC, ETH, SOL, USDC) options traded on the cryptocurrency derivative platform Deribit (https://www.deribit.com). 
All crypto option trades since the start of the platform are publicly available in the Deribit API v2.1.1 under 'https://history.deribit.com/api/v2/public/get_last_trades_by_currency' using REST requests. 
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
  3. Set the query parameters for the API endpoint in the params dictionary.
  4. Run the script.

The script will make requests to the API endpoint and page through the results until all data has been retrieved. The option trade data will be processed into a Pandas DataFrame with the following columns:
Markup :
  * *date_time*: the timestamp of the trade /newline
  * *instrument_name*: the name of the option instrument
  * *option_price*: the price of the option in USD
  * *direction*: the direction of the option trade (buy or sell)
  * *option_type*: the type of the option (call or put)
  * *amount*: the size of the option trade
  * *maturity_date*: the maturity date of the option
  * *strike_price*: the strike price of the option
  * *index_price*: the price of the underlying asset (BTC, ETH, SOL, USDC)
  * *iv*: the implied volatility of the option calculated by Deribit 
  * *moneyness*: the moneyness of the option
  * *time_to_maturity (days)*: the time-to-maturity of the option in days

## Contributing ##
If you find a bug or would like to suggest an enhancement, please create an issue or submit a pull request.
