from airflow.decorators import dag,task
from datetime import datetime,timedelta

default_args = {
    'owner': 'airflow',
    'catchup': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

@dag(
    dag_id="custom_image_py_packages",
    default_args=default_args,
    schedule=timedelta(minutes=3),
    start_date=datetime(2025,12,2),
    doc_md="This is a custom image and py packages dag" #Tells about the dag
)
def custom_image_py_packages():
    @task
    def matplotlib_import():
        import matplotlib
        print("Matplotlib imported" + matplotlib.__version__)    
    matplotlib_import()

custom_image_py_packages()



