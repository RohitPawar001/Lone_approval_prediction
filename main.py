
from src.lone_approval_prediction import logger
from lone_approval_prediction.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline
from lone_approval_prediction.entity.config_entity import DataIngestionConfig

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} has started <<<<<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>> sateg {STAGE_NAME} has completed <<<<<<<")
except Exception as e:
    logger.info(e)
    