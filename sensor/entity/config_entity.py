import os

TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

class TrainingPipelineConfig:

    def __init__(self):
        self.artifact_dir = os.pth.join(os.getwd(), "artifact", f"")

class DataIngetionCofig:

    def __init__(self, taining_pipeline_config:TrainingPipelineConfig):
        self.database_name:"aps"
        self.collection_name="sensor"
        self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact,)
        self.feature_store_file_path = os.path.join(self.data_ingestion_dir, "feature_store", )
        self.train_file_path = os.path.join()
        self.test_file_path = os.path.join()

    def to_def(self, )->dict:
        pass

class DataValidationConfog:...
class DataTransformation:...
class ModelTrainerArtifact:...
class ModelEvaluationArtifact:...
