import unittest
import sys, os
from pathlib import Path

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../../src/api'))

from sageone import *
from utils import *

class SageOneTest(unittest.TestCase):
    def test_get(self):
        api_config = Utils.get_api_config("sageOne")

        if(api_config == {}):
            self.assertEqual([], SageOne.GET())
        else:
            if("sage_product" in api_config):
                amount_products = len(api_config["sage_product"])
                self.assertEqual(len(SageOne.GET()), amount_products)
            else:
                self.assertEqual(SageOne.GET(), [])
    
    def test_create_params(self):
        api_config = Utils.get_api_config("sageOne")
        if(api_config == {}):
            self.assertEqual({}, SageOne.create_params(api_config))
        else:
            self.assertEqual(
                api_config["authentication"]["companyID"],
                SageOne.create_params(api_config)["companyid"]
            )

    def test_encode(self):
        api_config = Utils.get_api_config("sageOne")
        if(api_config == {}):
            self.assertEqual("", SageOne.encode_credentials(api_config))
        else:
            self.assertEqual(
                'aW5mb0Bnb21lZGlhLmNvLnphOmp1ai1tYXNoLXllVi0x',
                SageOne.encode_credentials(api_config)
            )

if __name__ == "__main__":
    unittest.main()