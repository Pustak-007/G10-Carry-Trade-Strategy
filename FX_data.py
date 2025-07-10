import pandas as pd
import numpy as np
import pandas as pd
import Interbank_data
import yfinance as yf
from fredapi import Fred
pd.set_option('display.max_columns', None)
api_key = "23dd8644a8456a82f3dc0e07c51e2a9b"
fred = Fred(api_key=api_key)
start = Interbank_data.start
end = Interbank_data.end
daily_index = pd.date_range(start = start, end = end, freq = 'D')
def Historical_PriceData(file_path):
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

#Functions to retrieve full price data for different pairs.
#Note the USDNOK is being obtained from the yfinance API, and the orientation of that
# -- data set is a little different than the local ones.

# We are trying to make our local data retrieval look data retrieval from yfinance but retaining 
# -- certain minor differences , just as a memory heuristic that 'USDNOK' is from yfinance

# Also important nuance to note: Metatrader is also showing data for some major holidays
# -- they are difficult to account for, because different years there seem to be different length of
# -- closure periods - around christmas. So, you can have USDNOK data as a kind of reference that which
# -- days were the ones where NY session was closed, so the tickvolume corresponding to that data in MT5
# -- is also lower. Hope this makes sense!

def giveEURUSD_FullPrice_data():
    path = '/Users/pustak/Desktop/G10 Carry Portfolio/Currency Price Historical Data - Meta Trader/EURUSD.csv'
    df = Historical_PriceData(path)
    level_0 = ['Open', 'High', 'Low', 'Close']
    level_1 = ['EURUSD=X'] * 4
    level_names = ['Price', 'Ticker']
    multi_index_column = pd.MultiIndex.from_arrays([level_0, level_1], names=level_names)
    df.columns = multi_index_column
    return df

def giveUSDJPY_FullPrice_data():
    path = '/Users/pustak/Desktop/G10 Carry Portfolio/Currency Price Historical Data - Meta Trader/USDJPY.csv'
    df = Historical_PriceData(path)
    level_0 = ['Open', 'High', 'Low', 'Close']
    level_1 = ['USDJPY=X'] * 4
    level_names = ['Price', 'Ticker']
    multi_index_column = pd.MultiIndex.from_arrays([level_0, level_1], names=level_names)
    df.columns = multi_index_column
    return df

def giveGBPUSD_FullPrice_data():
    path = '/Users/pustak/Desktop/G10 Carry Portfolio/Currency Price Historical Data - Meta Trader/GBPUSD.csv'
    df = Historical_PriceData(path)
    level_0 = ['Open', 'High', 'Low', 'Close']
    level_1 = ['GBPUSD=X'] * 4
    level_names = ['Price', 'Ticker']
    multi_index_column = pd.MultiIndex.from_arrays([level_0, level_1], names=level_names)
    df.columns = multi_index_column
    return df

def giveAUDUSD_FullPrice_data():
    path = '/Users/pustak/Desktop/G10 Carry Portfolio/Currency Price Historical Data - Meta Trader/AUDUSD.csv'
    df = Historical_PriceData(path)
    level_0 = ['Open', 'High', 'Low', 'Close']
    level_1 = ['AUDUSD=X'] * 4
    level_names = ['Price', 'Ticker']
    multi_index_column = pd.MultiIndex.from_arrays([level_0, level_1], names=level_names)
    df.columns = multi_index_column
    return df

def giveUSDCAD_FullPrice_data():
    path = '/Users/pustak/Desktop/G10 Carry Portfolio/Currency Price Historical Data - Meta Trader/USDCAD.csv'
    df = Historical_PriceData(path)
    level_0 = ['Open', 'High', 'Low', 'Close']
    level_1 = ['USDCAD=X'] * 4
    level_names = ['Price', 'Ticker']
    multi_index_column = pd.MultiIndex.from_arrays([level_0, level_1], names=level_names)
    df.columns = multi_index_column
    return df

def giveUSDCHF_FullPrice_data():
    path = '/Users/pustak/Desktop/G10 Carry Portfolio/Currency Price Historical Data - Meta Trader/USDCHF.csv'
    df = Historical_PriceData(path)
    level_0 = ['Open', 'High', 'Low', 'Close']
    level_1 = ['USDCHF=X'] * 4
    level_names = ['Price', 'Ticker']
    multi_index_column = pd.MultiIndex.from_arrays([level_0, level_1], names=level_names)
    df.columns = multi_index_column
    return df

