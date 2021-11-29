# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 11:16:12 2021

@author: Richard
"""


import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import math
from datetime import date

#get prices from yahoo finance

tday = date.today()
tday_str = tday.strftime("%Y-%m-%d")
#=============================================================================
# =============================================================================
hist = yf.download('HTRO.ST', start='2015-01-01', end=tday_str)
# =============================================================================
#=============================================================================

close_prices = hist["Adj Close"]#.dropna(how='all').fillna(0)
open_prices = hist["Open"]
#high_prices = hist["High"]
#low_prices = hist["Low"]

gap = open_prices/close_prices.shift(1)-1

volumes = hist["Volume"]#.dropna(how='all').fillna(0)

cl_cl_returns = close_prices.pct_change()
cl_cl_60d_returns = close_prices.pct_change(60)


rolling_windows_volume = volumes.rolling(100, min_periods=1)
adv100 = rolling_windows_volume.mean()

r_vol = volumes/adv100.shift(1)

rolling_windows_returns = cl_cl_returns.rolling(100, min_periods=1)
volatility = rolling_windows_returns.std()

avwap = 


#signal indicator
signal_ind =   (gap>3*volatility.shift(1)) & (r_vol>3)

#measure 3 month fwd return after big gapper
strat_ret_60d_returns = cl_cl_60d_returns*signal_ind.shift(60)