"""
Created on Sun May 23 05:40:21 2021

@author: leoprimero
"""

import yfinance as yf, numpy as np, pandas as pd, matplotlib.pyplot as plt, markowitz as mk

#                    'AAPL','AMZN','BG','C','DE','FCX','GOOGL','INTC','JNJ','JPM','KO','MSFT','PFE','PG','PKX','WMT'

df = yf.download(['AAPL','AMZN','BG'],
                 start='2021-01-01', end='2021-05-20')['Adj Close']
df = df.loc[~(df==0).any(axis=1)] 


pond1, real, = mk.markowitzreal ( df, q=1)
pond, optimo, = mk.markowitzoptimo ( df, q=1000)

print(pond, '\n\nPortafolio Optimo:\n',optimo, sep='')
# print(pond1, '\n\nPortafolio Real:\n',real, sep='')

writer=pd.ExcelWriter('PortafolioSimonP21_05.xlsx')
pond.to_excel(writer,'optimw')
optimo.to_excel(writer,'DataOpt')
pond1.to_excel(writer,'realw')
real.to_excel(writer,'DatoReal')
writer.save()
writer.close()
