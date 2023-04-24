import mysql.connector
import sys, os
from pathlib import Path

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../../src'))
from utils import *

class dbUtils:

    @staticmethod
    def queryDb(query: str):
        try:
            mydb = mysql.connector.connect(
                user=Utils.readConfig("username"),
                password=Utils.readConfig("password"),
                database=Utils.readConfig("database"),
                host=Utils.readConfig("host")
            )
            cursor = mydb.cursor()
            cursor.execute(query)
            for data in cursor:
                print(data)
        except Exception as error:
            print(error)