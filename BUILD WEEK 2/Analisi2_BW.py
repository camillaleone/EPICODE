
 ###    SECONDO SCRIPT ANALISI BUILD WEEK II    ###

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Leggi i file CSV
df_comuni = pd.read_csv('comuni_python_pulito.csv')
df_province = pd.read_csv('province_python_pulito.csv')
df_regioni = pd.read_csv('regioni_python_pulito.csv')

##### 6. Le prime 15 province con più positivi
province_cases = df_province.groupby('ProvinceName')['TotalPositiveCases'].sum()
# Ordino le regioni in base al numero totale di casi positivi in ordine decrescente
province_cases_sorted = province_cases.sort_values(ascending=False)
# Seleziono le prime 15 regioni con il numero più alto di casi positivi
top_15_province = province_cases_sorted.head(15)
top_15_province.to_csv('top_15_province_casi_positivi.csv', index=False)
# Grafico corrispondente
plt.figure(figsize=(10, 6))
top_15_province.plot(kind='bar', color='skyblue')
plt.title('Top 15 Province con il numero più alto di casi positivi')
plt.xlabel('Province')
plt.ylabel('Totale casi positivi')
plt.xticks(rotation=90)  
plt.tight_layout()
plt.show()


###### 7. Variazione dei nuovi casi per la regione Lombardia
df_regioni = df_regioni[df_regioni['RegionName'] == 'Lombardia']
df_regioni['Date'] = pd.to_datetime(df_regioni['Date'])
weekly_new_cases = df_regioni.groupby(pd.Grouper(key='Date', freq='W-Mon'))['NewPositiveCases'].sum().reset_index()
# Grafico corrispondente
plt.figure(figsize=(12, 8))
plt.plot(weekly_new_cases['Date'], weekly_new_cases['NewPositiveCases'], marker='o', markersize=5, color='blue', label='Nuovi casi settimanali')
plt.title('Variazioni Settimanali dei Nuovi Casi nella Regione Lombardia')
plt.xlabel('Data')
plt.ylabel('Nuovi casi')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
# Aggiungo annotazione della data con il picco massimo di nuovi casi
peak_date = weekly_new_cases.loc[weekly_new_cases['NewPositiveCases'].idxmax(), 'Date']
peak_cases = weekly_new_cases['NewPositiveCases'].max()
plt.annotate(f'Picco: {peak_cases} casi\n{peak_date.strftime("%d-%m-%Y")}',
             xy=(peak_date, peak_cases), xytext=(peak_date, peak_cases + 100),
             arrowprops=dict(facecolor='red', arrowstyle='->'),
             fontsize=10, color='red')
plt.show()


###### 8. Analizziamo la somma dei nuovi casi per ogni provincia della Lombardia
# Filtro i dati solo per la regione Lombardia e rimuovo le province indesiderate 
desired_provinces = ['Bergamo', 'Brescia', 'Como', 'Cremona', 'Lecco', 'Lodi', 'Mantova', 
                     'Milano', 'Monza e della Brianza', 'Pavia', 'Sondrio', 'Varese']
lombardia_data_filtered = df_province[df_province['ProvinceName'].isin(desired_provinces)]

lombardia_data_filtered['Date'] = pd.to_datetime(lombardia_data_filtered['Date'])
# Raggruppo i dati per provincia e settimana, calcolando la somma dei nuovi casi per ogni settimana
weekly_new_cases_by_province = lombardia_data_filtered.groupby(['ProvinceName', pd.Grouper(key='Date', freq='W-Mon')])['TotalPositiveCases'].sum().reset_index()
# Grafico corrispondente per visualizzare le variazioni settimanali dei nuovi casi per ogni provincia
plt.figure(figsize=(12, 8))
for province, data in weekly_new_cases_by_province.groupby('ProvinceName'):
    plt.plot(data['Date'], data['TotalPositiveCases'], label=province, marker='o', markersize=5)
plt.legend()
plt.title('Variazioni settimanali dei nuovi casi per provincia nella regione Lombardia')
plt.xlabel('Settimana')
plt.ylabel('Nuovi casi')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


###### 9. Percentuale totale di morti rispetto ai casi positivi
# Filtro il DataFrame per la data '2020-12-06'
df_regioni['Date'] = pd.to_datetime(df_regioni['Date'])
df_selected_date = df_regioni[df_regioni['Date'] == '2020-12-06']
# Calcol la percentuale totale di morti rispetto ai casi positivi per la data selezionata
total_death_percentage = (df_selected_date['Deaths'].sum() / df_selected_date['TotalPositiveCases'].sum()) * 100
# Creo un DataFrame con i valori per il grafico a torta
data = {'Morti': total_death_percentage, 'Guariti': 100 - total_death_percentage}
df = pd.DataFrame(data, index=['Percentuale'])
# Grafico a torta corrispondente
plt.figure(figsize=(8, 8))
colors = ['lightcoral', 'lightgreen']
explode = (0.3, 0) 
plt.pie(df.iloc[0], labels=df.columns, autopct='%1.1f%%', colors=colors, explode=explode, shadow=True, startangle=140)
plt.title('Percentuale totale di morti rispetto al totale dei casi positivi', fontsize=16)
plt.axis('equal')  
plt.show()
 

###### 10. Correlazione tra variabili nel tempo
data_for_correlation = df_regioni[['TestsPerformed', 'NewPositiveCases', 'HospitalizedPatients', 'Recovered', 'Deaths']]
# Calcolo la matrice di correlazione
correlation_matrix = data_for_correlation.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f",
            xticklabels=['Test effettuati', 'Nuovi casi positivi', 'Pazienti ospedalizzati', 'Guariti', 'Decessi'], 
            yticklabels=['Test effettuati', 'Nuovi casi positivi', 'Pazienti ospedalizzati', 'Guariti', 'Decessi'])
plt.title('Correlazione tra Variabili nel Tempo')
plt.show()

