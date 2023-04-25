import unittest
import sys, os
from pathlib import Path

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../src/database'))

from dbUtils import *

class UtilsTests(unittest.TestCase):
    def test_db_query(self):
        result = None
        try:
            result = DbUtils.queryDb("SELECT SKU AS 'Code' FROM inventory WHERE SKU='GenImp-V-AA' LIMIT 1")
        except Exception as error:
            print(error)
        self.assertEqual(result["query_data"][0][0], "GenImp-V-AA")

if __name__ == "__main__":
    unittest.main()