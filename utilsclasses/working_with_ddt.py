import json
import os


class GetDataForDDT:

    @staticmethod
    def get_data_for_ddt():
        data_for_ddt = []
        abs_path = os.path.abspath(__file__)
        file_directory = os.path.dirname(abs_path)
        filepath = os.path.dirname(file_directory)
        file_to_open = os.path.join(filepath, "test_data/ddt_data.json")
        with open(file_to_open, "r") as f:
            json_string_from_file = f.read()
            data_from_file = json.loads(json_string_from_file)
            keys = list(data_from_file.keys())
            values = list(data_from_file.values())
        keys_str = ', '.join(keys)
        lend = len(values[0])
        i = 0
        while i < lend:
            tuples = tuple([k[i] for k in values])
            data_for_ddt.append(tuples)
            i += 1
        return keys_str, data_for_ddt
