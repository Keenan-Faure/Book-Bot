import json
from pathlib import Path
import datetime;

CUR_DIR = Path(__file__).parent.absolute()

class Utils:

    """
    Displays the `error`, `info`, `warning` type 
    `messages` along with the 
    message and `timestamp` on the console/terminal
    """
    @staticmethod
    def logger(status: str='info', message:str=""):
        if(status == "error"):
            print("Error | " + str(message) + " | " + str(datetime.datetime.now()))
        elif(status == "warning"):
            print("Warn | " + str(message) + " | " + str(datetime.datetime.now()))
        elif(status == "info"):
            print("Info | " + str(message) + " | " + str(datetime.datetime.now()))

    """
    reads in the contents of the config.json file 
    using a certain key
    returns en empty string if key is not found
    """
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

    """
    Checks if a variable is an integer
    returns true if it's an integer, false otherwise
    """
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
    
    """
    writes out the `data` to a customer.json file
    """
    @staticmethod
    def export_data(data: dict):
        CUR_DIR = Path(__file__).parent.absolute()
        save_path = CUR_DIR / '../config/customer.json'
        if(Path(CUR_DIR / '../config/customer.json') == True):
            ptf = open(save_path)
            path = Path(ptf)
            if(path.is_file() == True):
                Path.unlink(ptf)
        with open(save_path, 'w') as json_file:
            json.dump(data, json_file)

    @staticmethod
    def export_product_data(data: dict):
        CUR_DIR = Path(__file__).parent.absolute()
        save_path = CUR_DIR / 'window/productDump.json'
        if(Path(CUR_DIR / 'window/productDump.json') == True):
            ptf = open(save_path)
            path = Path(ptf)
            if(path.is_file() == True):
                Path.unlink(ptf)
        with open(save_path, 'w') as json_file:
            json.dump(data, json_file)
    
    """
    imports the contents of the customer.json file
    returns an empty dict if its not found
    """
    @staticmethod
    def import_data():
        try:
            CUR_DIR = Path(__file__).parent.absolute()
            file_path = open(CUR_DIR / '../config/customer.json')
            data = json.load(file_path)
            file_path.close()
            return data
        except FileNotFoundError as fnf_error:
            Utils.logger('error', "File not found | " + fnf_error)
            return {}
        except Exception as error:
            Utils.logger('warn', error)
            return {}
        
    @staticmethod
    def import_product_data():
        try:
            CUR_DIR = Path(__file__).parent.absolute()
            file_path = open(CUR_DIR / 'window/productDump.json')
            data = json.load(file_path)
            file_path.close()
            return data
        except FileNotFoundError as fnf_error:
            Utils.logger('error', "File not found | " + fnf_error)
            return {}
        except Exception as error:
            Utils.logger('warn', error)
            return {}
    
    """
    returns the contents of the api.json file
    returns an Empty dict if its not found
    """
    @staticmethod
    def get_api_config(key: str=""):
        try:
            if(key == ""):
                raise Exception("Undefined key: None")
            CUR_DIR = Path(__file__).parent.absolute()
            config = open(CUR_DIR / '../config/api.json')
            config_data = json.load(config)
            config.close()
            return config_data[key]
        except Exception as error:
            Utils.logger('warn', error)
            return {}
