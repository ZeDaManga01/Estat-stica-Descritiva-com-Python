import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = 0

while a < 10: #Enquanto 'a' for menor que 10

    print("a = {}".format(a)) #Imprima o valor de 'a'
    
    a += 1 #Some 1 ao valor de 'a'

b = 0

for b in range(0,10): #Para cada valor de 'b' no intervalo de 0 a 9 

    print(("b = {}".format(b))) #Imprima o valor de 'b'

    b += 1  #Some 1 ao valor de 'b'

    #Nome da função
def soma(a,b):     

    resultado = a + b

    return resultado

resultado_soma = soma(3, 9)
print("{}".format(resultado_soma))

def nome_da_funcao(parametroA, parametroB):

    # Bloco de código que executa a função
    resultado = parametroA + parametroB
    return resultado

if a == 1:
    a = 2


#=======================

# Listas
lista = [1, 2, 3, 4, 5]
print(lista)

# Vetores com NumPy

vetor = np.array([1, 2, 3, 4, 5])
print(vetor)

# DataFrames com Pandas

df = pd.DataFrame({'Nomes': ['Ana', 'Bruno', 'Carlos'], 'Idade': [23, 34, 45]})
print(df)

#=======================


# Introdução ao NumPy
vetor = np.array([1, 2, 3, 4, 5])
print("Vetor NumPy:", vetor)

# Introdução ao Pandas
df = pd.DataFrame({
    'Produto': ['A', 'B', 'C'],
    'Preço': [10.5, 20.7, 30.2]
})
print("DataFrame Pandas:")
print(df)

######################


# Criando um array unidimensional (vetor)
vetor = np.array([1, 2, 3, 4, 5])
print("Vetor:", vetor)

# Criando um array bidimensional (matriz)
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matriz:")
print(matriz)




# Criando um DataFrame a partir de um dicionário
dados = {
    'Produto': ['A', 'B', 'C'],
    'Preço': [10.5, 20.7, 30.2],
    'Quantidade': [5, 3, 8]
}

df = pd.DataFrame(dados)
print("DataFrame:")
print(df)


# Gráfico de Barras
df['Preço'].value_counts().plot(kind='bar')
plt.title('Gráfico de Barras')
plt.show()

# Histograma
df['Preço'].plot(kind='hist', bins=10, edgecolor='black')
plt.title('Histograma')
plt.show()

# Boxplot
df['Quantidade'].plot(kind='box')
plt.title('Boxplot')
plt.show()
