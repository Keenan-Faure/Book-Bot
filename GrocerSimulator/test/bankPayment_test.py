import unittest
import sys, os
from pathlib import Path

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../src'))

from bankPayment import *
from bank import *

class BankPaymentTest(unittest.TestCase):
    def test_constructor(self):
        bank = Bank(
            "TestBankName",
            "98728",
            "0810980987"
        )

        bankPayment = BankPayment(
            "1246.90",
            bank,
        )

        self.assertEqual(bankPayment.get_amount(), 1246.90)
        self.assertEqual(bankPayment.get_bank().get_name(), "TestBankName")
        self.assertEqual(bankPayment.get_bank().get_branch_id(), 98728)
        self.assertEqual(bankPayment.get_bank().get_telephone(), "0810980987")

        bankPayment.withdraw(1200.00)
        self.assertEqual(bankPayment.get_amount(), 46.90)

        try:
            bankPayment.withdraw(50)
        except Exception as error:
            print(error)

        bankPayment.deposit(1200)
        self.assertEqual(bankPayment.get_amount(), 1246.90)


        try:
            bankPayment.deposit(-2400)
        except Exception as error:
            print(error)

if __name__ == "__main__":
    unittest.main()