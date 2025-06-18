# Análise de Churn - Telecom

Este projeto realiza um ETL (Extração, Transformação e Carregamento) para analisar a evasão de clientes (Churn) de uma empresa de telecomunicações.

## Estrutura do Projeto

```
telecom-churn-etl/
│
├── data/                # Dados brutos e tratados
├── etl/                 # Scripts de ETL
│   ├── extract.py       # Extração de dados da API
│   ├── transform.py     # Tratamento e transformação dos dados
│   └── load.py          # Carregamento dos dados (se necessário)
├── analysis/            # Scripts de análise exploratória
│   └── exploratory.py   # Análise e visualizações
├── reports/             # Relatórios e gráficos
│   └── churn_report.ipynb  # Notebook de relatório
├── requirements.txt     # Dependências do projeto
└── README.md            # Instruções do projeto
```

## Instalação

1. Clone o repositório.
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Uso

1. Execute o script de extração:
   ```
   python etl/extract.py
   ```
2. Execute o script de transformação:
   ```
   python etl/transform.py
   ```
3. Execute o script de análise exploratória:
   ```
   python analysis/exploratory.py
   ```
4. Abra o notebook de relatório:
   ```
   jupyter notebook reports/churn_report.ipynb
   ```

## Objetivo

O objetivo deste projeto é entender os fatores que influenciam a evasão de clientes (Churn) e gerar insights para reduzir a taxa de evasão.
