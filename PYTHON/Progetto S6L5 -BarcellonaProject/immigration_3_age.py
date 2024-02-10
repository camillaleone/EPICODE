# Analizziamo la distribuzione degli immigrati per fascia di età
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Carico il dataset
file_name = 'immigrants_emigrants_by_age.csv'
df_age = pd.read_csv(file_name)

# Raggruppiamo per età e calcoliamo la somma degli immigrati
immigrati_per_eta = df_age.groupby("Age")["Immigrants"].sum().sort_index(ascending=False)

# Creiamo un grafico a barre orizzontali
plt.figure(figsize=(10, 6))
immigrati_per_eta.plot(kind='barh', color='blue')

plt.title("Totale Immigrazione per fascia d'età")
plt.xlabel('Numero di Immigrati')
plt.ylabel("Fascia d'età")
plt.show()
