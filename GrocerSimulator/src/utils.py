import json
from pathlib import Path

CUR_DIR = Path(__file__).parent.absolute()

class Utils:

    @staticmethod
    def readConfig(key: str):
        CUR_DIR = Path(__file__).parent.absolute()
        config = open(CUR_DIR / '../config/config.json')
        config_data = json.load(config)
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
