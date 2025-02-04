
from src.lone_approval_prediction import logger
from lone_approval_prediction.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline
from lone_approval_prediction.pipeline.stage_02_data_validation_pipeline import DatavalidationPipeline 

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} has started <<<<<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>> sateg {STAGE_NAME} has completed <<<<<<<")
except Exception as e:
    logger.info(e)



STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} has started <<<<<<<<<<")
    obj = DatavalidationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>> sateg {STAGE_NAME} has completed <<<<<<<")
except Exception as e:
    logger.info(e)
    
    
    