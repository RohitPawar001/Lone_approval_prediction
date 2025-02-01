import zipfile
import pandas
import shutil
import os
import urllib.request as request
from pathlib import Path
from lone_approval_prediction import logger
from lone_approval_prediction.utils.comman import get_size



class DataIngestion:
    def __init__(self, config):
        self.config = config

    def download_file(self):
        local_data_file_dir = os.path.dirname(self.config.local_data_file)
        if not os.path.exists(local_data_file_dir):
            os.makedirs(local_data_file_dir, exist_ok=True)

        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded successfully with following info:\n{headers}")
        else:
            print(f"File already exists of size: {os.path.getsize(self.config.local_data_file)}")

    def extract_zipfile(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Extracted all files at {unzip_path}")
