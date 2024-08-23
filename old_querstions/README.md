#### Which feature in Airflow allows tasks to communicate with each other and share data?

- XComs
- Hooks
- Variables
- Connections

**Ans:** XComs

---

#### Which of the following best describes what a Transfer Operator does?

- It sends notifications or alerts during the execution of a workflow
- It intakes and transforms data into a different format or structure
- It evaluates conditions and determines the path the workflow should take
- It moves or transfers data between different sources, destinations, or storage systems

**Ans:** It moves or transfers data between different sources, destinations, or storage systems

---

#### Which parameters are optional when creating a new DAG object without using the `@dag` decorator? (select all that apply)

- schedule_interval
- dag_id
- start_date
- default_args

**Ans:** `schedule_interval`, `start_date`, `default_args`

---

#### Assume there are multiple tasks running on a single DAG. When the DAG is run, it takes a while to complete. What Airflow UI view would be most helpful in identifying the bottleneck?

- DAGs view
- Gantt view
- Tree view
- Graph view

**Ans:** The Gantt view

---

#### What Airflow CLI command runs a task without checking for dependencies or recording its state in the metadata database?

- `airflow dags test`
- `airflow tasks start`
- `airflow standalone`
- `airflow tasks test`

**Ans:** `airflow tasks test`

---

#### Assume there is a DAG with six tasks labeled `t0`, `t1`, `t2`, `t3`, `t4`, and `t5`. Would writing the DAG’s task dependency as `[t0, t1] >> t2 >> [t3, t4] >> t5` work?

- Yes
- No

**Ans:** Yes

---

#### What is the default timezone in Airflow?

- EST
- AEST
- UTC
- The user's local timezone

**Ans:** UTC

---

#### The team member doesn't see the new task in the DAG on the Airflow UI. What could be the cause?

- Airflow has a default delay of up to 5 minutes to detect a new task in a DAG.
- Airflow has a default delay of up to 30 seconds to detect a new task in a DAG.
- The task dependency setup is incorrect.
- The schedule_interval parameter is missing.

**Ans:** Airflow has a default delay of up to 5 minutes to detect a new task in a DAG.

---

#### Which of the following best describes what a Sensor Operator does?

- It evaluates conditions and determines the path a workflow should take.
- It waits for a certain condition to be met before proceeding with a workflow.
- It provides various utility functions to support workflow management.
- It sends notifications or alerts during the execution of a workflow.

**Ans:** It waits for a certain condition to be met before proceeding with a workflow.

---

#### Assume there is a DAG with four tasks labeled `t0`, `t1`, `t2`, and `t3`. Would writing the DAG’s task dependency as `[t0, t1] >> [t2, t3]` work?

- No
- Yes

**Ans:** Yes

---

#### If a DAG has a `schedule_interval` parameter with the value of `@daily` and a `catchup` parameter with the value of `True`, how far back in time will Airflow try to catch up on missed DAG runs?

- One day
- One week
- All days from the set `start_date` parameter value of the DAG
- One month

**Ans:** All days from the set `start_date` parameter value of the DAG

---

#### What is a XCom?

- A data serialization tool
- A type of task in a DAG
- A way to store data between tasks
- A real-time communication protocol

**Ans:** A way to store data between tasks

---
#### `[task_a, task_b] >> task_e [task_c, task_d] >> task_e`

How many tasks will run at the same time if this DAG is unpaused?

- 5
- 4
- 2
- 3

**Ans:** 4

---

#### What is the purpose of setting dependencies between tasks in Airflow?

- To ensure that tasks are executed in the correct order.
- To improve the performance of the Airflow scheduler.
- To increase the parallelism of task execution.
- To reduce the likelihood of task failures.

**Ans:** To ensure that tasks are executed in the correct order.

---

#### Assume an Airflow instance has a variable named `my_json` which stores a JSON value. Which of the following would return the variable as a Python dictionary?

