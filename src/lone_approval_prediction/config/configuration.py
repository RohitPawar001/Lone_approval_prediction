import os
import zipfile
import urllib.request as request
from lone_approval_prediction.constants import *
from lone_approval_prediction import logger
from lone_approval_prediction.utils.comman import create_directories, read_yaml
from lone_approval_prediction.entity.config_entity import (DataIngestionConfig,
                                                          DataValidationconfig)


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH
    ):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        
        create_directories([self.config["artifacts_root"]])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config["data_ingestion"]
        
        create_directories([config["root_dir"]])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir = config["root_dir"],
            source_url = config["source_url"],
            local_data_file = config["local_data_file"],
            unzip_dir = config["unzip_dir"]
            
        )
        
        return data_ingestion_config
    
    
    def get_data_validation_config(self) -> DataValidationconfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        
        create_directories([config.root_dir])
        
        data_validation_config = DataValidationconfig(
            root_dir= config.root_dir,
            unzip_dir= config.unzip_dir,
            STATUS_FILE= config.STATUS_FILE,
            all_schema= schema
    
        )
        
        return data_validation_config
    