import json
import os


class WorkingWithData:

    @staticmethod
    def working_with_data(key, name):
        abs_path = os.path.abspath(__file__)
        file_directory = os.path.dirname(abs_path)
        filepath = os.path.dirname(file_directory)
        file = ""
        if name == "test":
            file = os.path.join(filepath, "test_data/test_data.json")
        elif name == "config":
            file = os.path.join(filepath, "config_files/config.json")
        elif name == "logger_config":
            file = os.path.join(filepath, "config_files/logger_config.json")
        with open(file, "r") as f:
            s = json.load(f)
        for i in s:
            if key in i:
                value = i[key]
                return value
