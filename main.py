"""import sys
import os
src_path = "D:\\software\\python_vs\\loan_approval_prediction\\src"
sys.path.append(os.path.abspath(src_path))
print("Current sys.path:", sys.path)"""






from lone_approval_prediction import logger
from lone_approval_prediction.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline
from lone_approval_prediction.entity.config_entity import DataIngestionConfig

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} has started <<<<<<<<<<")
    obj = DataIngestionConfig()
    obj.main()
    logger.info(f">>>>>>>>>>>>> sateg {STAGE_NAME} has completed <<<<<<<")
except Exception as e:
    logger.info(e)
    