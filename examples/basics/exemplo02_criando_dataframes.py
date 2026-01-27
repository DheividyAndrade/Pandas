"""
Exemplo 02: Criando DataFrames

Este exemplo mostra diferentes formas de criar DataFrames no Pandas.
DataFrame é uma estrutura de dados bidimensional (tabela) com linhas e colunas.
"""

import pandas as pd

print("=" * 60)
print("EXEMPLO 02: CRIANDO DATAFRAMES")
print("=" * 60)

# 1. Criando DataFrame a partir de um dicionário
print("\n1. DataFrame a partir de dicionário:")
dados_alunos = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
    'Idade': [20, 22, 21, 23, 20],
    'Nota': [8.5, 7.0, 9.5, 8.0, 7.5],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Brasília']
}

df_alunos = pd.DataFrame(dados_alunos)
print(df_alunos)

# 2. Criando DataFrame a partir de listas
print("\n2. DataFrame a partir de lista de listas:")
dados = [
    ['Python', 'Programação', 40],
    ['Pandas', 'Dados', 20],
    ['SQL', 'Banco de Dados', 30],
    ['Excel', 'Planilhas', 15]
]

df_cursos = pd.DataFrame(dados, 
                         columns=['Curso', 'Categoria', 'Horas'])
print(df_cursos)

# 3. Criando DataFrame com índice personalizado
print("\n3. DataFrame com índice personalizado:")
vendas = pd.DataFrame({
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor'],
    'Preço': [3500, 50, 150, 800],
    'Estoque': [15, 100, 45, 20]
}, index=['P001', 'P002', 'P003', 'P004'])
print(vendas)

# 4. Informações básicas sobre o DataFrame
print("\n4. Informações sobre o DataFrame:")
print(f"Forma (linhas, colunas): {df_alunos.shape}")
print(f"Colunas: {df_alunos.columns.tolist()}")
print(f"Tipos de dados:\n{df_alunos.dtypes}")

# 5. Primeiras e últimas linhas
print("\n5. Primeiras 3 linhas:")
print(df_alunos.head(3))

print("\n6. Últimas 2 linhas:")
print(df_alunos.tail(2))

# 6. Estatísticas descritivas
print("\n7. Estatísticas descritivas:")
print(df_alunos.describe())

print("\n" + "=" * 60)
print("Fim do Exemplo 02")
print("=" * 60)