def giveUSDSEK_FullPrice_data():
    path = '/Users/pustak/Desktop/G10 Carry Portfolio/Currency Price Historical Data - Meta Trader/USDSEK.csv'
    df = Historical_PriceData(path)
    level_0 = ['Open', 'High', 'Low', 'Close']
    level_1 = ['USDSEK=X'] * 4
    level_names = ['Price', 'Ticker']
    multi_index_column = pd.MultiIndex.from_arrays([level_0, level_1], names=level_names)
    df.columns = multi_index_column
    return df

def giveNZDUSD_FullPrice_data():
    path = '/Users/pustak/Desktop/G10 Carry Portfolio/Currency Price Historical Data - Meta Trader/NZDUSD.csv'
    df = Historical_PriceData(path)
    level_0 = ['Open', 'High', 'Low', 'Close']
    level_1 = ['NZDUSD=X'] * 4
    level_names = ['Price', 'Ticker']
    multi_index_column = pd.MultiIndex.from_arrays([level_0, level_1], names=level_names)
    df.columns = multi_index_column
    return df

def giveUSDNOK_FullPrice_data():
    df = yf.download(tickers= 'USDNOK=X', start = start, end = end)
    df = df.reindex(daily_index)
    df.drop('Volume', axis = 1, inplace = True)
    start_for_fred_data = pd.Timestamp(2003,5,2)
    end_for_fred_data = pd.Timestamp(2003,11,30)
    new_df_fred = fred.get_series("DEXNOUS", start, end).to_frame(name = 'Close')
    df.loc[start_for_fred_data:end_for_fred_data] = new_df_fred[start_for_fred_data:end_for_fred_data]
    return df

Helper_List = ['EURUSD', 'USDJPY', 'GBPUSD', 'AUDUSD', 'USDCAD', 
                            'USDCHF', 'NZDUSD', 'USDSEK', 'USDNOK']

function_map = {
    'EURUSD': giveEURUSD_FullPrice_data(),
    'USDJPY': giveUSDJPY_FullPrice_data(),
    'GBPUSD': giveGBPUSD_FullPrice_data(),
    'AUDUSD': giveAUDUSD_FullPrice_data(),
    'USDCAD': giveUSDCAD_FullPrice_data(),
    'USDCHF': giveUSDCHF_FullPrice_data(),
    'NZDUSD': giveNZDUSD_FullPrice_data(),
    'USDSEK': giveUSDSEK_FullPrice_data(),
    'USDNOK': giveUSDNOK_FullPrice_data()
}

Concat_Set_for_ClosePrice_DataSet = [function_map[pair]['Close'] for pair in Helper_List]
ClosePrice_DataSet_ForAll = pd.concat(Concat_Set_for_ClosePrice_DataSet, axis = 1)
ClosePrice_DataSet_ForAll.loc[pd.isna(ClosePrice_DataSet_ForAll['USDNOK=X'])] = np.nan
#This line here makes sure that when there is a holiday every pair's value is NaN
# -- This makes sure there is no ambiguity in the interpretation of data and keeps things consistent

function_map_2 = {
    'EURUSD': ClosePrice_DataSet_ForAll['EURUSD=X'],
    'USDJPY': ClosePrice_DataSet_ForAll['USDJPY=X'],
    'GBPUSD': ClosePrice_DataSet_ForAll['GBPUSD=X'],
    'USDCHF': ClosePrice_DataSet_ForAll['USDCHF=X'],
    'AUDUSD': ClosePrice_DataSet_ForAll['AUDUSD=X'],
    'NZDUSD': ClosePrice_DataSet_ForAll['NZDUSD=X'],
    'USDCAD': ClosePrice_DataSet_ForAll['USDCAD=X'],
    'USDNOK': ClosePrice_DataSet_ForAll['USDNOK=X'],
    'USDSEK': ClosePrice_DataSet_ForAll['USDSEK=X']
}

ClosePriceWithPercentageChange_DataSet_ForAll = pd.DataFrame()
for pair, data in function_map_2.items():
    ClosePriceWithPercentageChange_DataSet_ForAll[pair] = data
    ClosePriceWithPercentageChange_DataSet_ForAll[f'{pair}_pct_change'] = data.ffill().pct_change() * 100
ClosePrice_PercentageChange_DataSet = pd.DataFrame()
for pair, data in function_map_2.items():
    ClosePrice_PercentageChange_DataSet[f'{pair}_pct_change'] = data.ffill().pct_change() * 100
if __name__ == "__main__":
 print(ClosePriceWithPercentageChange_DataSet_ForAll)