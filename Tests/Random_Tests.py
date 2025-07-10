import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#Code for access to the modules of the larger G10 Folder.
import yfinance as yf 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
pd.set_option('display.max_rows', None)
start = pd.Timestamp(2001, 1, 16)
end = pd.Timestamp(2005,5,1)
temp_index = pd.date_range(start,end)
data = yf.download(tickers='USDNOK=X', start = start, end = end)
df = data.reindex(temp_index)
df = df['Close']
print(df)
#temp_range = pd.date_range(start = pd.Timestamp(2003, 2, 1), end = pd.Timestamp(2004,7,1))

