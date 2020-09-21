import pandas as pd

df = pd.read_csv('SP500.csv')
df = df[['Date', 'Close', 'Volume']]
df.columns = ['date', 'price', 'volume']

df.to_csv('df.csv')
