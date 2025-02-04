import os
import pandas as pd
import numpy as np
from lone_approval_prediction import logger

class DataValidation:
    def __init__(self,config):
        self.config = config
    
    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            
            data = pd.read_csv(self.config.unzip_dir)
            all_colls = list(data.columns)
            
            all_schema = list(self.config.all_schema.keys())
            
            for col in all_colls:
                if col.replace(" ","") not in all_schema and col.replace(" ","") != "loan_status":
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as file:
                        file.write(f" validation status : {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as file:
                        file.write(f" validation status : {validation_status}")
                        
            return validation_status
        
        except Exception as e:
            logger.error(f" error during validation {e}")
            raise e
                    
                