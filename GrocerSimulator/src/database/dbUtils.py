import mysql.connector
import sys, os
from pathlib import Path

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../../src'))
from utils import *

class DbUtils:

    @staticmethod
    def init_conn(noDb: bool=True):
        result = None
        try:
            if(noDb == True):
                mydb = mysql.connector.connect(
                    user=Utils.readConfig("username"),
                    password=Utils.readConfig("password"),
                    host=Utils.readConfig("host")
                )
            else:
                mydb = mysql.connector.connect(
                    user=Utils.readConfig("username"),
                    password=Utils.readConfig("password"),
                    database=Utils.readConfig("database"),
                    host=Utils.readConfig("host")
                )
            result = mydb
        except Exception as error:
            print(error)
        return result

    @staticmethod
    def queryDb(mysql_connection: mysql.connector, query: str):
        result = {}
        mysql_conn = DbUtils.init_conn(False)
        if(mysql_conn != None):
            cursor = mysql_conn.cursor()
            cursor.execute(query)
            result["query_data"] = []
            for data in cursor:
                result["query_data"].append(data)
        return result

    @staticmethod
    def init_internal():
        #check if there exists mysql (connection)
        mysql_conn = DbUtils.init_conn()
        db_exists = False
        if(mysql_conn != None):
            #check if database exists
            databases = DbUtils.queryDb(mysql_conn, "show databases")
            for i in range(len(databases["query_data"])):
                if('dbclover' == (databases["query_data"][i][0]).lower()):
                    db_exists = True

        #check if products exist already (count)
        mysql_conn_db = DbUtils.init_conn(True)
        product_count = DbUtils.queryDb(mysql_conn_db, "SELECT COUNT(*) FROM inventory")
        print(product_count["query_data"][0][0])

DbUtils.init_internal()