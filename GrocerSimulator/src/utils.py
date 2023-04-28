import json
import os
from pathlib import Path

CUR_DIR = Path(__file__).parent.absolute()

class Utils:

    @staticmethod
    def readConfig(key: str):
        CUR_DIR = Path(__file__).parent.absolute()
        config = open(CUR_DIR / '../config/config.json')
        config_data = json.load(config)
        config.close()
        if(key != ''):
            keys = config_data.keys()
            if(key in keys):

                return config_data[key]
            return ''
        return ''

    @staticmethod
    def isInt(number):
        if(isinstance(number, (int, float))):
            if(number in [False, "False", "True", True]):
                return False
            if(isinstance(number, float)):
                return False
            if(isinstance(number, int)):
                return True
        elif(number.isnumeric()):
            return True
        else:
            return False
    
    @staticmethod
    def export_data(data):
        CUR_DIR = Path(__file__).parent.absolute()
        save_path = CUR_DIR / '../config/customer.json'
        if(Path(CUR_DIR / '../config/customer.json') == True):
            ptf = open(save_path)
            path = Path(ptf)
            if(path.is_file() == True):
                Path.unlink(ptf)
        with open(save_path, 'w') as json_file:
            json.dump(data, json_file)
