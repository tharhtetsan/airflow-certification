from airflow.decorators import dag, task
from airflow.sensors.filesystem import FileSensor
from datetime import datetime


"""
added file path in  airflow_settings.yaml
airflow:
  connections:
    - conn_id: fs_default
      conn_type: File (path) 
      conn_host:
      conn_schema:
      conn_login:
      conn_password:
      conn_port:
      conn_extra:
        path: /usr/local/airflow/include/

"""

@dag(
    dag_id= 'v10_sensor_local_file_exist',
    schedule='@daily',
    start_date=datetime(2024, 9, 10),
    tags=['sensor'],
    catchup=False
)
def first_dag():

    wait_for_files = FileSensor.partial(
        task_id='wait_for_files',
        fs_conn_id='fs_default',
    ).expand(
        filepath=['data_1.csv', 'data_2.csv', 'data_3.csv']
    )

    @task
    def process_file():
        print("I processed the file!")

    wait_for_files >> process_file()

first_dag()