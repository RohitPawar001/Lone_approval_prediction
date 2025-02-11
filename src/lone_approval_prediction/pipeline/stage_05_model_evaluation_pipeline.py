from lone_approval_prediction.config.configuration import ConfigurationManager
from lone_approval_prediction.entity.config_entity import ModelEvaluationConfig
from lone_approval_prediction.components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
   
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()
