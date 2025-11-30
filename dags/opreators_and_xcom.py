from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "praveen",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

def message(title,ti):
    name = ti.xcom_pull(key="name",task_ids="set_name")
    age = ti.xcom_pull(key="age",task_ids="set_age")
    print(f'Hello my name is {title}.{name} and I am {age} years old')

def set_name(ti):
    ti.xcom_push(key="name",value="Praveen")
def set_age(ti):
    ti.xcom_push(key="age",value=24)

with DAG(
    dag_id="opreators_and_xcom",
    default_args=default_args,
    start_date=datetime(2025, 11, 29),
    schedule=timedelta(minutes=3),
    catchup=False,
) as dag:
    task1 = PythonOperator(
        task_id="message",
        python_callable=message,
        op_kwargs={
            "title": "Mr"
        }
    )

    task2 = PythonOperator(
        task_id="set_name",
        python_callable=set_name,
    )

    task3 = PythonOperator(
        task_id="set_age",
        python_callable=set_age,
    )
    
    task2 >> task3 >> task1
    
    
