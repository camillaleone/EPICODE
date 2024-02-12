                                
 ###    PRIMO SCRIPT ANALISI BUILD WEEK II    ###

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carico i file CSV puliti
df_comuni = pd.read_csv('comuni_python_pulito.csv')
df_province = pd.read_csv('province_python_pulito.csv')
df_regioni = pd.read_csv('regioni_python_pulito.csv')

# Describe sommario generale 
summary_stats = df_regioni.describe()
print(summary_stats)
#####

######
#                                                  # INIZIO ANALISI #

###### 1. Guariti e Deceduti per ogni regione:
df_regioni['Date'] = pd.to_datetime(df_regioni['Date'])
df_selected_date = df_regioni[df_regioni['Date'] == '2020-12-06']
# Raggruppamento per regione e calcolo totale decessi e guariti
group_by_region = df_selected_date.groupby("RegionName").agg({"Deaths":"sum", "Recovered":"sum"}).reset_index()
# Ordino in modo decrescente 
group_by_region = group_by_region.sort_values(by='Deaths', ascending=False)
print(group_by_region[["RegionName","Deaths","Recovered"]])
# Grafico a barre corrispondente 
plt.figure(figsize=(10, 8)) 
bar_height = 0.35
index = range(len(group_by_region['RegionName']))
bars1 = plt.barh(index, group_by_region['Deaths'], bar_height, label='Morti', color='lightcoral')
bars2 = plt.barh([i + bar_height for i in index], group_by_region['Recovered'], bar_height, label='Guariti', color='lightgreen')
plt.title('Totale Guariti e Deceduti per ogni Regione')
# Invertito l'ordine degli elementi sull'asse y
plt.gca().invert_yaxis()
plt.yticks([i + bar_height / 2 for i in index], group_by_region['RegionName'])
plt.legend(loc='lower right')
plt.show()


###### 2. Del totale dei casi positivi, vogliamo vedere quanti pazienti ospedalizzati, in terapia intensiva e in isolamento
df_regioni['Date'] = pd.to_datetime(df_regioni['Date'])
df_selected_date = df_regioni[df_regioni['Date'] == '2020-12-06']
df_selected = df_selected_date[['HospitalizedPatients','IntensiveCarePatients','HomeConfinement']]
totals = df_selected.sum()
print(totals)
# Grafico a torta corrispondente
labels = ['Ricoverati', 'Terapia Intensiva', 'Isolamento Domiciliare']
sizes = totals.values
colors = ['lightblue', 'lightcoral', 'lightgreen']
explode = (0.4, 0.6, 0) 
plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, shadow=True)
plt.axis('equal')  
plt.title('Distribuzione dei Casi COVID-19')
plt.show()


###### 3. Assegnazione dei casi positivi totali a ciascun tipo di terapia
df_regioni['Date'] = pd.to_datetime(df_regioni['Date'])
df_regioni.set_index('Date', inplace=True)
# Sommo ogni colonna interessata 
OspedalizzatiTotITA = df_regioni["HospitalizedPatients"].sum()
TerapiaIntensivaTotITA = df_regioni["IntensiveCarePatients"].sum()
ConfinatiACasaTotITA =df_regioni["HomeConfinement"].sum()
# Media x ogni trimestre 
OspedalizzatiStagionaliITA = df_regioni.resample("Q")["HospitalizedPatients"].mean()
TerapiaIntensivaStagionaliITA = df_regioni.resample("Q")["IntensiveCarePatients"].mean()
ConfinatiACasaStagionaliITA = df_regioni.resample("Q")["HomeConfinement"].mean()
PazientiPositivi = pd.DataFrame({
    'Ospedalizzati': [OspedalizzatiTotITA],
    'TerapiaIntensiva': [TerapiaIntensivaTotITA],
    'Isolamento domiciliare': [ConfinatiACasaTotITA]
}, index=['Total'])
PazientiPositiviStagionali = pd.DataFrame({
    'Ospedalizzati': OspedalizzatiStagionaliITA,
    'Terapia Intensiva': TerapiaIntensivaStagionaliITA,
    'Isolamento domiciliare': ConfinatiACasaStagionaliITA
})
# Grafico a torta corrispondente
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2,figsize=(12, 10))
fig.suptitle('Distribuzione Stagionale dei Casi COVID-19', fontsize=16, fontweight='bold')
def annotate_pie(ax, labels, sizes):
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, explode = (0.1, 0.1, 0.1),  
           colors=['lightblue', 'lightcoral', 'lightgreen'])
    explode = (0.4, 0.6, 0) 
annotate_pie(ax1, PazientiPositiviStagionali.columns, PazientiPositiviStagionali.iloc[0])
ax1.set_title('Trimestre Invernale')
annotate_pie(ax2, PazientiPositiviStagionali.columns, PazientiPositiviStagionali.iloc[1])
ax2.set_title('Trimestre Primaverile')
annotate_pie(ax3, PazientiPositiviStagionali.columns, PazientiPositiviStagionali.iloc[2])
ax3.set_title('Trimestre Estivo')
annotate_pie(ax4, PazientiPositiviStagionali.columns, PazientiPositiviStagionali.iloc[3])
ax4.set_title('Trimestre Autunnale')
fig.legend(labels=PazientiPositiviStagionali.columns, loc='upper right')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()


###### 4. Andamento dei nuovi casi positivi mensilmente
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
df_regioni.groupby('Date')['NewPositiveCases'].sum().plot(marker='.', linestyle='-', color='red', label='Nuovi Casi Positivi')
plt.title('Andamento dei Nuovi Casi Positivi', fontsize=16)
plt.xlabel('Data', fontsize=12)
plt.ylabel('Nuovi Casi Positivi', fontsize=12)
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


###### 5. Calcolo del tasso di guarigione e tasso di mortalità nel tempo
# Tasso di guarigione nel tempo
df_regioni['RecoveryRate'] = df_regioni['Recovered'] / df_regioni['TotalPositiveCases']
recovery_rate = df_regioni.groupby('Date')['RecoveryRate'].mean()
# Tasso di mortalità nel tempo
df_regioni['MortalityRate'] = df_regioni['Deaths'] / df_regioni['TotalPositiveCases']
mortality_rate = df_regioni.groupby('Date')['MortalityRate'].mean()
# Grafico corrispondente
plt.figure(figsize=(10, 6))
plt.bar(recovery_rate.index, recovery_rate, label='Tasso di guarigione', color='lightgreen')
plt.bar(mortality_rate.index, mortality_rate, label='Tasso di mortalità', color='salmon')
plt.title('Tasso di guarigione e tasso di mortalità nel tempo')
plt.xlabel('Data')
plt.ylabel('Tasso')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()