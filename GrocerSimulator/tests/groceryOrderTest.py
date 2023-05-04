import unittest
import sys, os
from pathlib import Path

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../src'))

from groceryOrder import *
from customer import *
from product import Product as prod
from groceryList import *
from bankPayment import *
from cashPayment import *
from address import *
from bank import *

class GroceryListTest(unittest.TestCase):
    @staticmethod
    def init_class(cash=True, reset=True):
        address = Address(
            "1st street",
            "2nd street",
            "city",
            "0321",
            "country"
        )
        payment = None
        if(cash == False):
            bank = Bank("BankName", 45212, "0215478963")
            payment = BankPayment(203.5, bank)
        else:
            payment = CashPayment(203.5, "firstName lastName")
        customer = Customer("firstName", "lastName", address, payment)

        #products
        product_one = prod("GenImp-V-AA", "Ballad in Goblets - Venti", 5, 1500.0, "Stock2Shop")
        product_two = prod("GenImp-B-HC", "Barbara", 5, 1000.0, "Internal")
        product_three = prod("GenImp-SK-HC", "Sango", 5, 1699.0, "Internal")
        product_four = prod("GenImp-C-EP", "Cyno", 5, 1350.5, "Internal")
        if(reset == True):
            groceryList = GroceryList()
            groceryList.reset_list()
            groceryList.add_product(product_one)
            groceryList.add_product(product_two)
            groceryList.add_product(product_three)
            groceryList.add_product(product_four)
        else:
            groceryList = GroceryList()
            groceryList.add_product(product_one)
            groceryList.add_product(product_two)
            groceryList.add_product(product_three)
            groceryList.add_product(product_four)

        return GroceryOrder(customer, groceryList)
    
    def test_constructor(self):
        groceryOrder = GroceryListTest.init_class(True)
        self.assertEqual(groceryOrder.get_customer().get_address().get_address1(), "1st street")
        self.assertEqual(groceryOrder.get_customer().get_payment_method().get_amount(), 203.5)
        self.assertEqual(len(groceryOrder.get_grocery_list().get_grocery_list()), 4)

        groceryOrder = GroceryListTest.init_class()
        self.assertEqual(groceryOrder.get_customer().get_address().get_address1(), "1st street")
        self.assertEqual(groceryOrder.get_customer().get_payment_method().get_amount(), 203.5)
        self.assertEqual(len(groceryOrder.get_grocery_list().get_grocery_list()), 4)
    
    def test_order_confirm(self):
        groceryOrder = GroceryListTest.init_class()
        list = [prod("GenImp-C-EP", "Cyno", 1, 1350.5, "Internal")]
        
        result = groceryOrder.orderConfirm(list)
        self.assertEqual([], result[0])
        self.assertEqual(0, result[1])
        
if __name__ == "__main__":
    unittest.main()