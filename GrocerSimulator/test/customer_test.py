import unittest
import sys, os
from pathlib import Path

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../src'))

from customer import *
from address import *
from bankPayment import *
from cashPayment import *

class ProductTest(unittest.TestCase):
    def test_constructor(self):

        payment = CashPayment(
            "1500",
            "first_name last_name"
        )
        address = Address(
            "1st Streetname",
            "2nd Streetname",
            "city",
            "50",
            "CountrySouth"
        )

        #customer
        customer = Customer("first_name", "last_name", address, payment)
        self.assertEqual(customer.get_first_name(), "first_name")
        self.assertEqual(customer.get_last_name(), "last_name")

        #address
        self.assertEqual(customer.get_address().get_address1(), "1st Streetname")
        self.assertEqual(customer.get_address().get_address2(), "2nd Streetname")
        self.assertEqual(customer.get_address().get_city(), "city")
        self.assertEqual(customer.get_address().get_postalcode(), 50)
        self.assertEqual(customer.get_address().get_country(), "CountrySouth")

        #payment
        self.assertEqual(customer.get_payment_method().get_amount(), 1500)
        self.assertEqual(customer.get_payment_method().get_cash_owner(), "first_name last_name")
        
if __name__ == "__main__":
    unittest.main()