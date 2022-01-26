# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 23:02:13 2022

@author: richa
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 20:29:09 2022

@author: richa
"""
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import math
from datetime import date


tday = date.today()
tday_str = tday.strftime("%Y-%m-%d")

# =============================================================================
# tickers = ["AZN.ST","ATCO-A.ST","ABB.ST","INVE-B.ST","VOLV-B.ST","NDA-SE.ST","EQT.ST","ERIC-B.ST","HEXA-B.ST","SAND.ST","NOKIA-SEK.ST","ASSA-B.ST","HM-B.ST","EVO.ST", \
#            "SEB-A.ST","EPI-A.ST","VOLCAR-B.ST","SWED-A.ST","SHB-A.ST","ESSITY-B.ST","LATO-B.ST","NIBE-B.ST","TELIA.ST","STE-R.ST","ALFA.ST","INDU-C.ST","LUND-B.ST","8TRA.ST", \
#            "SWMA.ST","SCA-B.ST","BALD-B.ST","BOL.ST","LIFCO-B.ST","LUNE.ST","EMBRAC-B.ST","SKF-B.ST","SKA-B.ST","TEL2-B.ST","GETI-B.ST","SAGA-B.ST","SBB-B.ST","INDT.ST", \
#            "SBB-D.ST","SAGA-D.ST","ALIV-SDB.ST","KINV-B.ST","STOR-B.ST","CAST.ST","HOLM-B.ST","HUSQ-B.ST","SINCH.ST","TREL-B.ST","BEIJ-B.ST","LUMI.ST","SSAB-A.ST","ELUX-B.ST", \
#            "SOBI.ST","VOLO-PREF.ST","VITR.ST","AXFO.ST","WALL-B.ST","AAK.ST","THULE.ST","SWEC-B.ST","ADDT-B.ST","AZA.ST","FABG.ST","MCOV-B.ST","SECU-B.ST","EKTA-B.ST","HPOL-B.ST",\
#            "SAVE.ST","VNE-SDB.ST","CORE-D.ST","CORE-PREF.ST","CORE-B.ST","ALIF-B.ST","DOM.ST","TIETOS.ST","OP-PREF.ST","PEAB-B.ST","SAAB-B.ST","BILL.ST","NENT-A.ST","INTRUM.ST",\
#            "NENT-B.ST","WIHL.ST","TRUE-B.ST","SECT-B.ST","NYF.ST","CINT.ST","HUFV-A.ST","VIMIAN.ST","NOLA-B.ST","ATRLJ-B.ST","ARJO-B.ST","TIGO-SDB.ST","JM.ST","PNDX-B.ST","AFRY.ST",\
#            "MIPS.ST","KIND-SDB.ST","BURE.ST","BRAV.ST","CATE.ST","FPAR-A.ST","HMS.ST","LIAB.ST","FPAR-D.ST","TROAX.ST","ARION-SDB.ST","PDX.ST","SF.ST","LOOMIS.ST","SYSR.ST","MYCR.ST",\
#            "EPRO-B.ST","INSTAL.ST","NCC-B.ST","LUG.ST","CRED-A.ST","OP-PREFB.ST","RATO-B.ST","VOLO.ST","HEM.ST","NP3.ST","FOI-B.ST","HTRO.ST","DIOS.ST","SDIP-B.ST","BEIA-B.ST",\
#            "PLAZ-B.ST","KFAST-B.ST","VIT-B.ST","OX2.ST","VESTUM.ST","BICO.ST","SDIP-PREF.ST","FPAR-PREF.ST","BUFAB.ST","BILI-A.ST","KARO.ST","FIL.ST","NCAB.ST","ANOD-B.ST","BIOT.ST",\
#            "MTRS.ST","SECARE.ST","CARY.ST","HEBA-B.ST","ALM.ST","ALM-PREF.ST","BFG.ST","BOOZT.ST","CIBUS.ST","SKIS-B.ST","RVRC.ST","SUS.ST","DUST.ST","ALLIGO-B.ST","BHG.ST","GRNG.ST",\
#            "SAS.ST","MTG-B.ST","STORY-B.ST","VNV.ST"]
# =============================================================================

tickers = ["AZN.ST","ATCO-A.ST","ABB.ST","INVE-B.ST","VOLV-B.ST","NDA-SE.ST","EQT.ST","ERIC-B.ST","HEXA-B.ST","SAND.ST","NOKIA-SEK.ST","ASSA-B.ST","HM-B.ST","EVO.ST", \
            "SEB-A.ST","EPI-A.ST","VOLCAR-B.ST","SWED-A.ST","SHB-A.ST","ESSITY-B.ST","LATO-B.ST","NIBE-B.ST","TELIA.ST","STE-R.ST","ALFA.ST","INDU-C.ST","LUND-B.ST","8TRA.ST", \
            "SWMA.ST","SCA-B.ST","BALD-B.ST","BOL.ST","LIFCO-B.ST","LUNE.ST","EMBRAC-B.ST","SKF-B.ST","SKA-B.ST","TEL2-B.ST","GETI-B.ST","SAGA-B.ST","SBB-B.ST","INDT.ST", \
            "ALIV-SDB.ST","KINV-B.ST","STOR-B.ST","CAST.ST","HOLM-B.ST","HUSQ-B.ST","SINCH.ST","TREL-B.ST","BEIJ-B.ST","LUMI.ST","SSAB-A.ST","ELUX-B.ST", \
            "SOBI.ST","VITR.ST","AXFO.ST","WALL-B.ST","AAK.ST","THULE.ST","SWEC-B.ST","ADDT-B.ST","AZA.ST","FABG.ST","MCOV-B.ST","SECU-B.ST","EKTA-B.ST","HPOL-B.ST",\
            "SAVE.ST","VNE-SDB.ST","CORE-B.ST","ALIF-B.ST","DOM.ST","TIETOS.ST","PEAB-B.ST","SAAB-B.ST","BILL.ST","INTRUM.ST",\
            "NENT-B.ST","WIHL.ST","TRUE-B.ST","SECT-B.ST","NYF.ST","CINT.ST","HUFV-A.ST","VIMIAN.ST","NOLA-B.ST","ATRLJ-B.ST","ARJO-B.ST","TIGO-SDB.ST","JM.ST","PNDX-B.ST","AFRY.ST",\
            "MIPS.ST","KIND-SDB.ST","BURE.ST","BRAV.ST","CATE.ST","FPAR-A.ST","HMS.ST","LIAB.ST","TROAX.ST","ARION-SDB.ST","PDX.ST","SF.ST","LOOMIS.ST","SYSR.ST","MYCR.ST",\
            "EPRO-B.ST","INSTAL.ST","NCC-B.ST","LUG.ST","CRED-A.ST","RATO-B.ST","VOLO.ST","HEM.ST","NP3.ST","FOI-B.ST","HTRO.ST","DIOS.ST","SDIP-B.ST","BEIA-B.ST",\
            "PLAZ-B.ST","KFAST-B.ST","VIT-B.ST","OX2.ST","VESTUM.ST","BICO.ST","BUFAB.ST","BILI-A.ST","KARO.ST","FIL.ST","NCAB.ST","ANOD-B.ST","BIOT.ST",\
            "MTRS.ST","SECARE.ST","CARY.ST","HEBA-B.ST","ALM.ST","BFG.ST","BOOZT.ST","CIBUS.ST","SKIS-B.ST","RVRC.ST","SUS.ST","DUST.ST","ALLIGO-B.ST","BHG.ST","GRNG.ST",\
            "SAS.ST","MTG-B.ST","STORY-B.ST","VNV.ST"]
tickers = ["HTRO.ST", "SECARE.ST"]
# =============================================================================

#tickers = ["EVO","SINCH","LATO_B","KINV_B","NIBE_B","EQT","MIPS","STORY_B","SF","PDX","SBB_B","BALD_B","SAGA_B","INDT","LIFCO_B","LAGR_B"]
stock_returns = {}

for x in tickers:
    #=============================================================================
    # =============================================================================
    hist = yf.download(x, start='2015-01-01', end=tday_str)
    # =============================================================================
    #=============================================================================
    # 
    # hist = yf.download('ALIG.ST CCC.ST BALCO.ST BERG-B.ST'
    #                    ' COIC.ST HLDX.S LIAB.ST MTRS.ST NCC-B.ST'
    #                    ' NMAN.ST SYSR.ST', start='2015-01-01', end=tday_str)
    
    close_prices = hist["Adj Close"]#.dropna(how='all').fillna(0)
    high_prices = hist["High"]
    low_prices = hist["Low"]
    avg_prices = (close_prices + high_prices + low_prices)/3
    #volume traded each day
    Q = hist["Volume"].dropna(how='all').fillna(0).astype(float)
    #average daily volume traded each day
    V = Q.rolling(60).mean().shift(1)
    #high volume indicator
    high_volume_ind = Q/V > 5
    #calculate daily returns
    ret_daily = close_prices.pct_change()
    #calculate volatility
    sigma = ret_daily.rolling(20).std().shift(1)

    buy_signal = high_volume_ind & (ret_daily > 3*sigma)
    buy_signal[:]
    ret_100d = close_prices.pct_change(60)
    
    #calc transaction cost
    fee = 0.0002
    #market impact cost of my order
    daily_turnover = avg_prices*Q
    avg_daily_turnover = daily_turnover.rolling(10).mean()
    my_order_size = 250000
    #numerical scaling constant
    Y = 0.7
    slippage = Y*sigma*np.sqrt(my_order_size/avg_daily_turnover)
    
    long_returns_daily = ret_100d*buy_signal.shift(60)# - 2*fee*buy_signal.shift(60) - 1*slippage.shift(-60)*buy_signal.shift(60) - 1*slippage*buy_signal.shift(60)

    stock_returns.update(long_returns_daily)#+short_returns_daily)

returns = pd.DataFrame(list(stock_returns.items()),columns=["index", "returns"])
returns = returns.set_index("index")
returns = returns.sort_index()

cum_ret_w_zeroes = (1 + returns["returns"]).cumprod()

returns_wo_zeroes = returns.replace(False,np.nan)
#Cumulative returns 
#cum_ret =starting_capital +  np.cumsum(daily_returns_strat) #
cum_ret =(1 + returns_wo_zeroes["returns"]).cumprod()

#cum_long_ret =  (1 + avg_long_ret).cumprod()
#cum_short_ret =  (1 + avg_short_ret).cumprod()


###########################################
#stats for basic strategy
##########################################

print("   ")
print('Market impact deviation ')
CAGR = cum_ret[cum_ret.last_valid_index()]**(1/7)-1
print("CAGR " + str(CAGR))
mean_ret = returns_wo_zeroes.mean()
vol = (returns_wo_zeroes.std())
ann_vol = returns_wo_zeroes.std()*math.sqrt(buy_signal.sum()/7)
sharpe = CAGR/ann_vol
kelly_f = mean_ret/vol**2
print("Return per trade " + str(returns_wo_zeroes.mean()))
print("Volatility " + str(ann_vol))
print("Sharpe " + str(sharpe))
print("Kelly fraction " + str(kelly_f))
#maxiumum drawdown
Roll_Max = cum_ret.cummax()
Daily_Drawdown = cum_ret/Roll_Max - 1.0
Max_Daily_Drawdown = Daily_Drawdown.cummin()
print("Max drawdown " + str(Max_Daily_Drawdown.tail(1)[0]))

#plots
plt.plot(cum_ret_w_zeroes)