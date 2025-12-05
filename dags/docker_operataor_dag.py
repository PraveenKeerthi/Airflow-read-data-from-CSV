from airflow.decorators import dag,task
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.operators.bash import BashOperator
from datetime import datetime,timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 12, 5),
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}


@dag(
    dag_id="docker_operataor_dag",
    default_args=default_args,
    schedule=timedelta(minutes=3),
    doc_md="This dag runs python and docker operator combined"
)
def docker_operataor_dag():

    python_operator = BashOperator(
        task_id='run_python_classes_script',
        bash_command='python /opt/airflow/dags/scripts/understanding_python_classes.py',
    )

    docker_operator = DockerOperator(
            task_id='python_operator_data_manipulation',
            docker_url='unix://var/run/docker.sock',
            image='python_docker',
            api_version='auto', #version of image
            auto_remove='force', #remove container after execution
            container_name="python_docker_container",
        )

    python_operator >> docker_operator
    
docker_operataor_dag()

