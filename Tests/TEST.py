import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#Code for access to the modules of the larger G10 Folder.

#rebalancing day data is in Large_Set
import pandas as pd
import numpy as np
import Interbank_data
from construction import Large_Set, big_storage
from FX_data import ClosePrice_PercentageChange_DataSet
from FX_data import ClosePriceWithPercentageChange_DataSet_ForAll
import Carry_PnL
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
from Total_PnL import PnL_dataset
temp_start = Interbank_data.start
temp_end = temp_start + pd.Timedelta(days = 20)
my_dict = Carry_PnL.currency_to_country_interbank
temp_check = pd.DataFrame()
def Carry_PnL_Module_Manual_Test():
    mask = Large_Set['Rebalancing Day']
    #So, this mask basically becomes a boolean series which can be used to 
    # -- filter rows
    df = big_storage.loc[mask, 'Portfolio']
    # we want portfolio only at the rebalancing day because with this we have 
    # sufficent unique interbank data to manually check things
    print(df)
    print(PnL_dataset.loc[mask, ['Carry_long_Basket_Return','Carry_short_Basket_Return', 'Carry_daily_return']])
    return
Carry_PnL_Module_Manual_Test()

# This entire code snippet is for checking the validity of the computation of
# the forex module - in my testing it has worked So if you want to have check this one,
# -- without any clutter, just convert the carry check part of the code into a bunch of comments
# -- on second thought, I probably could have created separate functions as well.
def Forex_PnL_Module_Manual_Test():
    currency_to_pctChange = {
        'AUD': 'AUDUSD_pct_change',
        'CAD': 'USDCAD_pct_change',
        'CHF': 'USDCHF_pct_change',
        'EUR': 'EURUSD_pct_change',
        'GBP': 'GBPUSD_pct_change',
        'JPY': 'USDJPY_pct_change',
        'NOK': 'USDNOK_pct_change',
        'NZD': 'NZDUSD_pct_change',
        'SEK': 'USDSEK_pct_change'
    }
    temp_range = pd.date_range(temp_start, temp_end)
    mask = Large_Set['Rebalancing Day']
    port = big_storage.loc[temp_range, 'Portfolio']

    #Don't provide a date that extends one rebalancing period in here - the function is not for that and it serves
    # its testing purpose even without it, so I didn't generalize it for that.
    def give_me_changes(portfolio):
        df = pd.DataFrame()
        df.index = temp_range
        for currency in portfolio['long']:
            df[currency_to_pctChange[currency]] = ClosePriceWithPercentageChange_DataSet_ForAll[currency_to_pctChange[currency]]
        for currency in portfolio['short']:
            df[currency_to_pctChange[currency]] = ClosePriceWithPercentageChange_DataSet_ForAll[currency_to_pctChange[currency]]
        return df 

    df = give_me_changes(big_storage.loc[temp_start, 'Portfolio'])
    #Here you are just supposed to have one portfolio and because that portfolio only for a month I said 
    #- no portfolio across the rebalancing day, but to check for the forex data computation consistency,
    # - this constraint doesn't raise any impediments.
    print(port)
    print(df)
    print(PnL_dataset.loc[temp_range,['FX_long_Basket_Return','FX_short_Basket_Return','FX_daily_return']])

    #Okay, so the Forex PnL module is doing its task preety well.

