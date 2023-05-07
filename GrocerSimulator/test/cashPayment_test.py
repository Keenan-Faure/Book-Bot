import unittest
import sys, os
from pathlib import Path

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../src'))

from cashPayment import *

class CashPaymentTest(unittest.TestCase):
    def test_constructor(self):
        cash = CashPayment(
            "1500",
            "First LastName"
        )
        self.assertEqual(cash.get_amount(), 1500.00)
        self.assertEqual(cash.get_cash_owner(), "First LastName")

        cash.withdraw(200)
        self.assertEqual(cash.get_amount(), 1300.00)

        try:
            cash.withdraw(1700.00)
        except Exception as error:
            print(error)
        
        self.assertEqual(cash.get_amount(), 1300.00)

        cash.deposit(1500.00)
        self.assertEqual(cash.get_amount(), 2800.00)

        cash = CashPayment(
            1399.00
        )
        self.assertEqual(cash.get_amount(), 1399.00)
        self.assertEqual(cash.get_cash_owner(), "")
        
if __name__ == "__main__":
    unittest.main()