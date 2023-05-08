import unittest
import sys, os
from pathlib import Path

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../../src/api'))

from wooCom import *
from utils import *

class WooCommerceTest(unittest.TestCase):
    def test_get(self):
        api_config = Utils.get_api_config("wooCom")

        if(api_config == {}):
            self.assertEqual([], WooCommerce.GET())
        else:
            if("woo_product" in api_config):
                #Products not found with mess the count
                #TODO Try to find way to count the blank products as well
                amount_products = len(api_config["woo_product"])
                self.assertEqual(len(WooCommerce.GET()), amount_products)
            else:
                self.assertEqual(WooCommerce.GET(), [])
    
    def test_create_params(self):
        api_config = Utils.get_api_config("wooCom")
        if(api_config == {}):
            self.assertEqual({}, WooCommerce.create_params('testSKU'))
        else:
            self.assertEqual(
                "testSKU",
                (WooCommerce.create_params('testSKU'))["filter[sku]"]
            )

    def test_encode(self):
        api_config = Utils.get_api_config("wooCom")
        if(api_config == {}):
            self.assertEqual("", WooCommerce.encode_credentials(api_config))
        else:
            self.assertEqual(
                'Y2tfOTVjZGYzZDhiOTZiZWI2ODJlYWE4ZmRhYzE4ZDljMGMxOTc3NTFlNTpjc182'
                'MzEwNWE1YzlkODZjNDU3MmM0NTQyYzEyMzNmNTU5Nzc4M2IxMmJi',
                WooCommerce.encode_credentials(api_config)
            )

if __name__ == "__main__":
    unittest.main()