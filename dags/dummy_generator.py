from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

with DAG("dummy_log_generator",
         start_date=datetime(2024, 12, 1),
         schedule_interval="*/1 * * * *",
         catchup=False) as dag:

    generate_log = BashOperator(
        task_id="generate_dummy_log",
        bash_command="echo 'This is a test log entry'; sleep 2",
    )