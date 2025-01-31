from lone_approval_prediction.config.configuration import ConfigurationManager
from lone_approval_prediction.components.data_ingestion import DataIngestion
from lone_approval_prediction import logger


STAGE_NAME = "data ingestion stage"

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zipfile()
        
if __name__ == "__main__":
    try:
        logger.info(f" {STAGE_NAME} has been started")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f" {STAGE_NAME} has been completed")
    except Exception as e:
        logger.exception(e)
        raise e