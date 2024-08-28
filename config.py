import json
import loggers
from dataclasses import dataclass


@dataclass
class Config:
    bucket_name: str = ''
    prefix_name: str = ''
    extension_name: str = ''
    output_file: str = ''

    @staticmethod
    def get_config(filename: str):
        """creating config (instance) with bucket, prefix, extension names and output file"""
        config = Config()
        loggers.logging.info("Searching and finding json")
        try:
            with open(filename, "r") as f:
                file_content = f.read()
                content_dict = json.loads(file_content)
                config.bucket_name = content_dict['bucket_name']
                config.prefix_name = content_dict['prefix_name']
                config.extension_name = content_dict['extension_name']
                config.output_file = content_dict['output_file']
                loggers.logging.info(f"{filename} opened successfully")
        except FileNotFoundError:
            loggers.logging.error("File Not Found: Please provide json")
            exit()
        return config


