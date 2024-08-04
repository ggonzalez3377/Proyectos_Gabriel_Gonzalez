import pandas as pd
import numpy as np
import yfinance as yf

lista_acciones = ['META', 'NVDA', 'SBUX','UAL']
df_prices = pd.DataFrame()

i = 0
for accion in lista_acciones:
    if i==0:
        tick = yf.Ticker(accion)
        tick_history = tick.history(start='2022-01-01', end='2024-01-01', interval='1d')
        tick_history = tick_history.loc[:,['Close']]
        tick_history.rename(columns={'Close':accion}, inplace=True)
        df_prices = df_prices.join(tick_history, how='outer')
        i += 1
        
    else:
        
        tick = yf.Ticker(accion)
        tick_history = tick.history(start='2022-01-01', end='2024-01-01', interval='1d')
        tick_history = tick_history.loc[:,['Close']]
        tick_history.rename(columns={'Close':accion}, inplace=True)
        df_prices = df_prices.join(tick_history, how='inner')

df_returns = pd.DataFrame(columns=lista_acciones)

for accion in lista_acciones:
    for column in df_returns.columns:
        if accion == column:
            df_returns[column] = df_prices[column].pct_change()



  
