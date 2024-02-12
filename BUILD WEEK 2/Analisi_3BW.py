
 ###    TERZO SCRIPT ANALISI BUILD WEEK II    ###

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carico file csv puliti 
df_comuni = pd.read_csv('comuni_python_pulito.csv')
df_province = pd.read_csv('province_python_pulito.csv')
df_regioni = pd.read_csv('regioni_python_pulito.csv')

####  CARICAMENTO E PULIZIA NUOVO DATASET INTEGRATIVO CONTENENTE  DATI SULLA POPOLAZIONE 2020
####  UTILI AD UN'ANALISI MIGLIORE (avevamo solo dataset popolazione2011)

popolazione = pd.read_excel('Popolazione2020.xlsx',
                           skiprows=8,
                           names=["Regioni", "Maschi", "Femmine", "Totale"],
                           usecols=[0, 2, 3, 4]).iloc[:-1]
#Print(popolazione)
popolazione[['Maschi', 'Femmine', 'Totale']] = popolazione[['Maschi', 'Femmine', 'Totale']].astype(int)
print(popolazione)

##### CALCOLO IL TOTALE DELLA POPOLAZIONE IN ITALIA DIVISA PER SESSO
totale_popolazione = popolazione["Totale"].sum()
totale_maschi = popolazione["Maschi"].sum()
totale_femmine = popolazione["Femmine"].sum()
print("Il totale della popolazione italiana all'inizio del 2020 è: ", totale_popolazione)
print("Il totale della popolazione italiana maschile è: ", totale_maschi)
print("Il totale della popolazione italiana femminile è: ", totale_femmine)
# Creazione di un grafico a torta
plt.figure(figsize=(8, 8))
sizes = [totale_maschi, totale_femmine]
labels = ['Maschi', 'Femmine']
colors = ['lightblue', 'pink']
explode = (0.1, 0)  # Esplosione della fetta 'Maschi'
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Totale della popolazione italiana per sesso (2020)', fontsize=16)
plt.axis('equal')  # Equalizza gli assi per rendere il grafico a torta circolare
total_text = f'Totale \n popolazione: \n {totale_popolazione}'
plt.figtext(0.9, 0.5, total_text, ha='center', va='center', fontsize=12, color='black')
plt.show() 


####### 11. Calcolo variazione popolazione da inizio 2020 a fine 2020 a causa delle morti per Covid
totale_popolazione = popolazione["Totale"].sum()
# Filtra il DataFrame regioni per la data '2020-12-06'
df_regioni['Date'] = pd.to_datetime(df_regioni['Date'])
totale_morti_regione_date = df_regioni[df_regioni['Date'] == '2020-12-06']
totale_morti = totale_morti_regione_date['Deaths'].sum()
# Calcola la differenza tra la popolazione totale all'inizio del 2020 e il totale dei morti per COVID-19
variazione_popol_causa_morti = totale_popolazione - totale_morti
# Crea un dizionario con i dati per il grafico a barre
data = {'Popolazione inizio 2020': totale_popolazione, 'Popolazione a causa delle morti': variazione_popol_causa_morti}
# Creazione di un grafico a barre
plt.figure(figsize=(10, 6))
bars = plt.bar(data.keys(), data.values(), color=['lightblue', 'lightcoral'])
plt.title('Variazione della popolazione a causa delle morti per COVID-19 nel 2020', fontsize=16)
plt.ylabel('Popolazione italiana')
# Aggiungi il valore numerico all'interno delle barre
for bar in bars:
   height = bar.get_height()
   plt.text(bar.get_x() + bar.get_width() / 2, height, str(int(height)), ha='center', va='bottom', fontweight='bold')
tasso_mortalita = (totale_morti / totale_popolazione) * 100
total_text = f'Tasso di mortalità: {tasso_mortalita:.2f}%'
plt.figtext(0.7, 0.5, total_text, ha='center', va='center', fontsize=10, color='red')
plt.show()


###### 12. Calcolo variazione popolazione divisa per regione da inizio 2020 a fine 2020 a causa delle morti per Covid
# Rimuovo spazi aggiuntivi nei nomi delle regioni
popolazione['Regioni'] = popolazione['Regioni'].str.strip()
# Sostituisco i nomi di alcune regioni della colonna Regioni nel file popolazione per renderlo più pulito
popolazione['Regioni'] = popolazione['Regioni'].replace({'Trentino Alto Adige / Südtirol': 'Trentino Alto Adige',
                                                        "Valle d'Aosta / Vallée d'Aoste": "Valle d'Aosta",
                                                        'Friuli-Venezia Giulia': 'Friuli Venezia Giulia'})
# Sostituisco i nomi di alcune regioni della colonna Regioni nel file regioni per rendere più pulito
df_regioni['RegionName'] = df_regioni['RegionName'].replace({'P.A. Bolzano': 'Trentino Alto Adige',
                                                      "P.A. Trento": "Trentino Alto Adige"})
# Filtro per la data '2020-12-06' ultima
df_regioni['Date'] = pd.to_datetime(df_regioni['Date'])
totale_morti_regione_date = df_regioni[df_regioni['Date'] == '2020-12-06']

data = {'Regioni': [], 'Popolazione inizio 2020': [], 'Popolazione a causa delle morti': []}
for idx, reg in popolazione.iterrows():
   regione = reg['Regioni']
   tot_popol_regione = reg['Totale']
   # Totale dei morti per la regione corrispondente alla data specifica
   tot_morti_regione = totale_morti_regione_date[totale_morti_regione_date['RegionName'] == regione.strip()]['Deaths'].values[0]
   data['Regioni'].append(regione)
   data['Popolazione inizio 2020'].append(tot_popol_regione)
   data['Popolazione a causa delle morti'].append(tot_popol_regione - tot_morti_regione)
#Creo dataframe
df_data = pd.DataFrame(data)
# Grafico a barre per ogni regione con la variazione percentuale
plt.figure(figsize=(14, 8))
bar_width = 0.35
bar1 = plt.bar(df_data.index, df_data['Popolazione inizio 2020'], width=bar_width, label='Popolazione inizio 2020', color='lightblue')
bar2 = plt.bar(df_data.index + bar_width, df_data['Popolazione a causa delle morti'], width=bar_width, label='Popolazione a causa delle morti', color='lightcoral')
# Aggiungo la variazione percentuale come testo nel grafico
for i, (pop_inizio, pop_morti) in enumerate(zip(df_data['Popolazione inizio 2020'], df_data['Popolazione a causa delle morti'])):
   plt.text(i + bar_width / 2, max(pop_inizio, pop_morti) + 10, f'{((pop_morti - pop_inizio) / pop_inizio) * 100:.2f}%', ha='center', va='center', fontsize=10, color='black')
plt.title('Variazione della popolazione a causa delle morti per COVID-19 per ogni regione', fontsize=16)
plt.xlabel('Regioni')
plt.ylabel('Variazione della popolazione')
plt.xticks(df_data.index + bar_width/2, df_data['Regioni'], rotation=45, ha='right', rotation_mode='anchor')  # Posiziona le etichette sull'asse x
plt.legend()
plt.tight_layout() 
plt.show()
