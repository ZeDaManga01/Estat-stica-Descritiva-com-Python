import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Base de Dados\Cost_of_living_index.csv')

dfa = df.head(200)

dfb = df.tail(200)

dfc = pd.concat([dfa, dfb])

z = np.polyfit(dfc['Local Purchasing Power Index'], dfc['Groceries Index'], 1)
p = np.poly1d(z)
plt.plot(dfc['Local Purchasing Power Index'],p(dfc['Local Purchasing Power Index']),"r--")


print(df)
''''
# Gráfico de barras 
dfa.plot(kind='bar', x='City', y='Cost of Living Index', color='lightgreen', edgecolor='black')
plt.title('Cost of Living by city')
plt.xlabel('City')
plt.ylabel('Cost of Living Index')
plt.xticks(rotation=0)
plt.show()


# Histograma
df['Groceries Index'].plot(kind='hist', bins=10, edgecolor='black')
plt.title('Groceries Histogram')
plt.xlabel('Groceries Index')
plt.show()

# Boxplot
df['Restaurant Price Index'].plot(kind='box')
plt.title('Boxplot')
plt.show()

print(df[df['Restaurant Price Index'] > 129]'''

print(dfc)
# Criando o gráfico de dispersão
plt.scatter(dfc['Local Purchasing Power Index'], dfc['Groceries Index'])

# Adicionando título e rótulos aos eixos
plt.title('Relação entre Poder de compra e Consumo de mantimentos')
plt.xlabel('Poder de compra')
plt.ylabel('Consumo')



# Adicionando título e rótulos aos eixos
plt.title('Relação entre Horas de Estudo e Nota na Prova')
plt.xlabel('Horas de Estudo')
plt.ylabel('Nota na Prova')



# Mostrando o gráfico
plt.show()