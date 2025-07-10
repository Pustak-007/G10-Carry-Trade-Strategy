import pandas as pd
import Performance_Metrics
import numpy as np
import matplotlib.pyplot as plt
if __name__ == "__main__":
   pd.set_option('display.max_columns', None)
   pd.set_option('display.width', 200)

#Overall
overall_annualized_return = Performance_Metrics.calculate_annualized_return_pct(period = 'All')
overall_annualized_volatility = Performance_Metrics.calculate_annualized_volatility(period = 'All')
overall_annualized_sharpe = Performance_Metrics.calculate_sharpe_ratio(period = 'All')
overall_max_drawdown = Performance_Metrics.calculate_max_drawdown(period = 'All')

#Pre-GFC
pre_gfc_annualized_return = Performance_Metrics.calculate_annualized_return_pct(period = 'Pre-GFC')
pre_gfc_annualized_volatility = Performance_Metrics.calculate_annualized_volatility(period = 'Pre-GFC')
pre_gfc_annualized_sharpe = Performance_Metrics.calculate_sharpe_ratio(period = 'Pre-GFC')
pre_gfc_max_drawdown = Performance_Metrics.calculate_max_drawdown(period = 'Pre-GFC')

#GFC
gfc_annualized_return = Performance_Metrics.calculate_annualized_return_pct(period = 'GFC')
gfc_annualized_volatility = Performance_Metrics.calculate_annualized_volatility(period = 'GFC')
gfc_annualized_sharpe = Performance_Metrics.calculate_sharpe_ratio(period = 'GFC')
gfc_max_drawdown = Performance_Metrics.calculate_max_drawdown(period = 'GFC')

#Post-GFC
post_gfc_annualized_return = Performance_Metrics.calculate_annualized_return_pct(period = 'Post-GFC-(Before Covid)-ZIRP')
post_gfc_annualized_volatility = Performance_Metrics.calculate_annualized_volatility(period = 'Post-GFC-(Before Covid)-ZIRP')
post_gfc_annualized_sharpe = Performance_Metrics.calculate_sharpe_ratio(period = 'Post-GFC-(Before Covid)-ZIRP')
post_gfc_max_drawdown = Performance_Metrics.calculate_max_drawdown(period = 'Post-GFC-(Before Covid)-ZIRP')

#During Covid Crash:
covid_return = Performance_Metrics.covid_return()
covid_volatility = Performance_Metrics.covid_volatility()
covid_max_drawdown = Performance_Metrics.covid_maxDrawdown()

#Post-Covid Crash
post_covid_annualized_retun = Performance_Metrics.calculate_annualized_return_pct(period = 'Post-Covid')
post_covid_annualized_volatility = Performance_Metrics.calculate_annualized_volatility(period = 'Post-Covid')
post_covid_annualized_sharpe = Performance_Metrics.calculate_sharpe_ratio(period = 'Post-Covid')
post_covid_max_drawdown = Performance_Metrics.calculate_max_drawdown(period = 'Post-Covid')


df = pd.DataFrame()
df['Overall'] = pd.Series([overall_annualized_return, overall_annualized_volatility,
                           overall_annualized_sharpe, overall_max_drawdown])

df['Pre-GFC'] = pd.Series([pre_gfc_annualized_return, pre_gfc_annualized_volatility,
                             pre_gfc_annualized_sharpe, pre_gfc_max_drawdown])

df['GFC'] = pd.Series([gfc_annualized_return, gfc_annualized_volatility,
                       gfc_annualized_sharpe, gfc_max_drawdown])

df['Post-GFC']  = pd.Series([post_gfc_annualized_return, post_gfc_annualized_volatility,
                             post_gfc_annualized_sharpe, post_gfc_max_drawdown])

df['Covid Crash'] = pd.Series([covid_return, covid_volatility,
                          np.nan, covid_max_drawdown])
df['Post-Covid'] = pd.Series([post_covid_annualized_retun, post_covid_annualized_volatility, 
                             post_covid_annualized_sharpe, post_covid_max_drawdown])
df.index = ['Annualized Return', 'Annualized Volatility', 'Annualized Sharpe', 'Max Drawdown']

print(df)
