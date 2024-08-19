import numpy as np


# Criando um array unidimensional (vetor)
vetor = np.array([1, 2, 3, 4, 5])
print("Vetor:", vetor)

# Criando um array bidimensional (matriz)
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matriz:")
print(matriz)

# Operações aritméticas
soma = vetor + 10  # Adiciona 10 a cada elemento do vetor
multiplicacao = matriz * 2  # Multiplica cada elemento da matriz por 2

print("Vetor após soma:", soma)
print("Matriz após multiplicação:")
print(multiplicacao)

# Funções matemáticas
soma_total = np.sum(matriz)  # Soma todos os elementos da matriz
media = np.mean(vetor)  # Calcula a média dos elementos do vetor

print("Soma total dos elementos da matriz:", soma_total)
print("Média dos elementos do vetor:", media)

# Acessando elementos
elemento = vetor[2]  # Acessa o terceiro elemento do vetor
print("Terceiro elemento do vetor:", elemento)

# Fatiamento (slicing)
subvetor = vetor[1:4]  # Acessa elementos do índice 1 ao 3
print("Subvetor:", subvetor)
