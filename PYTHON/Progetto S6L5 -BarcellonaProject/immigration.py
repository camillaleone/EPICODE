# Scegliete un dataset a vostro piacere (che abbia almeno un migliaio di righe e 5 colonne) e 
# analizzatelo come abbiamo imparato a fare finora: esplorate i dati sia colonna per colonna che in combinazioni di esse 
# e applicate i concetti di statistica appresi nel modulo precedente, utilizzando Python. 
# A fine giornata ognuno deve presentare un jupyter notebook pulito (non ci devono essere refusi, il codice deve compilare in ogni cella)
# che mostri l’analisi fatta, compresa di grafici e spiegazioni inerenti.

# Abbiamo scelto un dataset sulla città di Barcellona, 
# e procediamo ad analizzare i dati sull'immigrazione (su questo script analizzeremo "immigrants by nationality",
# sullo script 2 analizziamo "immigrants_emigrants_by_sex": la distribuzione di genere tra gli immigrati,
# sullo script 3 analizziamo "immigrants_emigrants_by_age": la distribuzione degli immigrati per fascia di età.
# Analisi 1: Distribuzione temporale dell'immigrazione negli anni;
# Analisi 2: Quali sono le nazionalità più comuni tra gli immigrati?
# Analisi 2.1: Confronto dei flussi migratori per anno;
# Analisi 3: Quali distretti hanno ricevuto il maggior numero di immigrati?

import pandas as pd
import matplotlib.pyplot as plt
import numpy as nb
import seaborn as sns

# Carico il dataset 
file_name = 'immigrants_by_nationality.csv'
df = pd.read_csv(file_name)
print(df)

#########################

###### Analisi 1: Distribuzione temporale dell'immigrazione negli anni (grafico a barre orizzontali)

# Creiamo una figura per il grafico di dimensioni 10x4 pollici
plt.figure(figsize=(10, 4))

# Raggruppiamo il dataset per anno e calcoliamo la somma del numero di immigrati per ogni anno
Distribuzione_Immigrazione = df.groupby('Year')['Number'].sum()

# Creiamo un grafico a barre orizzontali
Distribuzione_Immigrazione.plot(kind= 'barh', color='green')

# Aggiungiamo titolo, etichette 
plt.title('Distribuzione Temporale Immigrazione Negli Anni')
plt.xlabel('Numero di Immigrati')
plt.ylabel('Anno')

plt.show()                                                  

##########################

###### Analisi 2: Quali sono le nazionalità più comuni tra gli immigrati? (grafico a dispersione )
# Creiamo una figura per il grafico di dimensioni 10x5 pollici
plt.figure(figsize=(10, 5))

# Creiamo un grafico a dispersione utilizzando Seaborn (limito a 10 perchè il grafico diventa confusionario)
sns.scatterplot(x='Nationality', y='Number', hue='Number', data=df.groupby('Nationality')['Number'].sum().nlargest(10).reset_index(),
                size='Number', sizes=(50, 500), alpha=0.8, palette='viridis')

# Aggiungiamo titolo, etichette
plt.title('Top 10 - Nazionalità di Provenienza Immigrati')
plt.xlabel('Nazionalità')
plt.ylabel('Numero di Immigrati')

plt.show()


###### Analisi 2.1: Abbiamo deciso di confrontare i flussi migratori per anno
# Flusso di immigrazione raggruppato per anno e nazionalità
flusso_immigrazione = df.groupby(["Year", "Nationality"])["Number"].sum().sort_values(ascending=False)
# Creazione della griglia di subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 15), sharex=True)
# Ciclo per disegnare i grafici per ciascun anno nei subplots
for i, anno in enumerate([2015, 2016, 2017]):
    flusso_anno = flusso_immigrazione.loc[anno].head(10)
    axs[i].bar(flusso_anno.index, flusso_anno.values, label=f'Anno {anno}', color=f'C{i}')
    axs[i].set_title(f"Flusso nell'anno {anno}")
    axs[i].set_xlabel('Nazionalità')
    axs[i].set_ylabel('Numero di Immigrati')
# Aggiungi una legenda generale
fig.legend(loc='upper right', bbox_to_anchor=(0.85, 0.9))
# Aggiungi titolo e mostra il grafico
fig.suptitle("Flusso di immigrazione per anno e nazionalità (Top 10)", fontsize=16)
plt.show()

##########################

###### Analisi 3: Quali distretti hanno ricevuto il maggior numero di immigrati?

# Creiamo una figura per il grafico di dimensioni 10x10 pollici
plt.figure(figsize=(10, 10))

# Raggruppiamo il dataset per distretto e calcoliamo la somma del numero totale di immigrati per ciascun distretto
Immigrati_per_distretto = df.groupby('District Name')['Number'].sum()

# Creiamo un grafico a torta
Immigrati_per_distretto.plot(kind='pie', autopct='%1.2f%%', colors=sns.color_palette('pastel'))

# Aggiungiamo titolo
plt.title('Distribuzione del Numero di Immigrati per Distretto')

# Mostrare solo il grafico a torta senza etichette sull'asse y
plt.ylabel('')
plt.show()


###########################