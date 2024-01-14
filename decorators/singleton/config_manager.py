import yaml
import sys

from singleton_decorator import singleton

@singleton
class ConfigManager:
    def __init__(self):
        self.config_data = {}
    
    def load_config(self, config_path):
        try:
            with open(config_path, "r") as yamlfile:
                data = yaml.load(yamlfile, Loader=yaml.FullLoader)
                self.config_data = data
        except FileNotFoundError as e:
            print(e)
            sys.exit()
