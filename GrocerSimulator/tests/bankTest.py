import unittest
import sys, os
from pathlib import Path

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../src'))

from bank import *

class BankTest(unittest.TestCase):
    def test_constructor(self):
        bank = Bank(
            "BankName",
            "10982",
            "0123456789"
        )
        self.assertEqual(bank.get_name(), "BankName")
        self.assertEqual(bank.get_branch_id(), 10982)
        self.assertEqual(bank.get_telephone(), "0123456789")

        bank = Bank(
            "bank_name_2"
        )
        self.assertEqual(bank.get_name(), "bank_name_2")
        self.assertEqual(bank.get_branch_id(), 99999)
        self.assertEqual(bank.get_telephone(), "")
        
if __name__ == "__main__":
    unittest.main()