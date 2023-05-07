import unittest
import sys, os
from pathlib import Path

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../src'))

from address import *

class AddressTest(unittest.TestCase):
    def test_constructor(self):
        address = Address(
            "1st Streetname",
            "2nd Streetname",
            "city",
            "50",
            "CountrySouth"
        )
        self.assertEqual(address.get_address1(), "1st Streetname")
        self.assertEqual(address.get_address2(), "2nd Streetname")
        self.assertEqual(address.get_city(), "city")
        self.assertEqual(address.get_postalcode(), 50)
        self.assertEqual(address.get_country(), "CountrySouth")

        address = Address(
            "1st Streetname",
            "2nd Streetname"
        )
        self.assertEqual(address.get_address1(), "1st Streetname")
        self.assertEqual(address.get_address2(), "2nd Streetname")
        self.assertEqual(address.get_city(), "")
        self.assertEqual(address.get_postalcode(), 9999)
        self.assertEqual(address.get_country(), "")
        
if __name__ == "__main__":
    unittest.main()