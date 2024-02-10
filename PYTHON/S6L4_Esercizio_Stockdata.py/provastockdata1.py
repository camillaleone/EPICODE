import pandas as pd
import matplotlib.pyplot as plt

file_name = "./stockdata.csv"
dataset = pd.read_csv(file_name)

# Andamento delle azioni di Microsoft
plt.figure(figsize=(10, 6))
plt.plot(dataset['Date'], dataset['MSFT'], label='MSFT Stock Value')
plt.title('Andamento Azioni Microsoft')
plt.xlabel('Date')
plt.ylabel('Stock Value')
plt.legend()
plt.show()

# Estrazione prime 5 righe delle colonne MSFT e date
first_5_rows = dataset.head(5)

# Grafico prime 5 righe
plt.figure(figsize=(8, 5))
plt.plot(first_5_rows['Date'], first_5_rows['MSFT'], marker='o', linestyle='-', color='b')
plt.title('Prime cinque righe')
plt.xlabel('Date')
plt.ylabel('Stock Value')
plt.show()

# Estrazione ultime 5 righe delle colonne MSFT e date
last_5_rows = dataset.tail(5)

# Grafico per le ultime 5 righe
plt.figure(figsize=(8, 5))
plt.plot(last_5_rows['Date'], last_5_rows['MSFT'], marker='o', linestyle='-', color='r')
plt.title('Ultime cinque righe')
plt.xlabel('Date')
plt.ylabel('Stock Value')
plt.show()