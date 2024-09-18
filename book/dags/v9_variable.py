from airflow.decorators import dag, task
from datetime import datetime
from airflow.models import Variable
import os

"""
For sensitive values, Airflow allows for the creation of hidden variables by specifying certain keywords such as "api_key", "password", or "secret" in the key. These variables remain hidden on the Airflow UI even when edited, providing a safe way to store sensitive information.
"""


"""
set this Variable in Airflow UI
ML_MODEL_PARA = {
  "param": [
    {
      "model_name": "Unet",
      "model_config": {
        "input_shape": [
          255,
          255,
          3
        ],
        "output_shape": [
          255,
          255,
          3
        ],
        "version": "V0.1"
      }
    }
  ]
}

OR 
add in .env file
AIRFLOW_VAR_VARName={"param": ["hello this is .env variable"]}
"""

@dag(
    dag_id="v9_variable",
    start_date = datetime(2024,9,10),
    schedule_interval='@daily', catchup=False)

def test_variable():
    

    @task
    def _get_parameters():
        airflow_parameter =  Variable.get('ML_MODEL_PARA',deserialize_json=True)["param"]
        for cur_para in  airflow_parameter:
            print(cur_para)
        return True

    @task
    def _get_ENV_parameters(temp):
      dot_env =  Variable.get('OS_ENVNAME')
      print("dot_env : ",dot_env)

    @task
    def _get_token(temp):
      dot_env =  Variable.get('API_TOKEN')
      print("API_TOKEN  : ",dot_env)
      
      if dot_env == "12345":
        print("Correct TOKEN")
      return dot_env

    temp = _get_parameters()
    temp1 = _get_token(temp)
    
    temp2 = _get_ENV_parameters(temp1)

test_variable()
    



