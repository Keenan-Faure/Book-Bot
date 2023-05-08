import requests
from requests.exceptions import HTTPError
from pathlib import Path
import base64
import sys, os

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../../src'))

from product import *
from utils import *

class WooCommerce:
    
    @staticmethod
    def GET():
        product_data = []
        try:
            config_data = Utils.get_api_config("wooCom")
            product_skus = config_data["woo_product"]
            for sku in product_skus:
                if(config_data != {}):
                    url = config_data["authentication"]["url"] + "/wc-api/v3/products"
                    headers = {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'Authorization': 'Basic ' + str(WooCommerce.encode_credentials(config_data))
                    }
                    params = WooCommerce.create_params(sku)
                    if(params != {}):
                        response = requests.get(url, params=params, headers=headers)
                        response.raise_for_status()
                        woo_product = response.json()
                        if(woo_product == None or woo_product["products"] == []):
                            Utils.logger("warn", f"Product with SKU: {str(sku)} not found on WooCommerce")
                            continue
                        else:
                            system_product = Product(str(woo_product["products"][0]["title"]),
                                                    str(woo_product["products"][0]["sku"]),
                                                    (woo_product["products"][0]["stock_quantity"]),
                                                    (woo_product["products"][0]["price"]),
                                                    "WooComm Market")
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
    def create_params(sku: str):
        if(sku != ""):
            params = {
                "filter[sku]": sku,
            }
            return params
        return {}
    
    @staticmethod
    def encode_credentials(config: dict):
        if(config != {}):
            credentials = str(config["authentication"]["api_key"]) + ":" + str(config["authentication"]["api_secret"])
            credentials_bytes = credentials.encode("ascii")        
            base64_bytes = base64.b64encode(credentials_bytes)
            base64_string = base64_bytes.decode("ascii")
            return base64_string
        else:
            return {}