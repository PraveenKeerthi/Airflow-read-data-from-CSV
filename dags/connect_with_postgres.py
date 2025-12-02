from airflow.decorators import task, dag
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import timedelta,datetime

default_args = {
    'owner': 'praveen',
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

@dag(
    dag_id="connect_with_postgres_v1",
    default_args=default_args,
    schedule=timedelta(minutes=3),
    start_date=datetime(2025,12,1),
    catchup=False,
)
def connect_with_postgres():

    @task()
    def connection():
        PostgresOperator(
            task_id='postgres_task',
            postgres_conn_id='postgres_con',
            sql='''
            create table if not exists employees (
                id int primary key,
                name varchar(100),
                age int,
                salary int
           )
            ''',
        )
    connection()

connect_with_postgres()
