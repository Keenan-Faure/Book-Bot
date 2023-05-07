import unittest
import sys, os
from pathlib import Path

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../src'))

from product import *

class ProductTest(unittest.TestCase):
    def test_constructor(self):
        product = Product("GenImp", "Genshin Impact", 50, 55.0)
        self.assertEqual(product.get_code(), "GenImp")
        self.assertEqual(product.get_title(), "Genshin Impact")
        self.assertEqual(product.get_qty(), 50)
        self.assertEqual(product.get_price(), 55.0)
        self.assertEqual(product.get_vendor(), "")

        product = Product("SKU", "I am a title", "1500", "0", "Stock2Shop")
        self.assertEqual(product.get_code(), "SKU")
        self.assertEqual(product.get_title(), "I am a title")
        self.assertEqual(product.get_qty(), 1500)
        self.assertEqual(product.get_price(), 0.0)
        self.assertEqual(product.get_vendor(), "Stock2Shop")
        
if __name__ == "__main__":
    unittest.main()