- `Variable.retrieve('my_json', deserialize_json=True)`
- `Variable.get('my_json')`
- `Variable.retrieve('my_json', deserialize_json=False)`
- `Variable.get('my_json', deserialize_json=True)`

**Ans:** `Variable.get('my_json', deserialize_json=True)`

---

#### Which of the following statements are true about a DAG in Airflow? (select all that apply)

- A DAG’s nodes define its tasks, and the directed edges define the dependencies between those tasks.
- It is a good practice to have loops in a DAG.
- DAG stands for Directed Acyclic Graph.
- A DAG is a programming language used for data analysis.

**Ans:** 
- A DAG’s nodes define its tasks, and the directed edges define the dependencies between those tasks.
- DAG stands for Directed Acyclic Graph.

---

#### Which of the following is a valid way to create a connection in Airflow? (select all that apply)

- Environment Variables
- Airflow CLI
- Airflow UI
- Inside of a XCom

**Ans:** 
- Environment Variables
- Airflow CLI
- Airflow UI

---

#### What are the core architectural components of Airflow? (select all that apply)

- A web server
- A scheduler
- An executor
- A metadata database
- DAGs
- A NoSQL database

**Ans:** 
- A web server
- A scheduler
- An executor
- A metadata database
- DAGs

---

#### Assume an Airflow user lives in New York, which is in the timezone UTC-5, and defines the `start_date` parameter of a DAG with a value of `datetime(2023, 1, 1)`. Will the DAG be triggered at 00:00 on January 1st, 2023, in New York?

- No
- Yes

**Ans:** No

---

#### Assume a data team member is building a connection in Airflow. They notice the provider they are trying to use (e.g., Presto) is missing from the dropdown in the UI. What should they do?

- Find a different provider because if the provider is missing in the dropdown, then it is impossible to use it in Airflow.
- Restart Airflow.
- Find and install the provider package.
- Reinstall Airflow.

**Ans:** Find and install the provider package.

---

#### Assume there is a DAG with four tasks labeled `t0`, `t1`, `t2`, and `t3`. Is writing the DAG's task dependency as `t0 >> t1 >> t2 >> t3` equivalent to writing `t3 << t2 << t1 << t0`?

- Yes
- No

**Ans:** Yes

---
```python
with DAG(
    'basic_python_dag',
    schedule_interval='@daily',
    catchup=False
):
    
    python_task = PythonOperator(
        python_callable=lambda: print('Hello Learner!')
    )
```
---

#### Which of the following are issues with this DAG? (select all that apply)

- The tags parameter is missing
- The PythonOperator is missing a `task_id` parameter
- The `start_date` parameter is missing
- The value assigned to the `python_callable` parameter has an error

**Ans:** 
- The PythonOperator is missing a `task_id` parameter
- The `start_date` parameter is missing

---

#### In which of the following places do Airflow users set up the dependencies between tasks in a DAG?

- In a Python file in the 'includes' directory
- In the Airflow UI
- In the DAG file itself
- In a separate configuration file

**Ans:** In the DAG file itself

---

#### Assume there is a DAG with defined task dependencies running in an Airflow instance. What would be the most helpful Airflow UI view for an overview of the dependencies?

- Graph view
- Gantt view
- Grid view
- DAGs view

**Ans:** Graph view

---

#### In a typical Airflow setup, what folder is parsed by the scheduler for new DAG files?

- The `/plugins` folder
- The `/airflow` folder
- The `/dags` folder
- The `/include` folder

**Ans:** The `/dags` folder

---

#### What mode is considered best practice to use when a sensor’s `poke_interval` parameter value is set to a very short duration (< 5 minutes)?

- `reschedule`
- `poke`

**Ans:** `reschedule`

---

#### After several weeks of testing, a data team has decided to use Airflow in their tech stack. Before getting started, they need to communicate with their DevOps team to set up an Airflow instance on Linux Ubuntu OS. However, the DevOps team needs to know which version of Python is currently running on the environment that the data team has been testing.

