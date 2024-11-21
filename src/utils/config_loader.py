# src/utils/config_loader.py

import yaml
import json

def load_yaml_config(filepath):
    """Loads a YAML configuration file."""
    with open(filepath, 'r') as file:
        config = yaml.safe_load(file)
    return config

def load_json_config(filepath):
    """Loads a JSON configuration file."""
    with open(filepath, 'r') as file:
        config = json.load(file)
    return config
