import Interbank_data 
import FX_data
import pandas as pd 
import numpy as np 
from fredapi import Fred 
from datetime import datetime 
api_key = "23dd8644a8456a82f3dc0e07c51e2a9b"
fred = Fred(api_key = api_key)
start = Interbank_data.start
end = Interbank_data.end
currency_codes = {
    "Europe":"EUR",
    "New Zealand":"NZD",
    "Norway":"NOK",
    "Japan": "JPY",
    "Australia": "AUD",
    "Switzerland": "CHF",
    "Canada": "CAD",
    "Sweden": "SEK",
    "United States": "USD",
    "United Kingdom": "GBP"
}
big_storage = Interbank_data.big_storage

def is_rebalancing(date):
    prices = FX_data.ClosePrice_DataSet_ForAll
    if date not in prices.index or pd.isna(prices.loc[date, 'USDNOK=X']):
        return False
    first_day_of_month = date.replace(day=1)
    candidate_days = pd.bdate_range(start=first_day_of_month, periods=10)
    
    true_rebal_day = None
    
    for day_to_check in candidate_days:
        if day_to_check in prices.index and not pd.isna(prices.loc[day_to_check, 'USDNOK=X']):
            true_rebal_day = day_to_check
            break
            
    return date == true_rebal_day
Large_Set = Interbank_data.give_largeSet()
Large_Set["Rebalancing Day"] = Large_Set.index.to_series().apply(is_rebalancing)

def construct_portfolio(Date):
    if not Large_Set.loc[Date, 'Rebalancing Day']:
        #if the day is not a rebalancing day
        past_rebalances = Large_Set['Rebalancing Day'].loc[:Date]
        if not past_rebalances.any():
            raise ValueError(f"No rebalancing day found before {Date}")
        last_rebal_day = past_rebalances[past_rebalances].index.max()
        effective_date = last_rebal_day + pd.Timedelta(days = 1)
    else:
        effective_date = Date   
            
    dat = big_storage.loc[effective_date, 'Ascending_Data_for_Portfolio']
    USD_rate = Interbank_data.united_states.loc[effective_date,"United States Interbank Rate"]
    portfolio = dict()
    portfolio['long'] = [currency_codes[dat[-1][0]],
                         currency_codes[dat[-2][0]],
                         currency_codes[dat[-3][0]] ]
    portfolio ['short'] = [currency_codes[dat[0][0]],
                           currency_codes[dat[1][0]],
                           currency_codes[dat[2][0]]]
    portfolio['long_rates'] = [dat[-1][1], dat[-2][1], dat[-3][1]]
    portfolio['short_rates'] = [dat[0][1], dat[1][1], dat[2][1]]
    if 'USD' in portfolio['long']:
        portfolio['long'].remove('USD')
        portfolio['long_rates'].remove(USD_rate)
    if 'USD' in portfolio['short']:
        portfolio['short'].remove('USD')
        portfolio['short_rates'].remove(USD_rate)        
    return portfolio
def show_portfolio(port):
    new_port = port
    new_port["long_rates"] = [float(format(x, ".2f")) for x in new_port["long_rates"]]
    new_port["short_rates"] = [float(format(x, ".2f")) for x in new_port["short_rates"]]
    for key in new_port:
        print(f"{key} : {new_port[key]}")
    return    

big_storage['Portfolio'] = big_storage.index.to_series().apply(construct_portfolio)
Large_Set["port"] = big_storage['Portfolio']
if __name__ == '__main__':
    #print(big_storage['Portfolio'])
    print(Large_Set['Rebalancing Day'])


