import matplotlib.pyplot as plt 
import os
import matplotlib.dates as mdates
from Interbank_data import daily_index
from matplotlib.ticker import ScalarFormatter
import pandas as pd
import numpy as np
from Total_PnL import PnL_dataset
initial_capital = 1 # to normalize the data, so the percentage growth is easily
# -- interpretable
def Create_Equity_Graph():
    df = pd.DataFrame()
    x = df.index =  daily_index 
    df['PnL (%)'] = PnL_dataset['Daily_PnL_History'].fillna(0)
    df['Growth Factor'] = 1 + PnL_dataset['Daily_PnL_History'].fillna(0)/100
    y = df['Equity'] = initial_capital * df['Growth Factor'].cumprod()
    fig, ax = plt.subplots()
    ax.plot(x,y)
    ax.xaxis.set_major_locator(mdates.YearLocator(1))
    ax.xaxis.set_minor_locator(mdates.MonthLocator(interval = 3))
    plt.title('G10 Carry Strategy Equity Curve (2002 - 2025)')
    plt.xlabel("(Date)", fontsize = 12, color = "Blue")
    plt.ylabel("(Equity $)", fontsize = 12, color = "green")
    ax.set_yscale('log')
    formatter = ScalarFormatter()
    formatter.set_scientific(False)
    ax.yaxis.set_major_formatter(formatter=formatter)
    plt.axhline(y = initial_capital, color = 'grey', linestyle = '--')
    #covid-range
    plt.axvline(x = pd.Timestamp(2020,2,1), color = 'grey', linestyle = ':')
    plt.axvline(x = pd.Timestamp(2020,4,20), color = 'grey', linestyle = ':')
    plt.axvline(x = pd.Timestamp(2007,12,1), color = 'grey', linestyle = ':')
    plt.annotate(
        text = 'Break-even Point',
        xy = (pd.Timestamp(2023,1,1), initial_capital),
        xytext = (pd.Timestamp(2023,1,1), 1.2*initial_capital),
        arrowprops= dict(arrowstyle = '-|>', color = 'gray'),
        ha = 'center', fontsize = 8
    )
def GFC_text_and_symbol():
    temp_date = pd.Timestamp(2008,9,10)
    temp_value = 1.70 * initial_capital
    plt.annotate(
        text = '2008 GFC Carry Trade Unwinding',
        xy = (temp_date+pd.Timedelta(days = 90), temp_value),
        xytext = (temp_date + pd.Timedelta(days = 365 * 1), 1.82 * initial_capital),
        arrowprops=dict(arrowstyle = '-|>', color = 'black'),
        ha = 'center', fontsize = 8
    )
def Covid_text_and_symbol():
    temp_date = pd.Timestamp(2020,1,10)
    temp_value = 1.70 * initial_capital
    plt.annotate(
        text = '2020 Covid Carry Trade Unwinding (Secondary)',
        xy = (temp_date+pd.Timedelta(days = 90), temp_value),
        xytext = (temp_date + pd.Timedelta(days = 365 * 1), 1.82 * initial_capital),
        arrowprops=dict(arrowstyle = '-|>', color = 'black'),
        ha = 'center', fontsize = 8
    )
Create_Equity_Graph()
GFC_text_and_symbol()
Covid_text_and_symbol()
plt.show()