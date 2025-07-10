import Interbank_data 
import construction
import pandas as pd 
import numpy as np 
from fredapi import Fred 
from datetime import datetime 
# pd.set_option('display.max_columns',None)
api_key = "23dd8644a8456a82f3dc0e07c51e2a9b"
fred = Fred(api_key = api_key)
start = Interbank_data.start
end = Interbank_data.end
daily_index = Interbank_data.daily_index
currency_to_country_interbank = {
    'AUD': 'Australia Interbank Rate',
    'CAD': 'Canada Interbank Rate',
    'CHF': 'Switzerland Interbank Rate',
    'EUR': 'Europe Interbank Rate',
    'GBP': 'United Kingdom Interbank Rate',
    'JPY': 'Japan Interbank Rate',
    'NOK': 'Norway Interbank Rate',
    'NZD': 'New Zealand Interbank Rate',
    'SEK': 'Sweden Interbank Rate',
    'USD': 'United States Interbank Rate'
}
Large_Interbank_Set = Interbank_data.Large_Interbank_Set
def give_average_long_IB_rate(Date):
    current_portfolio = Interbank_data.big_storage.loc[Date, 'Portfolio']
    Long_list = current_portfolio['long']
    Long_rates_list = current_portfolio['long_rates']
    big_list = zip(Long_list, Long_rates_list)
    assert Long_list, 'List must not be empty'
    sum_long_rate = float()
    for currency,long_rates in big_list:
        if currency not in currency_to_country_interbank.keys():
            return KeyError
        sum_long_rate += long_rates
        #sum_long_rate += Large_Interbank_Set.loc[Date, currency_to_country_interbank[currency]]
    return sum_long_rate/len(Long_list) 
def give_average_short_IB_rate(Date):
    current_portfolio = Interbank_data.big_storage.loc[Date, 'Portfolio']
    Short_list = current_portfolio['short']
    Short_rates_list = current_portfolio['short_rates']
    big_list = zip(Short_list, Short_rates_list)
    assert Short_list, 'List must not be empty'
    sum_short_rate = float()
    for currency, short_rates in big_list:
        if currency not in currency_to_country_interbank.keys():
            return KeyError
        sum_short_rate += short_rates
        #sum_short_rate += Large_Interbank_Set.loc[Date, currency_to_country_interbank[currency]] 
    return sum_short_rate/len(Short_list)
def give_daily_IB_rate_differential(Date):
    current_portfolio = Interbank_data.big_storage.loc[Date, 'Portfolio']
    long_rate = give_average_long_IB_rate(Date)
    short_rate = give_average_short_IB_rate(Date)
    return (long_rate - short_rate)/365
