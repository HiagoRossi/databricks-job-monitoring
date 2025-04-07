📊 Monitoramento de Performance de Jobs no Databricks

📌 Descrição do Projeto
Este projeto tem como objetivo coletar logs de execução dos jobs no Databricks, processá-los e armazená-los para futuras análises. A ideia é criar um pipeline de monitoramento que permita entender o desempenho dos jobs e detectar falhas ou lentidão.

🚀 Tecnologias Utilizadas
Python → Para extrair e processar os logs da API do Databricks.
Databricks API → Para obter informações dos jobs executados.
Pandas → Para manipulação dos dados extraídos.
Parquet → Para armazenamento otimizado dos logs.

📂 Estrutura do Projeto
📁 monitoramento-jobs-databricks
│— 📄 databricks_logs_extraction.py  # Script para coletar logs da API
│— 📄 README.md  # Documentação do projeto

🔧 Como Executar o Script

📌 Etapa AC1 – Extração de Dados
Configurar as credenciais do Databricks

No arquivo databricks_logs_extraction.py, substitua:

DATABRICKS_URL = "https://<seu-workspace>.cloud.databricks.com"
DATABRICKS_TOKEN = "<seu-token-aqui>"

Coloque o Databricks Workspace URL e o Token de Autenticação.

Instalar as dependências (caso necessário):

pip install requests pandas pyarrow

Rodar o script:

python databricks_logs_extraction.py

Verificar a saída:
O script gerará um arquivo databricks_logs.parquet contendo os logs extraídos.

📌 Etapa AC2 – Processamento e Estruturação dos Dados (06/04)

Nesta etapa foi criado um pipeline em Python (Google Colab) para processar os logs brutos extraídos da API do Databricks. O objetivo foi estruturar os dados para facilitar análises futuras e gerar um novo arquivo tratado.

🔧 Etapas realizadas:

Leitura do arquivo databricks_logs.parquet (gerado na AC1)

Conversão dos timestamps para datetime

Cálculo da duração de execução dos jobs (duration_minutes)

Criação da coluna data_execucao

Seleção de colunas relevantes (job_id, run_id, state, result_state, etc.)

Geração do novo arquivo logs_processados.parquet

Análise exploratória simples (média de duração por resultado, quantidade de execuções por dia)

📁 Arquivos gerados:

logs_processados.parquet

🛠️ Ferramentas:

Python (Google Colab)

Pandas

PyArrow (Parquet)

📌 Próximos Passos (AC3 e Entrega Final)
AC3 (04/05): Criar dashboard e sistema de alertas para falhas.
Entrega Final (08/06): Refinar o código e documentação final do projeto.

📌 Links Importantes
Repositório no GitHub
Board do GitHub Projects

