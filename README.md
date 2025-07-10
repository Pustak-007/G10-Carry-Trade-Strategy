# G10 FX Carry Trade: A Systematic Backtest (2002-2025)

## Overview
This repository contains the Python code and analysis for a comprehensive backtest of a systematic G10 foreign exchange carry trade strategy, spanning January 2002 to early 2025. The project evaluates the historical performance of the FX carry trade, a prominent alternative risk premium, across various market regimes, including the pre-GFC "golden era," the 2008 financial crisis, the zero-interest-rate policy (ZIRP) period, and the COVID-19 market crash. It also explores the potential revival of the carry trade post-COVID. Detailed findings are presented in the accompanying PDF report.

## Key Features
- **Systematic Strategy**: Implements a monthly rebalanced, dollar-neutral portfolio that goes long on the top 3 and shorts the bottom 3 G10 currencies based on their 3-month interbank rates.
- **Professional Performance Metrics**: Calculates key indicators, including Annualized Return, Volatility, Sharpe Ratio, and Maximum Drawdown.
- **Regime Analysis**: Segments the backtest into distinct economic periods to highlight the strategy’s drivers and risks.
- **Modular Codebase**: Written in Python with an emphasis on clean, modular, and reusable code.
- **Visualization**: Includes intuitive visualizations of relevant curves within their respective modules.

- **Data Retrieval and Filling**: Fred Interbank data is only available upto monthly level, as we need to calculate the Carry PnL Daily, this data has been forward filled. Interbank Data is obtained from Fred API, and Forex Spot data from combination of Pepperstone's brokerage service through metaTrader5 (8 Major Pairs) and Yahoo Finance (1 Major Pair).


## Technologies Used
- **Language**: Python 3.12.5
- **Core Libraries**: NumPy, pandas, matplotlib, yfinance, fredapi
- **Secondary Library**: dukascopy-python
- **Data Sources**:
  - Federal Reserve Economic Data (FRED) via fredapi
  - Yahoo Finance via yfinance
  - Pepperstone’s brokerage service (extracted from MetaTrader 5)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Pustak-007/G10-Carry-Trade-Strategy.git
   ```
2. Install the required dependencies:
   ```
   pip install pandas matplotlib yfinance fredapi dukascopy-python
   Note: dukascopy-python is not explicitly required for this code to run, I used it to assess if there were discrepencies (worth noting) in  historical price data between different APIs.
   ```
3. Ensure you have API access configured for fredapi and any necessary credentials for Pepperstone’s MetaTrader 5 data extraction. If you are using a mac, installation of MetaTrader 5 API is not possible, so either have a virtual box downloaded, or have the data downloaded locally on to your mac as I have done.

## Usage
The codebase is modular, allowing users to explore specific components of the strategy. Below is a guide to the key modules:

- **Total_PnL.py**: View the complete Profit and Loss (PnL) dataset or select specific columns for targeted analysis.
- **Interbank_data.py**: Handles extraction and processing of 3-month interbank rate data.
- **FX_data.py**: Manages retrieval and processing of forex price data.
- **construction.py**: Implements the portfolio construction logic for the carry trade strategy.
- **Carry_PnL.py**: Calculates the PnL attributed to the carry component.
- **Forex_PnL.py**: Computes the PnL from forex price movements.

- **Performance_Metrics.py**: Computes key performance metrics (e.g., Annualized Return, Sharpe Ratio, Volatility, Maximum Drawdown). A separate module called UST3MO.py has also been provided which extracts 3 Month Treasury Rates data from the Fred website. This data has been used to calculate the risk free rate in the computation of Sharpe Ratio.

- **Tear_Sheet.py**: Generates a dataframe summarizing the strategy’s performance across different market regimes, serving as the basis for the PDF report.

Visualizations are embedded in their respective modules with intuitive naming for easy identification.

Currency Price Historical Data - Meta Trader folder has csv files containing historical price data for major pairs from meta trader. Except for USDNOK (due to lack of deep historical data), daily price data for all the pairs is taken from metaTrader.



### Example
To explore the historical PnL:
```python
from Total_PnL import PnL_dataset
print(PnL_dataset)
```

## Notes
- The code assumes access to reliable data sources (FRED, Yahoo Finance, Pepperstone). Ensure proper API keys or credentials are configured.
- The analysis includes special focus on the COVID-19 market crash and post-COVID carry trade revival.
- Users can modify parameters or extend the analysis by tinkering with the modular codebase.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For questions or contributions, please open an issue or submit a pull request on the repository. You can also contact me personally at pustak@connect.hku.hk