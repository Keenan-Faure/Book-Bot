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
            payment = BankPayment(20003.5, bank)
        else:
            payment = CashPayment(20003.5, "firstName lastName")
        customer = Customer("firstName", "lastName", address, payment)

        #products
        product_one = prod("GenImp-V-AA", "Ballad in Goblets - Venti", 2, 1500.0, "Stock2Shop")
        product_two = prod("GenImp-C-EP", "Cyno", 1, 1350.5, "Internal")
        if(reset == True):
            groceryList = GroceryList()
            groceryList.reset_list()
            groceryList.add_product(product_one)
            groceryList.add_product(product_two)
        else:
            groceryList = GroceryList()
            groceryList.add_product(product_one)
            groceryList.add_product(product_two)

        return GroceryOrder(customer, groceryList)
    
    def test_constructor(self):
        groceryOrder = GroceryListTest.init_class(True)
        self.assertEqual(groceryOrder.get_customer().get_address().get_address1(), "1st street")
        self.assertEqual(groceryOrder.get_customer().get_payment_method().get_amount(), 20003.5)
        self.assertEqual(len(groceryOrder.get_grocery_list().get_grocery_list()), 2)

        groceryOrder = GroceryListTest.init_class()
        self.assertEqual(groceryOrder.get_customer().get_address().get_address1(), "1st street")
        self.assertEqual(groceryOrder.get_customer().get_payment_method().get_amount(), 20003.5)
        self.assertEqual(len(groceryOrder.get_grocery_list().get_grocery_list()), 2)
    
    def test_order_confirm(self):
        groceryOrder = GroceryListTest.init_class()
        list = [
            prod("GenImp-C-EP", "Cyno", 10, 1350.5, "Internal"),
            prod("GenImp-V-AA", "Ballad in Goblets - Venti", 5, 1500.0, "Stock2Shop")
        ]
        
        result = groceryOrder.orderConfirm(list)
        self.assertEqual(2, len(result[0]))
        self.assertEqual(4350, result[1])
        
if __name__ == "__main__":
    unittest.main()