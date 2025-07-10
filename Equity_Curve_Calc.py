import numpy as np
import pandas as pd
from Interbank_data import daily_index
from UST3MO import give_USTY3MO
Treasury_Rates = give_USTY3MO()
from Total_PnL import PnL_dataset 
equity_curve = pd.DataFrame()
initial_capital = 1 # Making it 1 to make percentage changes more readable
equity_curve.index = daily_index
equity_curve['PnL (%)'] = PnL_dataset['Daily_PnL_History'].fillna(0)
equity_curve['Growth Factor'] = 1 + PnL_dataset['Daily_PnL_History'].fillna(0)/100
equity_curve['Equity'] = initial_capital * equity_curve['Growth Factor'].cumprod()
#print(equity_curve['Equity'].iloc[-1])
total_cumulative_raturn_in_percentage = (equity_curve['Equity'].iloc[-1] - initial_capital) * 100
end = (equity_curve.loc[pd.Timestamp(2025,1,1), 'Equity'])
begin = (equity_curve.loc[pd.Timestamp(2002,1,2), 'Equity'])
begin_date = pd.Timestamp(2002,1,2)
end_date = pd.Timestamp(2025,1,1) 
print(begin)
print(end)
def diff_to_years(dates:tuple)->float:
    begin = dates[0]
    end = dates[1]
    diff = end - begin
    years = diff.days/365.25
    years = round(years, 2)
    return years
Number = diff_to_years((begin_date, end_date))
print(Number)

