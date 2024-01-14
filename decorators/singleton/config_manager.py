import yaml
import sys

from singleton_decorator import singleton

@singleton
class ConfigManager:
    """
    A class for managing configuration data.

    Attributes:
    - config_data (dict): A dictionary to store configuration data.

    Methods:
    - __init__(): Initializes an empty ConfigManager object.
    - load_config(config_path: str): Loads configuration data from a YAML file.
    """
    def __init__(self):
        self.config_data = {}
    
    def load_config(self, config_path):
        """
        Loads configuration data from a YAML file.

        Args:
        - config_path (str): The path to the YAML configuration file.

        Raises:
        - FileNotFoundError: If the specified configuration file is not found.
        """
        try:
            with open(config_path, "r") as yamlfile:
                data = yaml.load(yamlfile, Loader=yaml.FullLoader)
                self.config_data = data
        except FileNotFoundError as e:
            print(e)
            sys.exit()
