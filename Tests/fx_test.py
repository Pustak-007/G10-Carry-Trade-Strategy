import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#Code for access to the modules of the larger G10 Folder.
import Interbank_data 
import construction
import pandas as pd 
import numpy as np 
from fredapi import Fred 
from datetime import datetime 
import yfinance as yf 
api_key = "23dd8644a8456a82f3dc0e07c51e2a9b"
fred = Fred(api_key = api_key)
start = Interbank_data.start
end = Interbank_data.end
import yfinance as yf

def give_EURUSD_rate():
    ticker = "EURUSD=X"
    data = yf.download(ticker, start=start, end=end)
    df = data['Close']
    return df

def give_USDJPY_rate():
    ticker = "USDJPY=X"
    data = yf.download(ticker, start=start, end=end)
    df = data['Close']
    return df

def give_GBPUSD_rate():
    ticker = "GBPUSD=X"
    data = yf.download(ticker, start=start, end=end)
    df = data['Close']
    return df

def give_USDCAD_rate():
    ticker = "USDCAD=X"
    data = yf.download(ticker, start=start, end=end)
    df = data['Close']
    return df

def give_AUDUSD_rate():
    ticker = "AUDUSD=X"
    data = yf.download(ticker, start=start, end=end)
    df = data['Close']
    return df

def give_NZDUSD_rate():
    ticker = "NZDUSD=X"
    data = yf.download(ticker, start=start, end=end)
    df = data['Close']
    return df

def give_USDCHF_rate():
    ticker = "USDCHF=X"
    data = yf.download(ticker, start=start, end=end)
    df = data['Close']
    return df

def give_USDSEK_rate():
    ticker = "USDSEK=X"
    data = yf.download(ticker, start=start, end=end)
    df = data['Close']
    return df

def give_USDNOK_rate():
    ticker = "USDNOK=X"
    data = yf.download(ticker, start=start, end=end)
    df = data['Close']
    return df

EURUSD = give_EURUSD_rate()
USDJPY = give_USDJPY_rate()
GBPUSD = give_GBPUSD_rate()
USDCAD = give_USDCAD_rate()
AUDUSD = give_AUDUSD_rate()
NZDUSD = give_NZDUSD_rate()
USDCHF = give_USDCHF_rate()
USDSEK = give_USDSEK_rate()
USDNOK = give_USDNOK_rate()

major_pairs = [EURUSD, USDJPY, GBPUSD, USDCAD, AUDUSD, NZDUSD, USDCHF, USDSEK, USDNOK]
# List of pair names (strings) and their corresponding Series
pair_dict = {
    'EURUSD': EURUSD,
    'USDJPY': USDJPY,
    'GBPUSD': GBPUSD,
    'USDCAD': USDCAD,
    'AUDUSD': AUDUSD,
    'NZDUSD': NZDUSD,
    'USDCHF': USDCHF,
    'USDSEK': USDSEK,
    'USDNOK': USDNOK
}

daily_index = Interbank_data.daily_index
Spot_FX_dataset = pd.DataFrame()
Spot_FX_dataset.index = daily_index
for pair_name, pair_data in pair_dict.items():
    Spot_FX_dataset[pair_name] = pair_data
    Spot_FX_dataset[f'{pair_name}_pct_change'] = pair_data.pct_change() * 100
Spot_FX_dataset = Spot_FX_dataset.drop(pd.Timestamp(2003,12,31))    
#print(Spot_FX_dataset)
print(Spot_FX_dataset)


