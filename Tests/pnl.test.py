import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#Code for access to the modules of the larger G10 Folder.
import Interbank_data 
import construction
import fx_test
import pandas as pd 
import numpy as np 
from fredapi import Fred 
from datetime import datetime 
# pd.set_option('display.max_columns',None)
api_key = "23dd8644a8456a82f3dc0e07c51e2a9b"
pd.set_option('display.max_columns', None)
fred = Fred(api_key = api_key)
start = Interbank_data.start
end = Interbank_data.end
daily_index = Interbank_data.daily_index
portfolio = construction.construct_portfolio()
currency_equivalent = { 'EUR': fx_test.EURUSD, 'JPY': fx_test.USDJPY, 
                       'GBP': fx_test.GBPUSD, 'CAD': fx_test.USDCAD, 
                       'AUD': fx_test.AUDUSD, 'NZD': fx_test.NZDUSD, 
                       'CHF': fx_test.USDCHF, 'SEK': fx_test.USDSEK, 
                       'NOK': fx_test.USDNOK}

#sets are used- it will optimize the spot return function to some extent
usd_base_pairs = {'JPY', 'CAD', 'CHF', 'NOK', 'SEK'}
usd_quote_pairs = {'EUR', 'AUD', 'NZD', 'GBP'}

currency_to_pair = {
    'EUR': 'EURUSD',
    'JPY': 'USDJPY',
    'GBP': 'GBPUSD',
    'CHF': 'USDCHF',
    'AUD': 'AUDUSD',
    'CAD': 'USDCAD',
    'NZD': 'NZDUSD',
    'NOK': 'USDNOK',
    'SEK': 'USDSEK'
}
Large_FX_spot = fx_test.Spot_FX_dataset
def average_long_spot_return_function(long_list = portfolio['long']):
    daily_change = 0
    temp = list()
    for i in range(len(long_list)):
        pair = currency_to_pair[long_list[i]]
        temp.append(pair)
        daily_change = daily_change + fx_test.Spot_FX_dataset.loc[Interbank_data.date_for_ascen, f'{pair}_pct_change']
    return [daily_change, temp]
lado = 'EURUSD'
print(fx_test.Spot_FX_dataset.loc[Interbank_data.date_for_ascen, f'{lado}_pct_change'])
lado_list = ['AUDUSD', 'NZDUSD', 'GBPUSD']
daily_shit = 0
for i in range(3):
    daily_shit += fx_test.Spot_FX_dataset.loc[Interbank_data.date_for_ascen, f'{lado_list[i]}_pct_change']
print(daily_shit)
#Okay, so through this step, I have been to figure out, or at least isolate
#the cause of the problem
print(average_long_spot_return_function())    
        






    