import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#Code for access to the modules of the larger G10 Folder.
import pandas as pd 
import numpy as np
import yfinance as yf
from datetime import datetime
end = datetime.now()
data = yf.download("AUDUSD=X", start="1990-01-01", end=end)
data['Percentage_chane'] = data['Close'].pct_change()
print(data)





