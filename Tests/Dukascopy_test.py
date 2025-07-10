import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#Code for access to the modules of the larger G10 Folder.
from datetime import datetime
import pandas as pd
import dukascopy_python
from dukascopy_python.instruments import INSTRUMENT_FX_CROSSES_USD_NOK
pd.set_option('display.min_rows', 100)

df = dukascopy_python.fetch(
    INSTRUMENT_FX_CROSSES_USD_NOK,
    dukascopy_python.INTERVAL_DAY_1,
    dukascopy_python.OFFER_SIDE_BID,
    datetime(2000,1,1),
    datetime(2025,1,1)
)
df.drop('volume', axis = 1, inplace= True)
df.index = df.index.tz_convert(None)
print(df.head(100))