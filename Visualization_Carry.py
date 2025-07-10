import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.ticker import PercentFormatter
from Total_PnL import PnL_dataset
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import PercentFormatter

def Create_Carry_PnL_graph():
    Carry_Returns = PnL_dataset['Carry_daily_return']
    x = Carry_Returns.index
    y = Carry_Returns.values
    fig, ax = plt.subplots(2,1,sharex=True)
    ax[0].plot(x,y)
    ax[0].set_title('Carry Daily Returns')
    ax[0].set_xlabel('Date')
    ax[0].set_ylabel('Carry Daily PnL (%)')
    ax[0].yaxis.set_major_formatter(PercentFormatter(xmax = 100, decimals = 4))
    ax[0].xaxis.set_major_locator(mdates.YearLocator(base = 1))
    ax[0].xaxis.set_minor_locator(mdates.MonthLocator(interval = 3))
    y = Carry_Returns.rolling(window = 20).mean()
    ax[1].plot(x,y, color = 'orange')
    ax[1].set_xlabel('Date')
    ax[1].set_ylabel('Carry Daily PnL (%)')
    ax[1].yaxis.set_major_formatter(PercentFormatter(xmax = 100, decimals = 4))
    ax[1].set_title('Carry Daily Returns - 20 Day SMA')
    plt.tight_layout()
    plt.show()
Create_Carry_PnL_graph()