import os
import pandas as pd
import joblib
from lone_approval_prediction import logger
from sklearn.linear_model import LogisticRegression
from lone_approval_prediction.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config:ModelTrainerConfig) :
        self.config = config
        
    def train_model(self):
        x_train = pd.read_csv(self.config.x_train_data_path)
        y_train = pd.read_csv(self.config.y_train_data_path)
        
        logger.info(f"model trainig has started")
        logistic_regressor = LogisticRegression(penalty=self.config.penalty,C=self.config.C)
        logistic_regressor.fit(x_train,y_train)
        logger.info(f"model trainig has completed")
        
        joblib.dump(logistic_regressor,os.path.join(self.config.root_dir,self.config.model_name))
        
        logger.info(f"model has been saved at {self.config.root_dir}")
        
    