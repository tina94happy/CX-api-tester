# config_parser.py

import yaml
import os

class ConfigParser:
    def __init__(self, config_file):
        self.config_file = config_file

    def get_cx_config(self):
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config', self.config_file)
        with open(config_path, 'r') as file:
            config_data = yaml.safe_load(file)
        return config_data['cx']

