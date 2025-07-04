# Relatório Final: Análise de Evasão de Clientes (Churn) em uma Empresa de Telecomunicações

## 1. Introdução

### Objetivo da Análise

O presente projeto tem como principal objetivo realizar uma análise exploratória sobre um conjunto de dados de uma empresa de telecomunicações. O foco é identificar os principais fatores que influenciam a decisão de um cliente em cancelar seu contrato, fenômeno conhecido como **Churn** (evasão). Ao compreender os padrões e perfis dos clientes que evadem, a empresa pode desenvolver estratégias mais eficazes para a retenção, aumentando a satisfação e a lucratividade.

### O Problema do Churn

A evasão de clientes é uma das métricas mais críticas para negócios baseados em assinatura, como os de telecomunicações. Adquirir um novo cliente pode custar significativamente mais do que reter um existente. Portanto, entender as causas do churn não é apenas uma questão de análise de dados, mas uma necessidade estratégica para a sustentabilidade e o crescimento do negócio. Esta análise busca fornecer insights para ajudar a reduzir essa taxa de evasão.

## 2. Limpeza e Tratamento de Dados

Para garantir a qualidade e a consistência da análise, os dados brutos passaram por um processo de extração, limpeza e transformação. As seguintes etapas foram executadas:

1.  **Extração dos Dados**: Os dados foram inicialmente extraídos de uma API e carregados em um DataFrame do Pandas.
2.  **Normalização de Colunas**: Colunas que continham dados aninhados (estruturas JSON dentro de células) foram desmembradas, criando novas colunas e tornando a informação acessível.
3.  **Tratamento de Valores Ausentes**: Foi identificado que a coluna `Contas_Totais` possuia valores ausentes para clientes novos (com 0 meses de contrato). Esses valores foram substituídos por `0`, refletindo a realidade de que ainda não houve cobrança total.
4.  **Correção de Tipos de Dados**: As colunas foram convertidas para os tipos de dados apropriados (numérico, categórico, etc.) para permitir cálculos e visualizações corretas. Por exemplo, `Contas_Totais` foi convertida para o tipo numérico após o tratamento de valores ausentes.
5.  **Codificação de Variáveis Binárias**: Colunas com respostas "Yes" e "No" (como `Evasao`, `Parceiro`, `Dependentes`, `Servico_Telefone`) foram convertidas para o formato binário `1` e `0`, respectivamente. Isso facilita a análise quantitativa e a aplicação de modelos de machine learning no futuro.
6.  **Renomeação de Colunas**: Para facilitar a compreensão e a apresentação dos resultados, todas as colunas foram renomeadas para o português (ex: `Churn` para `Evasao`, `tenure` para `Meses_Contrato`).
7.  **Engenharia de Features**: Foi criada a coluna `Contas_Diarias` a partir da divisão de `Contas_Totais` por `Meses_Contrato` (considerando 30 dias por mês), buscando novas perspectivas sobre os gastos dos clientes.
8.  **Salvamento dos Dados Tratados**: Ao final do processo, o DataFrame limpo e transformado foi salvo em um arquivo `TelecomX-processed.csv`, garantindo que a etapa de análise exploratória pudesse ser executada de forma independente e reprodutível.

## 3. Análise Exploratória de Dados

Com os dados devidamente tratados, iniciamos a análise exploratória para extrair insights.

### Análise Descritiva Geral

Uma análise estatística inicial com o método `describe()` nos forneceu uma visão geral das variáveis numéricas, incluindo média, desvio padrão, e quartis para colunas como `Meses_Contrato`, `Contas_Mensais` e `Contas_Totais`.

### Distribuição da Evasão

Primeiramente, analisamos a proporção de clientes que evadiram em relação aos que permaneceram. O gráfico de barras mostrou que a base de clientes possui uma taxa de evasão de aproximadamente **26.5%**, um valor considerável que justifica a investigação aprofundada.

_( gráfico de barras da distribuição da variável `Evasao`)_

### Evasão por Variáveis Categóricas

Analisamos a taxa de evasão em relação a diversas características dos clientes e seus contratos:

