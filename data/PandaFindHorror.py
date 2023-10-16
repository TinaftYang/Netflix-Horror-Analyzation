import pandas as pd

csv_file = '/Users/TY/Desktop/data/archive/2023 data/titles.csv'

df = pd.read_csv(csv_file)

filtered_df = df[df['genres'].str.contains('horror', case=False, na=False)]

filtered_df.to_csv('/Users/TY/Desktop/data/archive/2023 data/titleshorror.csv', index=False)

print(filtered_df)
