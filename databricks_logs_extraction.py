import os
import requests
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()
DATABRICKS_URL = os.getenv("DATABRICKS_URL")
DATABRICKS_TOKEN = os.getenv("DATABRICKS_TOKEN")

HEADERS = {"Authorization": f"Bearer {DATABRICKS_TOKEN}"}

# Função para obter os logs de execução dos jobs
def get_job_runs():
    url = f"{DATABRICKS_URL}/api/2.0/jobs/runs/list"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        return response.json().get("runs", [])
    else:
        print("Erro ao buscar os logs:", response.text)
        return []

# Processamento dos logs
def process_logs():
    job_runs = get_job_runs()
    
    if not job_runs:
        print("Nenhum log encontrado.")
        return
    
    # Criando DataFrame
    data = []
    for job in job_runs:
        data.append({
            "job_id": job.get("job_id"),
            "run_id": job.get("run_id"),
            "state": job.get("state", {}).get("life_cycle_state"),
            "result_state": job.get("state", {}).get("result_state"),
            "start_time": job.get("start_time"),
            "end_time": job.get("end_time"),
            "cluster_id": job.get("cluster_instance", {}).get("cluster_id"),
            "creator_user_name": job.get("creator_user_name")
        })
    
    df = pd.DataFrame(data)
    
    # Salvando em arquivo Parquet
    table = pa.Table.from_pandas(df)
    pq.write_table(table, "databricks_logs.parquet")
    
    print("Logs salvos em 'databricks_logs.parquet'")

# Executando o processo
if __name__ == "__main__":
    process_logs()
