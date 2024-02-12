import pandas as pd

# Carico il file CSV in un DataFrame
df = pd.read_csv('Comuni_python.csv',delimiter=';',skiprows=7).iloc[:-1]
# Pulizia
df = df.drop(['Unnamed: 1'],axis=1)
df= df.dropna(how='all')
df = df.drop_duplicates()
df = df.fillna(0)
df['Regione'] =df['Regione'].str.title()
df['Popolazione2011'] = df['Popolazione2011'].astype(int)
print(df)
