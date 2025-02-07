from lone_approval_prediction import logger
from lone_approval_prediction.config.configuration import ConfigurationManager
from lone_approval_prediction.components.model_trainer import ModelTrainer


class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train_model()