import pandas as pd
import matplotlib.pyplot as plt

file_name = "./stockdata.csv"
data = pd.read_csv(file_name,usecols=["AAPL"])

plt.plot(data.head(20), color='r', linestyle='--', marker="o", markerfacecolor="black", linewidth="2")
plt.xlabel("Valore")
plt.ylabel("Data")
plt.title("Azioni Apple")
plt.show()


data2= pd.read_csv(file_name)
x , y = data2["Date"].head(20), data2["IBM"].head(20)
x1 , y1= data2["Date"].head(20), data2["SBUX"].head(20)
x2 , y2 = data2["Date"].head(20), data2["MSFT"].head(20)
x3 , y3 = data2["Date"].head(20), data2["AAPL"].head(20)
x4 , y4 = data2["Date"].head(20), data2["GSPC"].head(20)
plt.plot