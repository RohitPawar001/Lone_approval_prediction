from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
    
    
@dataclass
class DataValidationconfig:
    root_dir: Path
    unzip_dir: Path
    STATUS_FILE: str
    all_schema: dict
    
@dataclass
class DataTransformationConfig:
    root_dir : Path
    data_file_path : Path
    
@dataclass
class ModelTrainerConfig:
    root_dir: Path
    x_train_data_path : Path
    y_train_data_path : Path
    model_name : str
    C : float
    penalty : str
    