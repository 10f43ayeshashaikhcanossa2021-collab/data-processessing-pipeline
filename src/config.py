import json


def load_config(config_path="config/config.json"):
    """
    Load pipeline configuration from a JSON file.
    """

    with open(config_path, "r") as file:
        config = json.load(file)

    return config