Which of the following Airflow CLI commands would quickly allow the team to know what version of Python the environment is running?

- `airflow info`
- `airflow python version`
- `airflow standalone`
- `airflow version`

**Ans:** `airflow info`

---

#### What mode is considered best practice to use when a sensor’s `poke_interval` parameter value is set to greater than 5 minutes?

- `poke`
- `reschedule`

**Ans:** `poke`

---

#### A member of a data team writes a Python script that downloads data from an API and stores it in a database on a daily basis. Is this scenario a use case for Airflow?

- No
- Yes

**Ans:** Yes

---

#### Which of the following ways allows the code to avoid defining a DAG object in all operators (`dag=dag`)? (select all that apply)

- By instantiating the DAG object with the context manager `with`
- By giving all tasks the same `task_id`
- By creating a `default_argument` dictionary
- By defining tasks within a function decorated by `@dag`

**Ans:** 
- By instantiating the DAG object with the context manager `with`
- By defining tasks within a function decorated by `@dag`

---
#### Take a look at the code below from a `.env` file that creates a Snowflake connection:

`AIRFLOW_CONN_SNOWFLAKE_CONN='snowflake://LOGIN:PASSWORD@/?account=xy12345&region=eu-central-1'`

What is the connection ID?

- SNOWFLAKE_CONN
- CONN_SNOWFLAKE_CONN
- AIRFLOW_CONN_SNOWFLAKE_CONN
- SNOWFLAKE

**Ans:** SNOWFLAKE_CONN

---

#### Assume a member of a data team working with Airflow added a new DAG file into the `/dags` folder but reports that it doesn't show up on the Airflow UI. Which of the following could be causing the issue? (select all that apply)

- Airflow has a default delay of 5 minutes before Airflow acknowledges the new DAG file.
- The `.airflowignore` file has the name of the file in it.
- The code in the DAG does not contain any words, including `airflow` or `dag`.
- The Airflow instance must be restarted for the DAG to show up on the UI.

**Ans:** The `.airflowignore` file has the name of the file in it.  
The code in the DAG does not contain any words, including `airflow` or `dag`.

---

#### Once a DAG has a unique ID, the next step is to define when it will start being scheduled. Let's consider the scenario where the goal is to start scheduling the DAG as of 2023/01/01. Which of the following parameters would accomplish this?

- `start_date=datetime(1 , 1, 2023)`
- `start_date='2023/01/01'`
- `start_date=datetime(2023, 1 , 1)`
- `schedule_interval=datetime(2023, 1, 1)`

**Ans:** `start_date=datetime(2023, 1, 1)`

---

#### What is a DAG run?

- An object grouping all DAGs.
- A special Airflow object that determines the schedule of a DAG.
- A specific run or instance of a task.
- A specific run or instance of a DAG.

**Ans:** A specific run or instance of a DAG.

---

#### What method allows an Airflow user to add data to XComs?

- By executing the method `xcom_pull`
- By executing the method `xcom_add`
- By executing the method `xcom_push`
- By providing the data to the `xcom` parameter of the DAG object

**Ans:** By executing the method `xcom_push`

---

#### What is the default timeout value of a sensor?

- 1 day
- 7 days
- 1 minute
- 7 hours

**Ans:** 1 day

---

#### Take a look at the code below from a `.env` file that creates a PostgreSQL connection:

`AIRFLOW_CONN_POSTGRES='my-conn-type://login:password@host:port/schema?param1=val1&param2=val2'`

Is this the correct way to create a connection using an environment variable?

- Yes
- No

**Ans:** No

---

#### Which of the following is the correct way to define an Airflow variable using an environment variable with the name `customer_folder` and the value `'my_folder'`?

