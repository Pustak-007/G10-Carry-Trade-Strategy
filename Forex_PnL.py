import Interbank_data 
import construction
import FX_data
import pandas as pd 
import numpy as np 
from fredapi import Fred 
from datetime import datetime 
#pd.set_option('display.max_columns',None)
Big_Forex_Data = FX_data.ClosePriceWithPercentageChange_DataSet_ForAll
api_key = "23dd8644a8456a82f3dc0e07c51e2a9b"
fred = Fred(api_key = api_key)
start = Interbank_data.start
end = Interbank_data.end
daily_index = Interbank_data.daily_index
#current_portfolio = construction.construct_portfolio()
currency_to_pair = {
    'EUR': 'EURUSD',
    'AUD': 'AUDUSD',
    'NZD': 'NZDUSD',
    'GBP': 'GBPUSD',
    'CAD': 'USDCAD',
    'CHF': 'USDCHF',
    'JPY': 'USDJPY',
    'NOK': 'USDNOK',
    'SEK': 'USDSEK'
}
Counter_USD = {'EUR', 'AUD', 'GBP', 'NZD'} #list of currencies where USD is Counter
Base_USD = {'CHF', 'JPY', 'NOK', 'SEK', 'CAD'} #list of currenceis where USD is base

def give_Average_Long_Return(Date): #we need to enter the c_p['long'] in here
    current_portfolio = construction.construct_portfolio(Date)
    Long_data = current_portfolio['long']
    if not Long_data:
        return 0.0
    sum_percentage_return = float()
    for currency in Long_data:
        if currency in Counter_USD:
            sum_percentage_return = sum_percentage_return + (+1) * Big_Forex_Data.loc[Date, f'{currency_to_pair[currency]}_pct_change']
            #Emphasis on (+1) is deliberate
        elif currency in Base_USD:
            sum_percentage_return = sum_percentage_return + (-1) * Big_Forex_Data.loc[Date,f'{currency_to_pair[currency]}_pct_change']  
            # Imagine longing NOK, the major pair associated with NOK is USDNOK
            # -Longing NOK means shorting USDNOK, so we want USDNOK pct change to be negative
            # -- in order to realize a positive gain in longing USDNOK - hope this makes sense!
        else:
            print(f'The currency {currency} is not found in Counter_USD and Base_USD')    
    average_percentage_return = sum_percentage_return/len(Long_data)
    return average_percentage_return
def give_Average_Short_Return(Date): #we need to enter the c_p['short'] in here
    current_portfolio = construction.construct_portfolio(Date)
    Short_data = current_portfolio['short']
    if not Short_data:
        return 0.0
    sum_percentage_return = float()
    for currency in Short_data:
        if currency in Base_USD:
            sum_percentage_return = sum_percentage_return + (+1) * Big_Forex_Data.loc[Date, f'{currency_to_pair[currency]}_pct_change'] 
            #Again, take example of NOK, the major currency pair associated with NOK is USDNOK
            # -- shorting NOK means you expect USDNOK to go up. A positive value in the pct_change column
            # -- indicates that USDNOK went up - and so (+1) in this case.
        elif currency in Counter_USD:
            sum_percentage_return = sum_percentage_return + (-1) * Big_Forex_Data.loc[Date, f'{currency_to_pair[currency]}_pct_change'] 
            # Take example of EUR, the major currency pair associated with EUR is EURUSD 
            # --shorting EUR means you expect the EURUSD to go down. A negative value in pct_change column
            # --indicates EURUSD went down, but it going down is positive for us, because we betted on it going down.
            # -- So the return is positive for us.
        else:
            print(f'The currency {currency} is not found in Counter_USD or Base_USD')    
    average_percentage_return = sum_percentage_return/len(Short_data)
    return average_percentage_return
def give_total_daily_fx_return(Date): 
  current_portfolio = construction.construct_portfolio(Date)
  Total_Daily_Spot_Return = ( give_Average_Long_Return(Date) +
                             give_Average_Short_Return(Date) )
  return Total_Daily_Spot_Return

if __name__ == "__main__":
    def calculate_portfolio_pnl(current_portfolio):
        #Argument = Result of construction_portfolio function in construction module
        long_positions = current_portfolio.get('long', [])
        short_positions = current_portfolio.get('short', [])
        
        avg_long_return = give_Average_Long_Return(long_positions)
        avg_short_return = give_Average_Short_Return(short_positions)
        
        total_return = give_total_daily_fx_return(avg_long_return, avg_short_return)
        return {
            'long_return': avg_long_return,
            'short_return': avg_short_return,
            'total_return': total_return
        }   







