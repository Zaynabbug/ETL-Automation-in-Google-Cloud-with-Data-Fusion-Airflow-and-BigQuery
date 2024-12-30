import airflow
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta  
from airflow.providers.google.cloud.operators.datafusion import CloudDataFusionStartPipelineOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 12, 18),
    'depends_on_past': False,
    'email': ['elkasmi.zaynab@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('employee_data',
          default_args=default_args,
          description='Runs an external Python script',
          schedule_interval='@daily',
          catchup=False)
with dag:
    run_script_task = BashOperator(
        task_id='extract_data',
        bash_command='python /home/airflow/gcs/dags/scripts/extract.py',
    )
    start_pipeline = CloudDataFusionStartPipelineOperator(
    location='us-central1',
    pipeline_name='etl_pipeline',
    instance_name='datafusion-deev',
    #pipeline_timeout=1000,
    task_id="start_datafusion_pipeline",
)
    # Set task dependencies
    run_script_task >> start_pipeline