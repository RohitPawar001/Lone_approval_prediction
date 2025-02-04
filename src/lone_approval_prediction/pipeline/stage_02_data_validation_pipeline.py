from lone_approval_prediction.config.configuration import ConfigurationManager
from lone_approval_prediction.components.data_validation import DataValidation
from lone_approval_prediction import logger

STAGE_NAME = "data validation stage"

class DatavalidationPipeline:
    def __init__(self):
        pass
    
    def main(self):

        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
        
if __name__ == "__main__":
    try:
        logger.info(f" {STAGE_NAME} has been started")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f" {STAGE_NAME} has been completed")
    except Exception as e:
        logger.exception(e)
        raise e