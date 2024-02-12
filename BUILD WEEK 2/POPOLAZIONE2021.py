import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('popolazione_2021.csv')
# Calcola la somma della colonna "pop_res_21"
somma_popolazione_2021= df['pop_res_21'].sum()
print(f'Somma totale popolazione 2021: {somma_popolazione_2021}')
