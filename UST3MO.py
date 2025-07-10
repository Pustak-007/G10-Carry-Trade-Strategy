import pandas as pd
from fredapi import Fred
api_key = "23dd8644a8456a82f3dc0e07c51e2a9b"
start = pd.Timestamp(2002,1,1)
end = pd.Timestamp(2025,1,1)
daily_index = pd.date_range(start = start, end = end, freq = "D")
fred = Fred(api_key = api_key)
def give_USTY3MO():
    try:
        data = fred.get_series("DGS3MO", start, end)
        df = data.to_frame(name = "Rates")
        df = df.reindex(daily_index)
        df.index.name = 'Date'
        return df

    except ValueError as err:
        print(f"{err}: The code doesn't exist in fred library") 
if __name__ == "__main__":   
 print(give_USTY3MO().mean())  