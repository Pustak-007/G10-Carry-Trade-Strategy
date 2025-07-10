import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from Performance_Metrics import give_dataframe_with_drawdown
from matplotlib.ticker import PercentFormatter
if __name__ == "__main__":
    pd.set_option('display.max_rows', None)
df = give_dataframe_with_drawdown(period = 'All')
x = df.index
y = df['Drawdown (%)']
fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_xlabel('Date')
ax.set_ylabel('Drawdown (%)')
plt.title('Drawdown(%) of the G10 Carry Trade Strategy')
ax.xaxis.set_major_locator(mdates.YearLocator(base = 1))
ax.xaxis.set_minor_locator(mdates.MonthLocator(interval = 3))
plt.gca().yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals = 2))
ax.axhline(y = 0, color = 'gray', linestyle = ':')
plt.show()