import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import mutual_info_classif
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from collections import Counter
from lone_approval_prediction import logger
from lone_approval_prediction.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config
        self.data = pd.read_csv(self.config.data_file_path)
        
    def drop_unwanted_columns(self,unwanted_features:list):
        for feature in unwanted_features:
            if feature in self.data.columns:
                data.drop(feature,axis=1,inplace=True)
                logger.info(f"{feature} has been removed from the dataset")
            else:
                logger.info(f"{feature} does dont exists in this dataset")
    
    def preprocess_data(self):
        
        encoding =  OrdinalEncoder()
        categorical_features = [feature for feature in self.data.columns if self.data[feature].dtype == "O"]
        for feature in categorical_features:
            try:
                self.data[f"{feature}_encodded"] = encoding.fit_transform(self.data[[feature]])
                logger.info(f"{feature} has been encodded successfully with {feature}_encodded")
                self.data.drop(feature,axis=1,inplace=True)
                logger.info(f"{feature} has been deleted successfully")
            except Exception as e:
                raise e
            
        
        return self.data
    
    def train_test_split(self):
        data = self.preprocess_data()  
         

        X = data.iloc[:, :-1]
        y = data.iloc[:, -1].astype("int")

        mi = mutual_info_classif(X, y)
        mi_df = pd.DataFrame({'Feature': X.columns, 'Mutual Information': mi})
        mi_df = mi_df.sort_values(by='Mutual Information', ascending=False)
        top_features = mi_df.head(5)['Feature']

        X = data[top_features]

        X_train, X_test_, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
        
        scaler = StandardScaler()
        
        X_train = scaler.fit_transform(X_train)
        
        desired_percentage = 0.5

        current_counts = Counter(y_train)
        total_samples = len(y_train)
        minority_class = min(current_counts, key=current_counts.get)
        majority_class = max(current_counts, key=current_counts.get)

        desired_minority_count = int(total_samples * desired_percentage)
        minority_samples_needed = desired_minority_count - current_counts[minority_class]

        
        smote = SMOTE(sampling_strategy={minority_class: current_counts[minority_class] + minority_samples_needed})
        X_train, y_train = smote.fit_resample(X_train, y_train)
        X_train = pd.DataFrame(X_train, columns=X.columns)
        

        X_train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        y_train.to_csv(os.path.join(self.config.root_dir, "y_train.csv"), index=False)
        
        logger.info("Splited data into train and test sets")
        
        