from networksecuity.components.data_ingestion import DataIngestion
from networksecuity.components.data_validation import DataValidation
from networksecuity.components.data_transformation import DataTransformation
from networksecuity.components.model_trainer import ModelTrainer
from networksecuity.exception.exception import NetworkSecurityException
from networksecuity.logging.logger import logging
from networksecuity.entity.config_entity import DataIngestionConfig , DataValidationConfig , DataTransformationConfig , ModelTrainerConfig
from networksecuity.entity.config_entity import TrainingPipelineConfig 

import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the Data Ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
        print("\n")

        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact , data_validation_config)
        logging.info("Initiated the Data Validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(data_validation_artifact)
        print("\n")

        data_transformation_config = DataTransformationConfig(training_pipeline_config=trainingpipelineconfig)
        data_transformation = DataTransformation(data_validation_artifact , data_transformation_config)
        logging.info("Initiated the Data Transformation")
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation Completed")
        print(data_transformation_artifact)
        print("\n")

        model_trainer_config = ModelTrainerConfig(training_pipeline_config=trainingpipelineconfig)
        model_trainer = ModelTrainer(data_transformation_artifact=data_transformation_artifact , model_trainer_config=model_trainer_config)
        logging.info("Initiated Model Trainer")
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        logging.info("Model Trainer Completed")
        print(model_trainer_artifact)
        print("\n")
    
    except Exception as e:
           raise NetworkSecurityException(e,sys)



