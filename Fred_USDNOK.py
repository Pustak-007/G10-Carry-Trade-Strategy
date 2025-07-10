import yfinance as yf 
from fredapi import Fred 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
api_key = "23dd8644a8456a82f3dc0e07c51e2a9b"
fred = Fred(api_key = api_key)
pd.set_option('display.max_rows', None)
start = pd.Timestamp(2001, 7, 16)
end = pd.Timestamp(2003,5,1)
#temp_range = pd.date_range(start = pd.Timestamp(2003, 2, 1), end = pd.Timestamp(2004,7,1))
df = yf.download(tickers = 'USDNOK=X', start =start, end = end )
temp_index = pd.date_range(start = start, end = end, freq = 'D')
df = df.reindex(temp_index)
df = df['Close']
df = df.rename(columns = {'USDNOK=X':'Close'})
x = df.index
y = df['Close']
fig, ax = plt.subplots()
ax.plot(x,y, color = 'red', label = 'Yahoo')
my_data = fred.get_series("DEXNOUS", start, end )
df2 = my_data.to_frame(name = 'Close')
x = df2.index
y = df2['Close']
ax.plot(x,y, color = 'blue', label = 'Fred')
correlation = df['Close'].corr(df2['Close'])
print(correlation)
df2 = my_data.to_frame(name = 'Close')
x = df2.index
y = df2['Close']
ax.plot(x,y)
plt.legend(loc = 'upper right')
plt.show()


