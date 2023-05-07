import unittest
import sys, os
from pathlib import Path

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../src'))

from utils import *

class UtilsTests(unittest.TestCase):
    def test_is_int(self):
        numbers = [
            "False",
            False,
            "TruFalse",
            "I am a string"
            '=09',
            90.09,
            "672.123",
            "902.2",
        ]

        for number in numbers:
            self.assertEqual(
                False,
                Utils.isInt(number)
            )
        numbers = [
            "90",
            90,
            "82791",
            32380
        ]
        for number in numbers:
            self.assertEqual(
                True,
                Utils.isInt(number)
            )

    def test_read_config(self):
        keys = [
            "user",
            "keenan",
            "string",
            False
        ]
        for key in keys:
            self.assertEqual(
                '',
                Utils.readConfig(key)
            )

if __name__ == "__main__":
    unittest.main()