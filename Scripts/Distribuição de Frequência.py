import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



# Dados numéricos
dados = pd.Series([1, 7, 5, 6, 9, 2, 3, 8, 4, 7, 6, 5, 3, 2, 7, 6])

# Definindo os intervalos
bins = [0, 3, 6, 9]

# Criando a distribuição de frequência
categorias = pd.cut(dados, bins)
frequencia = categorias.value_counts()
print(frequencia)

frequencia.plot(kind='bar')
plt.show()

dados = {
    'Produto': ['A', 'B', 'C'],
    'Preço': [10.5, 20.7, 30.2],
    'Quantidade': [5, 3, 8]
}

df = pd.DataFrame(dados)
print("DataFrame:")
print(df)
print("\n")

# Distribuição de Frequência
dados = pd.read_csv('Base de Dados\Cost_of_living_index.csv')

df = pd.DataFrame(dados)
df['Groceries Index'].plot(kind='hist', bins=8, edgecolor='black')
plt.title('Frequencia')
plt.show()



