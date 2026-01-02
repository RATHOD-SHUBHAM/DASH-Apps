import pandas as pd
import pandas_datareader.data as web
import datetime

# https://stooq.com/
start = datetime.datetime(2023, 1, 1)
end = datetime.datetime(2024, 12, 3)

df = web.DataReader(['AMZN','GOOGL','FB','PFE','MRNA','BNTX'],
                    'stooq', start=start, end=end)
print(df.head())

df = df.stack().reset_index()
print(df.head())

df.rename(columns={'level_0': 'Date'}, inplace=True)
print(df.head())

df.to_csv("mystocks.csv", index=False)
df = pd.read_csv("mystocks.csv")
print(df.head())