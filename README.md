# 🐼 Pandas - Minha Jornada de Aprendizado

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org)
[![Pandas](https://img.shields.io/badge/Pandas-Latest-green.svg)](https://pandas.pydata.org/)

Bem-vindo à minha vitrine de códigos Pandas! Este repositório documenta minha jornada de aprendizado em análise de dados com Python e Pandas.

## 📚 Sobre o Projeto

Este repositório serve como um portfólio pessoal dos meus estudos e práticas com a biblioteca Pandas, uma das ferramentas mais poderosas para análise e manipulação de dados em Python.

## 🗂️ Estrutura do Repositório

```
Pandas/
├── examples/          # Exemplos de código organizados por tópico
│   ├── basics/        # Fundamentos do Pandas
│   ├── dataframes/    # Trabalhando com DataFrames
│   ├── series/        # Trabalhando com Series
│   ├── manipulation/  # Manipulação de dados
│   ├── analysis/      # Análise de dados
│   └── visualization/ # Visualização de dados
├── notebooks/         # Jupyter Notebooks com análises completas
├── datasets/          # Conjuntos de dados para prática
└── README.md          # Este arquivo
```

## 🎯 Tópicos de Estudo

### 1. Fundamentos
- [ ] Instalação e configuração do Pandas
- [ ] Estruturas de dados: Series e DataFrames
- [ ] Importação e exportação de dados (CSV, Excel, JSON)
- [ ] Visualização básica de dados

### 2. Manipulação de Dados
- [ ] Seleção e filtragem de dados
- [ ] Ordenação de dados
- [ ] Tratamento de valores ausentes
- [ ] Adição e remoção de colunas/linhas
- [ ] Renomeação de colunas

### 3. Análise de Dados
- [ ] Estatísticas descritivas
- [ ] Agrupamento de dados (GroupBy)
- [ ] Agregações e transformações
- [ ] Merge, Join e Concatenação
- [ ] Pivot Tables

### 4. Limpeza de Dados
- [ ] Identificação e tratamento de duplicatas
- [ ] Normalização de dados
- [ ] Conversão de tipos de dados
- [ ] Tratamento de outliers

### 5. Visualização
- [ ] Gráficos básicos com Pandas
- [ ] Integração com Matplotlib
- [ ] Integração com Seaborn
- [ ] Gráficos interativos

### 6. Tópicos Avançados
- [ ] Otimização de performance
- [ ] Trabalhando com grandes datasets
- [ ] Séries temporais
- [ ] Multi-indexing
- [ ] Apply, Map e Applymap

## 🚀 Como Usar Este Repositório

### Instalação
```bash
# Clone o repositório
git clone https://github.com/DheividyAndrade/Pandas.git

# Entre no diretório
cd Pandas

# Instale as dependências
pip install -r requirements.txt
```

### Executando os Exemplos
```bash
# Execute um exemplo específico
python examples/basics/exemplo01_criando_series.py

# Ou abra os notebooks Jupyter
jupyter notebook notebooks/
```

## 📖 Recursos de Aprendizado

### Documentação Oficial
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [Pandas API Reference](https://pandas.pydata.org/docs/reference/index.html)

### Tutoriais Recomendados
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas Exercises](https://github.com/guipsamora/pandas_exercises)
- [Real Python - Pandas Tutorials](https://realpython.com/learning-paths/pandas-data-science/)

### Datasets para Prática
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
- [Data.gov](https://data.gov/)
- [Google Dataset Search](https://datasetsearch.research.google.com/)

## 🛠️ Tecnologias Utilizadas

- **Python 3.7+**
- **Pandas** - Manipulação e análise de dados
- **NumPy** - Computação numérica
- **Matplotlib** - Visualização de dados
- **Seaborn** - Visualização estatística
- **Jupyter Notebook** - Ambiente interativo

## 📝 Exemplos de Código

Aqui estão alguns exemplos rápidos do que você encontrará neste repositório:

### Criando um DataFrame
```python
import pandas as pd

# Criando um DataFrame a partir de um dicionário
data = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Idade': [25, 30, 35, 28],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília']
}

df = pd.DataFrame(data)
print(df)
```

### Análise Básica
```python
# Estatísticas descritivas
print(df.describe())

# Filtrando dados
jovens = df[df['Idade'] < 30]

# Agrupamento
df.groupby('Cidade')['Idade'].mean()
```

## 📊 Projetos e Análises

À medida que avanço nos estudos, documentarei aqui os projetos e análises realizadas:

1. **Em breve...** - Análise exploratória de dados
2. **Em breve...** - Limpeza e preparação de dados
3. **Em breve...** - Visualização de dados

## 🤝 Contribuições

Este é um repositório pessoal de aprendizado, mas sugestões e dicas são sempre bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## 📧 Contato

- GitHub: [@DheividyAndrade](https://github.com/DheividyAndrade)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

⭐ **Dica**: Marque este repositório com uma estrela se você também está aprendendo Pandas!

**Última atualização**: Janeiro 2026
