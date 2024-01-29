# Dopo le analisi sull'immigrazione, ci spostiamo sull'analisi della disoccupazione. 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as nb
import seaborn as sns

file_name = "unemployment.csv"
df = pd.read_csv(file_name)

# Analisi 1: Analisi della domanda di occupazione per i vari distretti
distretti_demand = df.groupby(['District Code', 'District Name'])['Number'].sum().reset_index()
distretti_demand.plot(x='District Name', y='Number', kind='bar', legend=False)
plt.title('Domanda di occupazione per distretti')
plt.xlabel('Distretto')
plt.ylabel('Numero di richieste di occupazione')
plt.yticks([])
plt.show()

# Analisi 2: Analisi della domanda di lavoro per genere
genere_demand = df.groupby('Gender')['Number'].sum().reset_index()

# Grafico a torta
plt.pie(genere_demand['Number'], labels=genere_demand['Gender'], autopct='%1.1f%%', startangle=90)
plt.title('Domanda di lavoro per genere')
plt.show()
