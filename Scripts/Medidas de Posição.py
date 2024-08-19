import pandas as pd

# Conjunto de dados
dados = pd.Series([10, 20, 30, 40, 50])

# Calculando a média
media = dados.mean()
print("Média:", media)

#################################

# Conjunto de dados
dados = pd.Series([10, 20, 30, 40, 50])

# Calculando a mediana
mediana = dados.median()
print("Mediana:", mediana)


#################################

# Conjunto de dados
dados = pd.Series([10, 20, 20, 30, 40, 50])

# Calculando a moda
moda = dados.mode()
print("Moda:", moda)
