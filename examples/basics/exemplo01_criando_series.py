"""
Exemplo 01: Criando e Manipulando Series

Este exemplo demonstra como criar e trabalhar com Series no Pandas.
Series é uma estrutura de dados unidimensional que pode armazenar qualquer tipo de dado.
"""

import pandas as pd

print("=" * 60)
print("EXEMPLO 01: CRIANDO E MANIPULANDO SERIES")
print("=" * 60)

# 1. Criando uma Series a partir de uma lista
print("\n1. Criando Series a partir de uma lista:")
numeros = pd.Series([10, 20, 30, 40, 50])
print(numeros)

# 2. Criando uma Series com índices personalizados
print("\n2. Series com índices personalizados:")
notas = pd.Series([8.5, 9.0, 7.5, 10.0], 
                  index=['Matemática', 'Física', 'Química', 'Biologia'])
print(notas)

# 3. Criando uma Series a partir de um dicionário
print("\n3. Series a partir de um dicionário:")
populacao = pd.Series({
    'São Paulo': 12400000,
    'Rio de Janeiro': 6748000,
    'Brasília': 3094000,
    'Salvador': 2900000
})
print(populacao)

# 4. Acessando elementos
print("\n4. Acessando elementos:")
print(f"População de São Paulo: {populacao['São Paulo']}")
print(f"Nota em Física: {notas['Física']}")

# 5. Operações com Series
print("\n5. Operações matemáticas:")
print("Notas + 1 ponto extra:")
print(notas + 1)

print("\n6. Estatísticas básicas:")
print(f"Média das notas: {notas.mean():.2f}")
print(f"Maior nota: {notas.max()}")
print(f"Menor nota: {notas.min()}")

# 7. Filtragem de dados
print("\n7. Filtrando notas acima de 8.0:")
print(notas[notas > 8.0])

print("\n" + "=" * 60)
print("Fim do Exemplo 01")
print("=" * 60)
