import pandas as pd

# Criando uma Series
serie = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print("Series:")
print(serie)
print("\n")

# Criando um DataFrame a partir de um dicionário
dados = {
    'Produto': ['A', 'B', 'C'],
    'Preço': [10.5, 20.7, 30.2],
    'Quantidade': [5, 3, 8]
}

df = pd.DataFrame(dados)
print("DataFrame:")
print(df)
print("\n")


# Selecionando uma coluna
precos = df['Preço']
print("Preços:")
print(precos)
print("\n")


# Selecionando múltiplas colunas
produtos_precos = df[['Produto', 'Preço']]
print("Produtos e Preços:")
print(produtos_precos)
print("\n")

# Seleção de linhas por rótulo
linha = df.loc[1]  # Seleciona a segunda linha
print("Segunda linha do DataFrame:")
print(linha)
print("\n")

# Seleção de linhas por índice
linha_idx = df.iloc[2]  # Seleciona a terceira linha
print("Terceira linha do DataFrame:")
print(linha_idx)
print("\n")

# Filtrando linhas com base em uma condição
produtos_caros = df[df['Preço'] > 15]
print("Produtos com preço maior que 15:")
print(produtos_caros)
print("\n")

# Soma total das quantidades
quantidade_total = df['Quantidade'].sum()
print("Quantidade total de produtos:", quantidade_total)
print("\n")

# Média dos preços
media_precos = df['Preço'].mean()
print("Média dos preços:", media_precos)
print("\n")