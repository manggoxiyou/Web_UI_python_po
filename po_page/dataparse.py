import json
import keyword

import yaml


class DataParse:
    def read_and_parse_data(self, file=None):
        if file is None:
            with open("../data_resource/data.yaml", encoding="UTF-8") as f:
                user_data = yaml.safe_load(f)
        else:
            with open(file, encoding="UTF-8") as f:
                user_data = yaml.safe_load(f)
        return user_data
