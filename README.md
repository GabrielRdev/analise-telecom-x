# Análise de Evasão de Clientes (Churn) em Telecom

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-blue?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter&logoColor=white)

## 1. Visão Geral do Projeto

Este repositório contém uma análise de dados completa sobre a evasão de clientes (Churn) em uma empresa fictícia de telecomunicações. O objetivo principal é identificar os fatores que mais contribuem para o cancelamento de serviços, permitindo que a empresa desenvolva estratégias de retenção mais eficazes e direcionadas.

O projeto abrange desde a extração de dados brutos de uma API, passando por um rigoroso processo de limpeza e transformação, até a análise exploratória detalhada para a geração de insights acionáveis.

## 2. O Problema de Negócio

A taxa de Churn é uma métrica vital para empresas de serviços por assinatura. Um alto índice de evasão impacta diretamente a receita e aumenta os custos, já que adquirir um novo cliente é consideravelmente mais caro do que manter um existente. Compreender os motivos que levam um cliente a sair é o primeiro passo para criar ações proativas que aumentem a lealdade e o valor do ciclo de vida do cliente (LTV).

## 3. Estrutura de Pastas

O projeto está organizado da seguinte forma para garantir clareza e reprodutibilidade:

```
├── data/
│   ├── raw/                # Dados brutos extraídos da API
│   │   ├── TelecomX_Raw_Data.json
│   │   └── TelecomX_Raw_Data.csv
│   └── processed/          # Armazena os dados limpos e prontos para análise
│       └── TelecomX-processed.csv
├── notebooks/
│   ├── 01-transform-load-telecomx.ipynb  # Notebook para extração e limpeza dos dados
│   └── 02-analise-telecomx.ipynb   # Notebook para análise e visualização dos dados
├── reports/                # Contém os relatórios e apresentações finais
│   └── relatorio.ipynb
├── .gitignore
├── README.md               # Documentação do projeto
└── requirements.txt
```

## 4. Processo de ELT (Extract, Load, Transform)

O fluxo de dados do projeto segue um modelo ELT, onde os dados são primeiro extraídos e carregados em um formato bruto e, em seguida, transformados para a análise. O diagrama abaixo ilustra o processo:

```mermaid
graph TD;
    subgraph "1. Extração e Carga (Bruto)";
        |Executa extração| B(Api Externa) --> A[notebooks/01-transform-load-telecomx.ipynb] ;
        A -->|Salva dados brutos| C[data/raw/TelecomX_Raw_Data.json];
    end

    subgraph "2. Transformação";
        C -->|Lê dados brutos| A;
        A -->|Aplica limpeza e normalização| D[notebooks/01-transform-load-telecomx.ipynb];
    end

    subgraph "3. Carga (Processado) e Análise";
        D -->|Salva dados processados| E[processed/TelecomX-processed.csv];
        E --> F(notebooks/02-analise-telecomx.ipynb);
        F -->|Lê dados, analisa, faz gráficos e gera um relatório| G[reports/relatorio.ipynb];
    end
```

**Etapas da Transformação:**

1.  **Normalização:** Expansão de colunas com dados aninhados (JSON).
2.  **Tratamento de Nulos:** Preenchimento de valores ausentes na coluna `Contas_Totais`.
3.  **Correção de Tipos:** Conversão de colunas para tipos numéricos e categóricos adequados.
4.  **Codificação:** Transformação de variáveis categóricas binárias (ex: 'Yes'/'No') em `1`/`0`.
5.  **Renomeação:** Padronização dos nomes das colunas para o português.
6.  **Engenharia de Features:** Criação da coluna `Contas_Diarias` para novas perspectivas de análise.

## 5. Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Bibliotecas de Análise:** Pandas, NumPy
- **Bibliotecas de Visualização:** Matplotlib, Seaborn
- **Ambiente de Desenvolvimento:** VSCode

## 6. Principais Insights da Análise

A análise exploratória revelou padrões claros no comportamento dos clientes que evadem:

- **Tipo de Contrato:** Clientes com **contrato mensal** possuem uma taxa de churn drasticamente maior em comparação com contratos de 1 ou 2 anos.
- **Tempo de Contrato:** A evasão é muito mais comum nos **primeiros meses** de serviço. A retenção aumenta significativamente com o tempo de permanência do cliente.
- **Forma de Pagamento:** O pagamento via **boleto eletrônico** está associado a uma maior taxa de churn.
- **Serviços Adicionais:** Clientes que **não contratam serviços de segurança** (como `Seguranca_Online` e `Backup_Online`) tendem a evadir mais.

## 7. Recomendações Estratégicas

Com base nos insights, as seguintes ações são recomendadas:

1.  **Incentivar Contratos de Longo Prazo:** Criar ofertas e benefícios para migrar clientes do plano mensal para planos anuais.
2.  **Melhorar o Onboarding:** Implementar um programa de acompanhamento nos primeiros meses para garantir a satisfação e o engajamento do novo cliente.
3.  **Promover Pacotes de Serviços:** Oferecer pacotes com serviços de segurança e suporte para aumentar o valor percebido e a "aderência" do cliente.
4.  **Otimizar Formas de Pagamento:** Incentivar a adesão ao débito automático ou cartão de crédito, oferecendo pequenos descontos.

## 8. Como Executar o Projeto

Siga os passos abaixo para configurar e executar a análise em seu ambiente local.

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/GabrielRdev/analise-telecom-x.git
    cd analise-telecom-x
    ```

2.  **Crie e ative um ambiente virtual:**

    ```bash
    # Windows
    python -m venv .venv
    .\.venv\Scripts\activate

    # Linux / macOS
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute os notebooks:**
    Inicie o Jupyter Notebook e execute os arquivos na ordem numérica:
    - `01-transform-load-telecomx.ipynb`
    - `02-analise-telecomx.ipynb`

## 9. Autor

- **Gabriel Ricardo** - GitHub
