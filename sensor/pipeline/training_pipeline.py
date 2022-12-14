from sensor.exception import SensorException
from sensor.entity import config_entity
from sensor.components.data_ingetion import DataIngestion
from sensor.components.data_validation import DataValidation
from sensor.components.data_transformation import DataTransformation
from sensor.components.model_trainer import ModelTrainer
from sensor.components.model_evaluation import ModelEvaluation
from sensor.components.model_pusher import ModelPusher
from sensor.logger import logging
import sys


def start_training_pipeline():
    try:
        training_pipeline_config = config_entity.TrainingPipelineConfig()

        # Dataa ingestion
        data_ingetion_config = config_entity.DataIngetionConfig(taining_pipeline_config=training_pipeline_config)
        logging.info(f"{data_ingetion_config.to_dict()}")
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion-config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

        # Data validation 
        data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
        data_validation = DataValidation(
            data_validation_config=data_validation_config,
            data_ingestion_artifact=data_ingestion_artifact
            )
        data_validation_artifact = data_validation.initiate_data_validation()

        # Data transformation
        data_transfromation_config = config_entity.DataTransformationConfig(training_pipeline_config=training_pipeline_config)
        data_transformation =DataTransformation(
            data_transformation_config=data_transformation_config,
            data_ingestion_artifact=data_ingestion_artifact
            )
        data_transformation_artifact = data_transformation.initate_data_transformation()

        # Model trainer 
        model_trainer_config = config_entity.ModelTrainerConfig(trainig_pipeline_config=training_pipeline_config)
        model_trainer = ModelTrainer(
            model_trainer_config=model_trainer_cinfig,
            data_transformation_artifact=data_transformation_artifact
            )
        model_trainer_artifact = model_trainer.initiate_model_trainer()

        # Model evaluation
        model_eval_config = config_entity.ModelEvaluationConfig(training_pipeline_config=training_ppipeline_config)
        model_eval = ModelEvaluation(
            model_eval_config=Model_eval_config, 
            data_ingestion_artifact=data_ingestion_artifact, 
            data_transformation_artifact=data_transformation_artifact, 
            model_trainer_artifact=model_trainer_artifact
            )
        model_eval_artifact = model_eval.initiate_model_evaluation()

        # Model pusher
        model_pusher_config = config_entity.ModelPusherConfig(trainig_pipeline_config)
        model_pusher = ModelPusher(
            model_pusher_config=model_pusher_config, 
            data_transformation_artifact=data_transformation_artifact, 
            model_trainer_artifact=model_trainer_artifact
            )
        model_pusher_artifact = model_pusher.initiate_model_pusher()
    except Exception as e:
        raise SensorException(e, sys)


