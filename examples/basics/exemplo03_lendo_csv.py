"""
Exemplo 03: Lendo Arquivos CSV

Este exemplo demonstra como importar dados de arquivos CSV usando Pandas.
"""

import pandas as pd
import os

print("=" * 60)
print("EXEMPLO 03: LENDO ARQUIVOS CSV")
print("=" * 60)

# Caminho para o arquivo CSV
csv_path = '../../datasets/funcionarios.csv'

# Verificar se o arquivo existe
if os.path.exists(csv_path):
    # 1. Lendo o arquivo CSV
    print("\n1. Lendo arquivo CSV completo:")
    df = pd.read_csv(csv_path)
    print(df)
    
    # 2. Informações sobre o DataFrame
    print("\n2. Informações sobre os dados:")
    print(f"Número de linhas: {len(df)}")
    print(f"Número de colunas: {len(df.columns)}")
    print(f"Colunas: {df.columns.tolist()}")
    
    # 3. Primeiras linhas
    print("\n3. Primeiras 5 linhas:")
    print(df.head())
    
    # 4. Estatísticas descritivas
    print("\n4. Estatísticas sobre dados numéricos:")
    print(df.describe())
    
    # 5. Informações sobre tipos de dados
    print("\n5. Tipos de dados:")
    print(df.dtypes)
    
    # 6. Informações gerais
    print("\n6. Informações gerais do DataFrame:")
    df.info()
    
    # 7. Valores únicos em uma coluna
    print("\n7. Cidades únicas:")
    print(df['Cidade'].unique())
    
    print("\n8. Departamentos únicos:")
    print(df['Departamento'].unique())
    
else:
    print("\n⚠️  Arquivo CSV não encontrado!")
    print(f"Esperado em: {os.path.abspath(csv_path)}")
    print("\nPara criar o arquivo de exemplo, execute:")
    print("Certifique-se de que o arquivo funcionarios.csv existe na pasta datasets/")

print("\n" + "=" * 60)
print("Fim do Exemplo 03")
print("=" * 60)
