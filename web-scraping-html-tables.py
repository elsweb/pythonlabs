import pandas as pd

df_crypto = pd.read_html('https://coinmarketcap.com/')[0]

print(df_crypto.head())