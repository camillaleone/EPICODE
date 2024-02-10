# Analizziamo la distribuzione di genere tra gli immigrati tramite grafico a torta
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Carico il dataset
file_name = 'immigrants_emigrants_by_sex.csv'
df_sex = pd.read_csv(file_name)

# Calcolo la somma degli immigrati
Immigrati_per_sesso = df_sex.groupby('Gender')['Immigrants'].sum()

# Grafico a torta
Immigrati_per_sesso.plot(kind='pie', autopct='%1.2f%%', startangle=90, colors=['violet', 'green'])

# Aggiungiamo il titolo
plt.title('Distribuzione di Genere tra gli Immigrati')
plt.ylabel('')
plt.show()