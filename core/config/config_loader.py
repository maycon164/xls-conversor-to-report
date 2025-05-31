import yaml

class ConfigLoader:

    def load(self, path: str):
        with open(path, "r") as config_file:
            config = yaml.safe_load(config_file)
        return config