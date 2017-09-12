import pandas as pd

df = pd.read_csv('birthday_opn_2017.csv')
df[['day', 'month', 'year']] = df.pop('birthday').str.split('/', 2, expand=True)
df = df.sort_values(['month', 'day', 'name'])
df.to_csv('new_birtday_opn_2017.csv', index=False)
print(df)
