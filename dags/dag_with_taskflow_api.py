from airflow.decorators import dag,task
from datetime import datetime, timedelta

default_args = {
    "owner": "praveen",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

@dag(
    dag_id="dag_with_taskflow_api",
    default_args=default_args,
    schedule=timedelta(minutes=3),
    start_date=datetime(2025,11,29),
    catchup=False,
)
def taskflow_api():
    @task()
    def get_name():
        return "Praveen"    

    @task()
    def get_age():
        return 24

    @task()
    def message(name,age,title):
        print(f"Hello my name is {title}.{name} and I am {age} years old")    

    name = get_name()
    age = get_age()
    message(name,age,'Mr')

taskflow_api()
