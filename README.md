# databricks-job-monitoring

# 📊 Monitoramento de Performance de Jobs no Databricks

## 📌 Descrição do Projeto
Este projeto tem como objetivo coletar logs de execução dos jobs no **Databricks**, processá-los e armazená-los para futuras análises. A ideia é criar um pipeline de monitoramento que permita entender o desempenho dos jobs e detectar falhas ou lentidão.

## 🚀 Tecnologias Utilizadas
- **Python** → Para extrair e processar os logs da API do Databricks.
- **Databricks API** → Para obter informações dos jobs executados.
- **Pandas** → Para manipulação dos dados extraídos.
- **Parquet** → Para armazenamento otimizado dos logs.

## 📂 Estrutura do Projeto
```
📁 monitoramento-jobs-databricks
│── 📄 databricks_logs_extraction.py  # Script para coletar logs da API
│── 📄 README.md  # Documentação do projeto
```

## 🔧 Como Executar o Script
1. **Configurar as credenciais do Databricks**
   - No arquivo `databricks_logs_extraction.py`, substitua:
     ```python
     DATABRICKS_URL = "https://<seu-workspace>.cloud.databricks.com"
     DATABRICKS_TOKEN = "<seu-token-aqui>"
     ```
   - Coloque o **Databricks Workspace URL** e o **Token de Autenticação**.

2. **Instalar as dependências**
   Se ainda não tiver instalado, execute:
   ```bash
   pip install requests pandas pyarrow
   ```

3. **Rodar o script**
   ```bash
   python databricks_logs_extraction.py
   ```

4. **Verificar a saída**
   - O script gerará um arquivo `databricks_logs.parquet` contendo os logs extraídos.

## 📌 Próximos Passos (AC2, AC3 e Entrega Final)
- **AC2 (06/04):** Criar pipeline de processamento e estruturação dos dados.
- **AC3 (04/05):** Criar dashboard e sistema de alertas para falhas.
- **Entrega Final (08/06):** Refinar o código e documentação final do projeto.

## 📎 Links Importantes
- **[Repositório no GitHub](#)**
- **[Board do GitHub Projects](#)** 
