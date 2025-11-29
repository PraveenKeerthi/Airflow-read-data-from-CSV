from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime,timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG(
    dag_id="data_from_csv_dag",
    default_args=default_args,
    start_date=datetime(2025, 11, 29),
    schedule=timedelta(minutes=3),
    catchup=False,
)

bash_task = BashOperator(
    task_id="bash_task",
    bash_command="bash /opt/airflow/dags/scripts/wrapper_script.sh ",
    dag=dag,
)

