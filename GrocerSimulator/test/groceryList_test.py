import unittest
import sys, os
from pathlib import Path

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../src'))

from groceryList import *
from product import *

class GroceryListTest(unittest.TestCase):
    def test_constructor(self):
        product = Product("GenImp-V-AA", "Venti", 5, "1599.0", "SageOne")
        productNew = Product("GenImp-D-PC", "Diluc", 7, "1799.0", "Stock2Shop")
        groceryList = GroceryList([product])

        self.assertEqual([product], groceryList.get_grocery_list())

        groceryList.reset_list()
        self.assertEqual([], groceryList.get_grocery_list())

        groceryList.add_product(product)
        groceryList.add_product(productNew)
        self.assertEqual([product, productNew], groceryList.get_grocery_list())
        self.assertEqual(2, len(groceryList.get_grocery_list()))
        
if __name__ == "__main__":
    unittest.main()