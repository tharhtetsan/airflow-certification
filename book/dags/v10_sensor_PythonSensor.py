from airflow import DAG
from airflow.sensors.python import PythonSensor
from datetime import datetime
from airflow.models import Variable

def _condition():
    dot_env =  Variable.get('API_TOKEN')
    if dot_env == "123456":
        print("Correct TOKEN")
        return True
    
    return False

with DAG(
    dag_id="v10_sensor_PythonSensor",
    start_date=datetime(2024, 9, 10),
    tags=["sensor"],
    schedule="@daily",
    catchup=False,
):
    waiting_for_condition = PythonSensor(
        task_id="waiting_for_condition",
        python_callable=_condition,
        poke_interval=60,
        timeout=7 * 24 * 60 * 60 # ( 7 days by default)
    )

    