- **Tipo de Contrato**: A análise revelou que clientes com **contrato mensal** têm uma taxa de evasão drasticamente superior àqueles com contratos de 1 ou 2 anos. Isso sugere que a falta de um compromisso de longo prazo é um forte indicador de risco de churn.
- **Forma de Pagamento**: Clientes que utilizam **boleto eletrônico** como forma de pagamento apresentaram uma taxa de churn mais elevada em comparação com outras formas, como cartão de crédito ou débito automático.
- **Serviços Adicionais**: Observou-se que clientes que **não possuem serviços de proteção**, como `Seguranca_Online` e `Backup_Online`, tendem a evadir mais. Isso pode indicar que clientes com mais serviços integrados percebem maior valor e têm maior "aderência" à empresa.

_(os gráficos de contagem (countplot) comparando a evasão por `Tipo_Contrato`, `Forma_Pagamento`, etc.)_

### Evasão por Variáveis Numéricas

A relação entre as variáveis numéricas e a evasão também trouxe insights importantes:

- **Meses de Contrato**: Histogramas e boxplots mostraram que a **maioria dos clientes que evadem o faz nos primeiros meses** de contrato. A taxa de churn diminui consideravelmente à medida que o tempo de permanência do cliente aumenta.
- **Contas Mensais**: Clientes com **contas mensais mais altas** tendem a ter uma taxa de churn maior. Isso é especialmente verdade para o grupo com contrato mensal, onde o valor elevado pode ser um fator decisivo para a busca por alternativas mais baratas.

_(Sugestão: Insira aqui os histogramas ou boxplots para `Meses_Contrato` e `Contas_Mensais`, segmentados pela variável `Evasao`)_

## 4. Conclusões e Insights

A análise dos dados nos permitiu extrair as seguintes conclusões:

1.  **O Perfil do Cliente que Evade**: O cliente com maior probabilidade de evasão é aquele com **pouco tempo de casa**, **contrato mensal**, que paga via **boleto eletrônico** e **não possui serviços adicionais de segurança**.
2.  **Contratos de Longo Prazo são a Chave para a Retenção**: A diferença na taxa de churn entre contratos mensais e anuais/bianuais é o insight mais forte da análise. A fidelização por meio de contratos mais longos é extremamente eficaz.
3.  **Os Primeiros Meses são Críticos**: A jornada inicial do cliente é um período de alto risco. A falta de engajamento ou problemas não resolvidos no início do relacionamento podem levar a uma saída prematura.
4.  **Valor Percebido Importa**: Clientes que contratam mais serviços (como segurança e backup) tendem a ficar mais tempo. Isso sugere que quanto mais integrado o cliente está ao ecossistema de produtos da empresa, menor a chance de ele sair.

## 5. Recomendações

Com base nas conclusões, as seguintes ações estratégicas são recomendadas para a empresa:

- **Incentivar Contratos de Longo Prazo**: Criar campanhas ativas para migrar clientes de contratos mensais para planos de 1 ou 2 anos, oferecendo descontos, benefícios exclusivos ou upgrades de serviço como incentivo.
- **Focar na Retenção Inicial (Onboarding)**: Desenvolver um programa de _onboarding_ para novos clientes, com acompanhamento proativo nos primeiros 3 a 6 meses para garantir a satisfação, tirar dúvidas e apresentar os benefícios dos serviços contratados.
- **Promover Pacotes de Serviços (Bundles)**: Oferecer pacotes que incluam serviços de segurança, backup e suporte técnico premium a preços atrativos. Isso não só aumenta a receita, mas também a "aderência" do cliente, tornando a troca de provedor mais complexa e menos atraente.
- **Otimizar Formas de Pagamento**: Investigar por que o boleto eletrônico está associado a um churn maior. Pode ser por esquecimento, dificuldade no pagamento ou menor compromisso. Oferecer pequenos descontos para quem adere ao débito automático ou cartão de crédito pode ser uma solução eficaz.
- **Ações Preditivas**: Utilizar os insights desta análise para construir um modelo de machine learning que preveja a probabilidade de churn para cada cliente. Com isso, a equipe de retenção pode agir de forma proativa nos clientes de maior risco, antes que eles decidam cancelar o serviço.
  Espero que este relatório detalhado seja útil para a conclusão do seu projeto. Ele estrutura a narrativa da sua análise, conectando os passos técnicos com os insights de negócio.
