import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#Code for access to the modules of the larger G10 Folder.
import pandas as pd
import numpy as np
import pandas as pd
import yfinance as yf
pd.set_option('display.min_rows', 100)

def Historical_PriceData(file_path):
    daily_index = pd.date_range(start = pd.Timestamp(2000,1,1), end = pd.Timestamp(2025,1,1), freq = 'D')
    df = pd.read_csv(file_path, delimiter='\t')
    df = df.rename(columns={
        '<DATE>': 'Date',
        '<OPEN>': 'Open',
        '<HIGH>': 'High',
        '<LOW>': 'Low',
        '<CLOSE>': 'Close',
        '<TICKVOL>': 'TickVolume',
        '<VOL>': 'Volume',
        '<SPREAD>': 'Spread'
    })
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')
    df = df.reindex(daily_index)
    df.drop(['TickVolume', 'Volume', 'Spread'], axis = 1, inplace = True)
    df[(df.index.dayofweek == 5) | (df.index.dayofweek == 6)] = np.nan
    return df

file_path = '/Users/pustak/Desktop/G10 Carry Portfolio/Currency Price Historical Data - Meta Trader/EURUSD.csv'



