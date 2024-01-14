import os
from pathlib import Path

from config_manager import ConfigManager

def main():
    print("Loading config")

    config_manager = ConfigManager()
    config_path = Path(os.path.dirname(__file__)) / "config.yaml"
    config_manager.load_config(config_path)

    logging_config = config_manager.config_data.get('logging')
    print(f"Logging configuration: {logging_config}")

    test_config_manager = ConfigManager()
    print(config_manager is test_config_manager)

if __name__ == "__main__":
    main()