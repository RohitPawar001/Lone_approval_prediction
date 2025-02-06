from lone_approval_prediction import logger
from lone_approval_prediction.config.configuration import ConfigurationManager
from lone_approval_prediction.components.data_transformation import DataTransformation

STAGE_NAME = "data transformation stage"

class DataTransformationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.train_test_split()
        
