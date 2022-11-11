import pandas as pd 
import yfinance as yf
import datetime as dt

perInicio = '2022-08-01'
perFin = '2022-08-10'
ticker = ['MGLU3.SA']

df = yf.download(ticker, start=perInicio, end=perFin, rounding=True);
df.sort_values(by=['Date'], inplace=True, ascending=False);
df.reset_index(inplace=True);

df = pd.concat([pd.Series(ticker, name='Ticker'), df], axis=1)

print(df)