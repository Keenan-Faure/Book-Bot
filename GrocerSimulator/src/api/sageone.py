import requests
from requests.exceptions import HTTPError
from pathlib import Path
import base64
import sys, os

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../../src'))

from product import *
from utils import *

class SageOne:
    
    @staticmethod
    def GET():
        product_data = []
        try:
            config_data = Utils.get_api_config("sageOne")
            product_ids = config_data["sage_product"]
            for id in product_ids:
                if(config_data != {}):
                    url = 'https://accounting.sageone.co.za/api/2.0.0/item/Get/' + str(id)
                    headers = {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'Authorization': 'Basic ' + str(SageOne.encode_credentials(config_data))
                    }
                    params = SageOne.create_params(config_data)
                    if(params != {}):
                        response = requests.get(url, params=params, headers=headers)
                        response.raise_for_status()
                        sage_product = response.json()
                        if(sage_product == None):
                            raise Exception(f"Product with ID: {str(id)} not found in Sage One")
                        system_product = Product(str(sage_product["Code"]),
                                                 str(sage_product["Description"]),
                                                 (sage_product["QuantityOnHand"]),
                                                 (sage_product["PriceInclusive"]),
                                                 "Sage One Market")
                        product_data.append(system_product)
            return product_data
        except KeyError as key_error:
            print('Key Error: ' + str(key_error) + " does not exist")
            return product_data
        except HTTPError as http_err:
            print('HTTP Error: ' + str(http_err))
            return product_data
        except Exception as error:
            Utils.logger('error', str(error))
            return product_data

    @staticmethod
    def create_params(config: dict):
        if(config != {}):
            params = {
                "companyid": str(config["authentication"]["companyID"]),
                "includeAdditionalItemPrices": "false",
                "apikey": "{" + str(config['authentication']['apiKey']) + "}"
            }
            return params
        return {}

    @staticmethod
    def encode_credentials(config: dict):
        if(config != {}):
            credentials = str(config["authentication"]["username"]) + ":" + str(config["authentication"]["password"])
            credentials_bytes = credentials.encode("ascii")        
            base64_bytes = base64.b64encode(credentials_bytes)
            base64_string = base64_bytes.decode("ascii")
            return base64_string
        return ""
        