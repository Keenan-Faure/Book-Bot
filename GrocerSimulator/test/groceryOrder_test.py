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
    def init_class(cash=True, reset=True, emptyStore=False):
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
        if(emptyStore == False):
            if(reset == True):
                groceryList = GroceryList()
                groceryList.reset_list()
                groceryList.add_product(product_one)
                groceryList.add_product(product_two)
            else:
                groceryList = GroceryList()
                groceryList.add_product(product_one)
                groceryList.add_product(product_two)
        else:
            groceryList = GroceryList()

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
        #First Test Case
        #Populated grocery list & enough money
        groceryOrder = GroceryListTest.init_class()
        storeProducts = [
            prod("GenImp-C-EP", "Cyno", 10, 1350.5, "Internal"),
            prod("GenImp-V-AA", "Ballad in Goblets - Venti", 5, 1500.0, "Stock2Shop")
        ]
        
        result = groceryOrder.orderConfirm(storeProducts)
        self.assertEqual(2, len(result[0]))
        self.assertEqual(4350.5, result[1])

        #Second Test case
        #Empty Grocery List & enough money
        groceryOrder = GroceryListTest.init_class(False, True, True)

        storeProducts = [
            prod("GenImp-C-EP", "Cyno", 10, 1350.5, "Internal"),
            prod("GenImp-V-AA", "Ballad in Goblets - Venti", 5, 1500.0, "Stock2Shop")
        ]

        with self.assertRaises(Exception):
            groceryOrder.orderConfirm(storeProducts)

        #Third Test case
        #Empty Store (no products) & enough money
        groceryOrder = GroceryListTest.init_class(False, True)

        storeProducts = []

        with self.assertRaises(Exception):
            groceryOrder.orderConfirm(storeProducts)
    
    def test_in_stock(self):
        #First test case
        #Products in stock

        groceryOrder = GroceryListTest.init_class(False, True, False)
        storeProducts = [
            prod("GenImp-C-EP", "Cyno", 10, 1350.5, "Internal"),
            prod("GenImp-V-AA", "Ballad in Goblets - Venti", 5, 1500.0, "Stock2Shop")
        ]
        result = groceryOrder.in_stock(
            prod("GenImp-C-EP", "Cyno", 10, 1350.5, "Internal"),
            storeProducts
        )
        self.assertTrue(result)

        #Second Test Case
        #Product not in stock (orders more than available amount)

        groceryOrder = GroceryListTest.init_class(False, True, False)
        storeProducts = [
            prod("GenImp-C-EP", "Cyno", 10, 1350.5, "Internal"),
            prod("GenImp-V-AA", "Ballad in Goblets - Venti", 5, 1500.0, "Stock2Shop")
        ]
        with self.assertRaises(Exception):
            groceryOrder.in_stock(
            prod("GenImp-C-EP", "Cyno", 20, 1350.5, "Internal"),
            storeProducts)

        #Third Test Case
        #Product not in stock - orders 1 but 0 on hand

        groceryOrder = GroceryListTest.init_class(False, True, False)
        storeProducts = [
            prod("GenImp-C-EP", "Cyno", 0, 1350.5, "Internal"),
            prod("GenImp-V-AA", "Ballad in Goblets - Venti", 5, 1500.0, "Stock2Shop")
        ]
        with self.assertRaises(Exception):
            groceryOrder.in_stock(
            prod("GenImp-C-EP", "Cyno", 1, 1350.5, "Internal"),
            storeProducts
        )
    
    def test_deduct_cost(self):
        #First Test Case
        #Customer has enough money to buy single item
        groceryOrder = GroceryListTest.init_class(False, True, False)
        groceryOrder.deduct_cost(
            prod("GenImp-C-EP", "Cyno", 10, 1350.5, "Internal"),
            groceryOrder.get_customer()
        )
        self.assertNotEqual(groceryOrder.totalCost, 0)

        #Second Test Case
        #Customer does not have enough to buy x2 of item

        groceryOrder = GroceryListTest.init_class(False, True, False)

        with self.assertRaises(Exception):
            groceryOrder.deduct_cost(
            prod("GenImp-C-EP", "Cyno", 20, 1350.5, "Internal"),
            groceryOrder.get_customer()
        )
        self.assertEqual(groceryOrder.totalCost, 0)

        #Third Test Case
        #Customer buys 3 products - test final value

        groceryOrder = GroceryListTest.init_class(False, True, False)
        groceryOrder.deduct_cost(
            prod("GenImp-C-EP", "Cyno", 5, 1350.5, "Internal"),
            groceryOrder.get_customer()
        )
        groceryOrder.deduct_cost(
            prod("GenImp-C-EP", "Cyno", 5, 1350.5, "Internal"),
            groceryOrder.get_customer()
        )
        self.assertNotEqual(groceryOrder.totalCost, 6752.5)
    
    def test_remove_zero_qty(self):
        #First Test Case
        #Zero quantity product in the list
        groceryOrder = GroceryListTest.init_class(False, True, False)

        #adds additional product
        groceryOrder.get_grocery_list().add_product(
            prod("GenImp-D-PC", "Diluc", 0, 1750.5, "Stock2Shop")
        )
        groceryOrder.remove_zero_qty()

        self.assertNotEqual(
            len(groceryOrder.get_grocery_list().get_grocery_list()),
            3
        )

        #Second Test Case
        #No zero quantity products in the list

        groceryOrder = GroceryListTest.init_class(False, True, False)
        groceryOrder.remove_zero_qty()

        self.assertEqual(
            len(groceryOrder.get_grocery_list().get_grocery_list()),
            2
        )
        
if __name__ == "__main__":
    unittest.main()