- `AIRFLOW_CUSTOMER_FOLDER='my_folder'`
- `CUSTOMER_FOLDER='my_folder'`
- `AIRFLOW_VAR_CUSTOMER_FOLDER='my_folder'`
- `AIRFLOW_VARIABLE_CUSTOMER_FOLDER='my_folder'`

**Ans:** `AIRFLOW_VAR_CUSTOMER_FOLDER='my_folder'`

---

#### Assume a scenario where a company is running a website, and a specific DAG should only be triggered when a customer hits a button on a form. This means that the DAG should not be scheduled. Which of the following values for the `schedule_interval` parameter of the DAG accomplishes this?

- `schedule_interval=None`
- `schedule_interval='@once'`
- `schedule_interval='@never'`
- `schedule_interval=''`

**Ans:** `schedule_interval=None`

---

#### What types of data can be stored in an Airflow variable? (select all that apply)

- Python Dataclasses
- JSON
- Strings
- Integers

**Ans:** JSON  
Strings  
Integers

---

#### A DAG was designed to fetch data from files coming from different data sources. The DAG has to be triggered every day at 7:00 AM. What value should be assigned to the `schedule_interval` DAG parameter to achieve this scheduling frequency?

- `schedule_interval=timedelta(hours=6)`
- `schedule_interval=timedelta(hours=7)`
- `schedule_interval='0 7 * * *'`
- `schedule_interval='7 * * * *'`

**Ans:** `schedule_interval='0 7 * * *'`

---

#### What is the purpose of the `catchup` parameter in a DAG?

- It determines the number of retries for failed tasks.
- It determines whether the DAG should be run retroactively for missed intervals.
- It determines whether the DAG should be scheduled to run in the future.
- It determines the schedule interval for the DAG.

**Ans:** It determines whether the DAG should be run retroactively for missed intervals.

---

#### Which of the following are valid values for scheduling a DAG in Airflow? (select all that apply)

- Integers
- Calendar
- Timedelta
- Cron

**Ans:** Timedelta  
Cron

---

#### Assume a DAG is scheduled to run daily at 00:00. The start date is January 1st, 2023. What is the `data_interval_start` (logical_date) for the first DAG Run?

- 2023/01/02 23:59
- 2023/01/01 00:00
- 2023/01/01 00:01
- 2023/01/02 00:00

**Ans:** 2023/01/01 00:00

---
```python
@dag(start_date=datetime(2023, 1, 1), catchup=False)
def my_dag():
    
    @task
    def my_task():
        print('My task executed')
```
#### This DAG doesn't show up on the Airflow UI. Why?

- The `schedule_interval` parameter is missing
- `my_dag` isn't called
- The `catchup` parameter is set to False
- The `start_date` parameter is incorrectly formatted

**Ans:** `my_dag` isn't called

---

#### What happens if two DAGs share the same `dag_id` parameter?

- Airflow will use the DAG with the earlier `start_date` parameter value and disregard the other DAG.
- Airflow will automatically assign a new `dag_id` parameter value to one of the two DAGs.
- Airflow will throw an error because it does not allow two DAGs to share the same `dag_id`.
- Airflow will exhibit unpredictable behavior and may switch randomly between the two DAGs.

**Ans:** Airflow will throw an error because it does not allow two DAGs to share the same `dag_id`.

---

#### Which of the following Airflow CLI commands is necessary to run to create the metadata database?

- `airflow db check`
- `airflow db init`
- `airflow db reset`
- `airflow db start`

**Ans:** `airflow db init`

---

#### Assume a DAG needs to process data one month before the value of the DAG’s `start_date` parameter. Which of the following Airflow CLI commands is the best way to accomplish this?

- `airflow dags backfill`
- `airflow dags run`
- It is not possible in Airflow
- `airflow dags trigger`

**Ans:** `airflow dags backfill`

---

#### What does it mean when a DAG’s task has the status of queued?

- The task is executed immediately.
- The task has been assigned to an Executor and is awaiting a worker.
- The task is waiting to be scheduled.
- The task is running in a worker.

