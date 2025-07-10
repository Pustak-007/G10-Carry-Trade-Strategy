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
#period_list = ["Pre-GFC", "GFC", "Post-GFC-(Before Covid)-ZIRP", "Covid-2020", "Post-Covid"]
def diff_to_years(dates:tuple)->float:
    begin = dates[0]
    end = dates[1]
    diff = end - begin
    years = diff.days/365.25
    years = round(years, 2)
    return years
period_to_date_range = {"All" : (pd.Timestamp(2002,1,2), pd.Timestamp(2025,1,1), diff_to_years((pd.Timestamp(2002,1,2), pd.Timestamp(2025,1,1)))),
                                  "Pre-GFC" : (pd.Timestamp(2002,1,2), pd.Timestamp(2007,12,1), diff_to_years((pd.Timestamp(2002,1,2), pd.Timestamp(2007,12,1)))),
                 "GFC" : (pd.Timestamp(2007,12,1), pd.Timestamp(2009,6,1), diff_to_years((pd.Timestamp(2007,12,1), pd.Timestamp(2009,6,1)))),
                "Post-GFC-(Before Covid)-ZIRP": (pd.Timestamp(2009,7,1),pd.Timestamp(2019,12,10), diff_to_years((pd.Timestamp(2009,7,1),pd.Timestamp(2019,12,10)))),
                "Covid-Crash": (pd.Timestamp(2020,2,1), pd.Timestamp(2020,4,20), None),
                "Post-Covid":(pd.Timestamp(2020,4,20), pd.Timestamp(2025,1,1), diff_to_years((pd.Timestamp(2020,4,20), pd.Timestamp(2025,1,1))))}
def calculate_annualized_return_pct(period):
    if period not in period_to_date_range:
        return f'{KeyError}: Invalid Period'
    if period == 'Covid-Crash':
        raise ValueError ("The covid-crash happened so fast that calculating annualized return/volatility of that period is meaningless" \
        "use the functions dedicated for this to understand the magnitude of that event.")
    beginning_capital = equity_curve.loc[period_to_date_range[period][0], 'Equity'] 
    ending_capital = equity_curve.loc[period_to_date_range[period][1], 'Equity']
    Number_of_years = period_to_date_range[period][2]  
    annualized_return_pct = (((ending_capital/beginning_capital) ** (1/Number_of_years)) - 1) * 100
    return annualized_return_pct
def calculate_annualized_volatility(period):
    if period not in period_to_date_range:
        return f'{KeyError}: Invalid Period'
    if period == 'Covid-Crash':
        raise ValueError ("The covid-crash happened so fast that calculating annualized return/volatility of that period is meaningless" \
        "use the functions dedicated for this to understand the magnitude of that event.")
    begin = period_to_date_range[period][0]
    end = period_to_date_range[period][1]
    daily_volatility = PnL_dataset.loc[begin:end, 'Daily_PnL_History'].std()
    annualized_volatility = daily_volatility * np.sqrt(252) 
    return annualized_volatility  
# I implemented a more efficient way to get through this repetitve if/else system, perhaps should implement this system
# for the functions above as well.   
# Well, I did implement it 
def calculate_sharpe_ratio(period):
    if period not in period_to_date_range:
        return f'{KeyError}: Invalid Period'
    if period == 'Covid-Crash':
        raise ValueError ("The covid-crash happened so fast that calculating annualized return/volatility of that period is meaningless" \
        "use the functions dedicated for this to understand the magnitude of that event.")
    begin = period_to_date_range[period][0]
    end = period_to_date_range[period][1]
    period_for_risk_free = Treasury_Rates.loc[begin:end, 'Rates']
    risk_free_rate = period_for_risk_free.mean()
    annualized_volatility = calculate_annualized_volatility(period)
    annualized_return = calculate_annualized_return_pct(period)
    sharpe_ratio = (annualized_return - risk_free_rate)/annualized_volatility
    return sharpe_ratio
def calculate_max_drawdown(period):
    #if period == 'Covid-Crash':
    #    raise ValueError ("The covid-crash happened so fast that calculating annualized return/volatility of that period is meaningless" \
    #    "use the functions dedicated for this to understand the magnitude of that event.")
    if period not in period_to_date_range:
        raise KeyError ('Invalid Period')
    begin = period_to_date_range[period][0]
    end = period_to_date_range[period][1]
    df = equity_curve.loc[begin:end, 'Equity'].fillna(0).to_frame(name = "Equity")
    df['Cumulative Max'] = df['Equity'].cummax()
    df['Drawdown'] = ((df['Equity'] - df['Cumulative Max'])/df['Cumulative Max'] * 100).round(2)
    return df['Drawdown'].min()
def give_dataframe_with_drawdown(period):
    if period not in period_to_date_range:
        raise KeyError ('Invalid Period')
    begin = period_to_date_range[period][0]
    end = period_to_date_range[period][1]
    df = equity_curve.loc[begin:end,'Equity'].fillna(0).to_frame(name = "Equity")
    df['Cumulative Max'] = df['Equity'].cummax()
    df['Drawdown (%)'] = ((df['Equity'] - df['Cumulative Max'])/df['Cumulative Max'] * 100).round(2) 
    return df
# Now we get into functions that are explicitly for covid period
# -- the reason of this separation is because the crash was so sharp that trying to calculate 
# an annualized return/volatility of something that only lasted for around 1.5 to 2 months simply doesn't make
# -- sense. So, we will be creating funtions that are basically calculating the total cumulative return
# and the daily volatility figure over the period but give it an explicit name as covid functions;
# nothing but a pragmatic wrap around it - Hope this makes sense to you!

def covid_return():
    begin = period_to_date_range['Covid-Crash'][0]
    end = period_to_date_range['Covid-Crash'][1]
    total_cumulative_return = ((equity_curve.loc[end, 'Equity'] - equity_curve.loc[begin, 'Equity'])/equity_curve.loc[begin, 'Equity']) * 100
    return total_cumulative_return
def covid_volatility():
    begin = period_to_date_range['Covid-Crash'][0]
    end = period_to_date_range['Covid-Crash'][1]
    total_volatility = PnL_dataset.loc[begin:end, 'Daily_PnL_History'].std()
    return total_volatility
def covid_maxDrawdown():
    begin = period_to_date_range['Covid-Crash'][0]
    end = period_to_date_range['Covid-Crash'][1]
    max_drawdown = calculate_max_drawdown('Covid-Crash')
    return max_drawdown




if __name__ == "__main__":
    begin = pd.Timestamp(2002,1,1)
    end = pd.Timestamp(2007,12,1)
    print(calculate_annualized_return_pct(period = 'Pre-GFC'))
    print(calculate_annualized_volatility(period = 'Pre-GFC'))
    print(Treasury_Rates.loc[begin:end, 'Rates'].mean())
    print(calculate_sharpe_ratio(period = 'Pre-GFC'))
    print('-' * 100)
    print(calculate_sharpe_ratio(period = 'GFC'))
    print(calculate_annualized_volatility(period = 'GFC'))
    print(calculate_annualized_volatility(period = 'Post-GFC-(Before Covid)-ZIRP'))
    print(calculate_annualized_return_pct(period = 'Post-GFC-(Before Covid)-ZIRP'))



