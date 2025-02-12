import joblib
from pathlib import Path
import os
import numpy 
import pandas

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load("artifacts/model_trainer/model.joblib")
        
    def predict(self,data):
        
        return self.model.predict(data)