import pandas as pd
import matplotlib.pyplot as plt

file_name = "./stockdata.csv"
dataset = pd.read_csv(file_name)

# Colonne
colonne = ["MSFT", "IBM", "SBUX", "AAPL", "GSPC"]

# Andamento di tutte le azioni sullo stesso grafico
dataset[colonne].plot(figsize=(12, 8), marker='s', linestyle='-')

# Nomi assi e titolo grafico
plt.xlabel("Data")
plt.ylabel("Valore")
plt.title("Andamento Azioni")

plt.legend(loc='lower right')

plt.show()