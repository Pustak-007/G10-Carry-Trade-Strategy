import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#We include this piece of code at the top of every module in the Tests Folder because without it,
#--we can't access the data of the larger folder.
import FX_data
import pandas as pd 
import numpy as np

prices = FX_data.function_map['USDNOK']['Close']

def is_rebalancing(date):
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

prices['CheckRebal'] = prices.index.to_series().apply(is_rebalancing)

print(prices)