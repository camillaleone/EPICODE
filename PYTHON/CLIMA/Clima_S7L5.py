import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv(r"C:\Users\camil\Desktop\EPICODE\PYTHON\CLIMA\dataset_climatico.csv")
df.dropna(inplace=True)  #Elimino valori mancanti 

# Normalizzazione Z-score
colonne_norm = ['temperatura_media', 'precipitazioni', 'umidita', 'velocita_vento']
df[colonne_norm] = (df[colonne_norm] - df[colonne_norm].mean()) / df[colonne_norm].std()


#Analisi Esplorativa dei Dati
#Calcolare statistiche descrittive (media, mediana, deviazione standard) per ogni variabile
descrizione = df.describe()
print(descrizione)

#Creo i grafici 
for colonna in colonne_norm:
    plt.figure(figsize=(12, 5))
    # Istogramma per ogni colonna
    plt.subplot(1, 2, 1)
    sns.histplot(df[colonna], bins=40)
    plt.title('Istogramma di ' + colonna)
    # Box plot
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df[colonna])
    plt.title('Box plot di ' + colonna)
    plt.show

#Analisi di Correlazione
# Utilizzare una heatmap per visualizzare la correlazione tra le diverse variabili meteorologiche. 
# Identificare eventuali correlazioni significative (es. tra temperatura e umidità).
# Calcolare la matrice di correlazione
matrice_correlazione = df[colonne_norm].corr()

# Creazione di un grafico di regressione lineare con correlazione annotata
plt.figure(figsize=(8, 6))
sns.regplot(x="temperatura_media", y="precipitazioni", data=df)
plt.title('Grafico di Regressione tra Temperatura Media e Precipitazioni')
plt.xlabel('Temperatura Media')
plt.ylabel('Precipitazioni')
plt.show()