import pandas as pd

# Carico il file 
df = pd.read_csv('covid19_italy_province_python.csv')
# Pulizia
df = df.drop('SNo', axis=1)
df = df.dropna(how='all')
df = df.drop_duplicates()
df = df.fillna(0)
# Elimino orario 
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.date

# Converti la colonna "TotalPositiveCases" da float a int
df['TotalPositiveCases'] = df['TotalPositiveCases'].astype(int)
print(df)
