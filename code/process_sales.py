import pandas as pd
import os

data_folder = 'data'
files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]

dfs = []

for f in files:
    df = pd.read_csv(os.path.join(data_folder, f))
    df = df[df['product'] == 'Pink Morsel']
    df['sales'] = df['quantity'] * df['price']
    df = df[['sales', 'date', 'region']]
    dfs.append(df)

final_df = pd.concat(dfs, ignore_index=True)
final_df.to_csv('formatted_sales.csv', index=False)