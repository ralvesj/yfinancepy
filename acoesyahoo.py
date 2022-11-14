import pandas as pd 
import yfinance as yf # caso precise, instale o yfinance com -> pip install yfinance  
import datetime as dt

#Período inicial formato yyyy-MM-dd
perInicio = '2022-08-01' 

#Período final yyyy-MM-dd
perFin = '2022-08-10' 

#Coloque aqui os tickers da ações que você quer saber o preço
ticker = ['PETR4.SA','IRBR3.SA'] 

df = yf.download(ticker, start=perInicio, end=perFin, rounding=True);
df.sort_values(by=['Date'], inplace=True, ascending=False);
df.reset_index(inplace=True);

#Descomente a linha abaixo se quiser todas as colunas: 

#df = pd.concat([df, pd.Series(ticker, name='Ticker')], axis=1)

#acoes = df

#Aqui você tem um exemplo de como trazer colunas específicas:

acoes = df[['Date', 'Close']]

print(acoes)

#execute com -> python acoesyahoo.py