**Ans:** The task has been assigned to an Executor and is awaiting a worker.

---

#### Assume an Airflow variable with the name `airtable_api_key` was created via the Airflow UI. Will the variable's value be hidden on the Airflow UI?

- Yes
- No

**Ans:** No

---

#### Assume multiple DAGs are running in an Airflow instance. Which of the following Airflow UI views would be most helpful in providing an overview of all DAG runs of a single DAG as well as showing the state of each task in each run?

- Gantt view
- Grid view
- DAGs view
- Landing Times view

**Ans:** Grid view

---
```python
dag = DAG(
    'basic_bash_dag',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
)
```
#### Assuming the current date is 2023/01/04, how many DAG runs will occur right after the DAG is triggered?

- 1
- 0
- 4
- 2

**Ans:** 2

---

#### What does the "Last Run" column represent?

- The end date/time of the most recent DAG run.
- The date when the DAG is scheduled to run next.
- The interval of time between each DAG run.
- The start date/time of the latest DAG run.

**Ans:** The end date/time of the most recent DAG run.

---

#### What does the Recent Task component represent?

- All of the statuses of tasks from all active or most recent DAG runs.
- Only failed, success, or skipped task statuses from all active or most recent DAG runs.
- The status of all previous DAG runs.
- The status of all future DAG runs.

**Ans:** Only failed, success, or skipped task statuses from all active or most recent DAG runs.

---

#### What is an Airflow provider?

- Operators that are part of core Airflow, like the PythonOperator and the BashOperator.
- A configuration in Airflow that allows users to control the number of tasks running at a time.
- A Docker image that installs Airflow.
- A separate Python package that extends Airflow’s functionality, in most cases by integrating with external systems or services.

**Ans:** A separate Python package that extends Airflow’s functionality, in most cases by integrating with external systems or services.

---

#### What is the purpose of the PythonOperator in Airflow?

- To manage Python virtual environments for Airflow tasks
- To schedule Python scripts to run on a regular basis
- To execute Python code as a task in a DAG
- To deploy Python packages to remote servers

**Ans:** To execute Python code as a task in a DAG

---

#### Which of the following `DAG` `schedule_interval` parameter Cron values would cause a DAG to run every day at midnight? (select all that apply)

- `0 0 * * *`
- `0 0 * * 0`
- `0 * * * *`
- `@daily`

**Ans:** `0 0 * * *` and `@daily`

---

#### A member of a data team is tasked with checking whether multiple data pipelines have failed every morning. If they have, then they have to rerun them manually. They are looking for a data tool that offers automated notifications when something goes wrong with the data pipelines. Is this scenario a use case for Airflow?

- No
- Yes

**Ans:** Yes

---

#### What is the purpose of an Airflow variable? (select all that apply)

- To avoid hardcoding a value
- To reuse a value across multiple DAGs
- To store large amounts of data
- To store a XCom

**Ans:** To avoid hardcoding a value and To reuse a value across multiple DAGs

---

#### An Airflow variable was created using an environment variable and is not visible on the Airflow UI. Can it still be accessed/used in DAGs?

- No
- Yes

**Ans:** Yes

---

#### Assume a DAG experienced a bug, and a data team needed to pause the DAG to fix it. The bug took 3 days to fix. The DAG is scheduled to be triggered every day and has a DAG `start_date` parameter value of `2023/01/05 00:00`. The current date after the fix is `2023/01/08 10:00`. If the DAG is unpaused; how many running DAG runs will occur if the DAG `catchup` parameter value is set to True?

- 2
- 4
- 3
- 1

**Ans:** 3

---

#### What is the role of the executor in Airflow?

- It executes tasks.
- It schedules tasks.
- It deletes unwanted tasks.
- It defines how tasks are executed and on which system.

**Ans:** It defines how tasks are executed and on which system.

---

#### What is a limitation of using XComs? (select all that apply)

