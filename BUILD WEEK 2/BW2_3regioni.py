import pandas as pd


# Carico il file 
df = pd.read_csv('covid19_italy_region_python.csv')
# Pulizia
df = df.drop('SNo', axis=1)
df = df.dropna(how='all')
df = df.drop_duplicates()
# Elimino orario 
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.date
df= df.fillna(0)
# Converti la colonna "TestsPerformed" da float a int
df['TestsPerformed'] = df['TestsPerformed'].astype(int)
print(df)
