from networksecuity.components.data_ingestion import DataIngestion
from networksecuity.components.data_validation import DataValidation
from networksecuity.exception.exception import NetworkSecurityException
from networksecuity.logging.logger import logging
from networksecuity.entity.config_entity import DataIngestionConfig , DataValidationConfig
from networksecuity.entity.config_entity import TrainingPipelineConfig 

import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)

        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact , data_validation_config)
        logging.info("Initiated the data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(data_validation_artifact)

        
    except Exception as e:
           raise NetworkSecurityException(e,sys)



