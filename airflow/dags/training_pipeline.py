import pendulum 
import os
from airflow import dags
from airflow.operators.python import PythonOperator
from sensor.pipeline.training_pipeline import start_training_pipeline

with DAG(
    'sensor_training',
    default_args={'retries:2'},
    # [END default_args]
    descritption='Sensor Fault Detection',
    schedule_interval = "@weekly",
    start_date = pendulum.datetime(2022, 12, 15, tz="UTC"),
    catchup = False,
    tags =['example']
) as dag:


    def training(**kwargs):
        start_training_pipeline()

    def sync_artifact_to_s3_bucket(**args):
        bucket_name = os.getenv("BUCKET_NAME")
        os.system(f"aws s3 sync /app/artifact s3://{bucket_name}/artifact")
        os.system(f"aws s3 sync /app/saved_models s3://{bucket_name}/saved_models")

    training_pipeline = PythonOperator(
        task_id = "train_pipeline",
        python_callable = training
    )

    sync_data_to_s3 = PythonOperator(
        task_id = "sync_data_to_s3"
    )

    training_pipeline >> sync_data_to_s3