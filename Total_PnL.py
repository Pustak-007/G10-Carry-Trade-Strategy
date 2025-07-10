import pandas as pd
import Interbank_data
import numpy as np
import Carry_PnL
import Forex_PnL
if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('display.min_rows', 100)
PnL_dataset = pd.DataFrame()
PnL_dataset.index = Interbank_data.daily_index
PnL_dataset['FX_long_Basket_Return'] = PnL_dataset.index.to_series().apply(Forex_PnL.give_Average_Long_Return)
PnL_dataset['FX_short_Basket_Return'] = PnL_dataset.index.to_series().apply(Forex_PnL.give_Average_Short_Return)
PnL_dataset['FX_daily_return'] = PnL_dataset.index.to_series().apply(Forex_PnL.give_total_daily_fx_return)
PnL_dataset['Carry_long_Basket_Return'] = PnL_dataset.index.to_series().apply(Carry_PnL.give_average_long_IB_rate)
PnL_dataset['Carry_short_Basket_Return'] = PnL_dataset.index.to_series().apply(Carry_PnL.give_average_short_IB_rate)
PnL_dataset['Carry_daily_return'] = PnL_dataset.index.to_series().apply(Carry_PnL.give_daily_IB_rate_differential)
def total_daily_PnL(Date):
    carry = Carry_PnL.give_daily_IB_rate_differential(Date)
    spot_diff = Forex_PnL.give_total_daily_fx_return(Date)
    return carry + spot_diff
PnL_dataset['Daily_PnL_History'] = PnL_dataset.index.to_series().apply(total_daily_PnL)
if __name__ == "__main__":
    print(PnL_dataset[['Carry_long_Basket_Return', 'Carry_short_Basket_Return', 'Carry_daily_return']])


