from airflow.decorators import dag,task
from datetime import datetime

from airflow.operators.python import PythonOperator

@dag("v6_define_dag_obj_2_decorators", start_date=datetime(2024,8,12), 
        description="This is a hello world pipeline", tags=["hello"],
        schedule='@daily',catchup=False )

def parent_task_flow():
    @task
    def print_a():
        print("hello from task a")


    @task
    def print_b():
        print("hello from task b")

    print_a()

    print_b()

parent_task_flow_obj = parent_task_flow()