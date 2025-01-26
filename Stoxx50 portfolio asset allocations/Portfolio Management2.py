import datetime as dt
from re import M

import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import yfinance as yf
import numpy as np
from numpy import mean
from yahoofinancials import YahooFinancials
def yfinancials(param):
    pass

start = dt.datetime(2011,1,1)
end = dt.datetime(2021,1,1)
symbols = ["BMW.DE","DAI.DE","STLA.MI","VOW.DE","ING","SAN","BNP.PA","ISP.MI","IFX.DE","CRH","DG.PA","SIE.DE","BAS.DE","BAYN.DE","AI.PA","SAN.PA","^STOXX50E","EURUSD=X"]
data = pd.DataFrame()
for sym in symbols:
 data[sym] = yf.download(sym, start, end,interval="1mo")['Close']
data = data.dropna()
print(data.tail(120))
data[["VOW.DE","SIE.DE","SAN.PA","BNP.PA"]].plot()
plt.show()
data[["DAI.DE","AI.PA","BAS.DE","STLA.MI"]].plot()
plt.show()
data[["BMW.DE","DG.PA","SAN","ING"]].plot()
plt.show()
data[["BAYN.DE","IFX.DE","ISP.MI","CRH"]].plot()
plt.show()
data[["^STOXX50E"]].plot()
plt.show()
data[["EURUSD=X"]].plot()
plt.show()
data.to_csv('PM.csv')


