
from src.lone_approval_prediction import logger
from lone_approval_prediction.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline
from lone_approval_prediction.pipeline.stage_02_data_validation_pipeline import DatavalidationPipeline
from lone_approval_prediction.pipeline.stage_03_data_transformation_pipeline import DataTransformationPipeline
from lone_approval_prediction.pipeline.stage_04_model_trainer_pipeline import ModelTrainerPipeline 
from lone_approval_prediction.pipeline.stage_05_model_evaluation_pipeline import ModelEvaluationPipeline 


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} has started <<<<<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} has completed <<<<<<<")
except Exception as e:
    logger.info(e)



STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} has started <<<<<<<<<<")
    obj = DatavalidationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} has completed <<<<<<<")
except Exception as e:
    logger.info(e)
    
STAGE_NAME = "Data transformation Stage"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} has started <<<<<<<<<<")
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} has completed <<<<<<<")
except Exception as e:
    logger.info(e)
    
    
STAGE_NAME = "Model training Stage"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} has started <<<<<<<<<<")
    obj = ModelTrainerPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} has completed <<<<<<<")
except Exception as e:
    logger.info(e)
    
    
STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} has started <<<<<<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} has completed <<<<<<<")
except Exception as e:
    logger.info(e)
    
    
    