- XComs can only be used with a maximum of two tasks in a DAG.
- XComs are the only way to share data between tasks.
- There must be a defined DAG with at least one associated task to create an XCom.
- The amount of data that can be given to an XCom is limited.

**Ans:** There must be a defined DAG with at least one associated task to create an XCom and The amount of data that can be given to an XCom is limited.

---

#### What happens when a DAG is deleted by using the Airflow UI?

- The file corresponding to the DAG is put into an archives directory.
- All metadata related to the DAG is removed from the metadata database. The file corresponding to the DAG is deleted.
- All metadata related to the DAG is removed from the metadata database. The file corresponding to the DAG is not deleted.
- The file corresponding to the DAG is deleted. Only the history of the DAG runs remains in the Airflow UI.

**Ans:** All metadata related to the DAG is removed from the metadata database. The file corresponding to the DAG is not deleted.

---
```python
with DAG(
    'data_dag',
    schedule='@daily'
    catchup=False
):

    task_a = BashOperator(
        task_id='task_a',
        bash_command='echo "Executing task A"'
    )

    task_b = BashOperator(
        task_id='task_b',
        bash_command='echo "Executing task B"'
    )

  task_a >> task_b
```
#### Would this DAG be able to run properly?

- No
- Yes

**Ans:** No

---

#### What method allows an Airflow user to get data from an XCom?

- By executing the method `xcom_push`
- By executing the method `xcom_pull`
- By executing the method `xcom_add`
- By providing the data to the `xcom` parameter of the DAG object

**Ans:** By executing the method `xcom_pull`

---

#### A CEO asks their company’s data team to create a dashboard that analyzes user behavior in the company's product. Which of the following best describes how Airflow can help create that dashboard?

- Airflow can be used to build the analytics dashboard directly in the Airflow UI.
- Airflow can be used as the product’s primary database for user information which powers the dashboard.
- Airflow can be used to schedule a data pipeline that ingests user data into a data warehouse that powers the dashboard.
- Airflow can be embedded directly into a product to analyze user click events and present the information as a dashboard.

**Ans:** Airflow can be used to schedule a data pipeline that ingests user data into a data warehouse that powers the dashboard.

---

#### In a bank setting, a DAG is designed to process awaiting transfers. To accomplish this, the DAG should be triggered every 4 hours, starting from the date `datetime(2023, 1, 1)`. What value should be assigned to the `schedule_interval` DAG parameter to achieve this scheduling frequency?

- `schedule_interval='0 4 * * *'`
- `schedule_interval='4'`
- `schedule_interval=timedelta(hours=4)`
- `schedule_interval='/4 * * * *'`

**Ans:** `schedule_interval=timedelta(hours=4)`

---

#### A member of a data team has a SQL script that aggregates data about their company's previous day’s performance. They want to schedule the SQL script to run every day at midnight. Is this scenario a use case for Airflow?

- No
- Yes

**Ans:** Yes

---
#### What would be the Cron value of the `schedule_interval` parameter of a DAG if it needed to be triggered every two hours but only on weekends?

- `0 */2 * * 6,7`
- `0 2 * * 6,7`
- `0 */2 2 * 0,1`
- `0 0/2 * * 6,7`

**Ans:** `0 */2 * * 6,7`

---

#### What is the role of the Airflow scheduler?

- To execute tasks.
- To both trigger scheduled workflows and submit tasks to the executor to run.
- To define how tasks are executed and on which system.
- To define the interval of when a task is expected to be executed.

**Ans:** To both trigger scheduled workflows and submit tasks to the executor to run.

---

#### Assume a DAG is set to run daily but is paused on 2023/05/11 at 08:00 UTC. The DAG was then unpaused on 2023/05/15 at 10:00 UTC. How many DAG runs will occur if the DAG `catchup` parameter value is set to False?

- 0
- 1
- 4
- 5

**Ans:** 1

---