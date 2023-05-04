import mysql.connector
import sys, os
from pathlib import Path

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../../src'))
from utils import *
from product import *

class DbUtils:
    """
    Creates a mysql connection to the mysql-server
    """
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
            Utils.logger("warning", error)
        return result

    """
    Runs the `query` against the database/mysql server
    """
    @staticmethod
    def queryDb(mysql_connection: mysql.connector, query: str):
        result = {}
        if(mysql_connection != None):
            cursor = mysql_connection.cursor()
            cursor.execute(query)
            if("insert into" in query.lower()):
                mysql_connection.commit()
            result["query_data"] = []
            for data in cursor:
                result["query_data"].append(data)
        return result
    
    """
    checks if the `inventory` table is defined
    inside the database, if not it creates it
    """
    @staticmethod
    def checkInventory(mysql_connection: mysql.connector):
        table_exist = False
        tables = DbUtils.queryDb(mysql_connection, "show tables")
        for i in range(len(tables["query_data"])):
            if('inventory' == (tables["query_data"][i][0]).lower()):
                table_exist = True
                break
        if(table_exist == False):
            DbUtils.queryDb(
                mysql_connection,
                "CREATE table inventory(Code varchar(255),"
                "Title varchar(255),"
                "Price varchar(255),"
                "Quantity varchar(255))"
            )
    
    @staticmethod
    def checkDatabase(mysql_connection: mysql.connector):
        db_exists = False
        if(mysql_connection != None):
            databases = DbUtils.queryDb(mysql_connection, "show databases")
            for i in range(len(databases["query_data"])):
                if('dbgrocery' == (databases["query_data"][i][0]).lower()):
                    db_exists = True
                    break
            if(db_exists == False):
                DbUtils.queryDb(mysql_connection, "CREATE DATABASE dbGrocery")
                db_exists = True
        else:
            Utils.logger("warning", "Unable to load Internal Products")
        return db_exists

    """
    Inserts products into database
    if database does not exist it creates it
    if products do not exist it 
    """
    @staticmethod
    def init_internal():
        mysql_conn = DbUtils.init_conn()
        db_exists = DbUtils.checkDatabase(mysql_conn)
        if(db_exists == True):
            mysql_conn_db = DbUtils.init_conn(False)
            DbUtils.checkInventory(mysql_conn_db)
            DbUtils.queryDb(mysql_conn_db, "SELECT COUNT(*) FROM inventory")

            product_count = DbUtils.queryDb(mysql_conn_db, "SELECT COUNT(*) FROM inventory")
            count = product_count["query_data"][0][0]
            if(count != 5):
                DbUtils.queryDb(mysql_conn_db,"DELETE FROM inventory")
                DbUtils.queryDb(
                    mysql_conn_db,
                    "INSERT INTO inventory(Code, Title, Price, Quantity)"
                    "values('GenImp-V-AA','Ballad in Goblets - Venti','1170','0'),"
                    "('GenImp-A-GC','Onis Royale - Arataki Itto','779.9','10'),"
                    "('GenImp-S-CP','The Transcendent One Returns - Shenhe','1759.9','2'),"
                    "('GenImp-RedHornStone','Redhorn Stonethresher','1050.0','4'),"
                    "('GenImp-K-AS','Leaves in the Wind - Kaedehara Kazuya','3400.9','10')")
                Utils.logger('info', 'Successfully created internal products')
            else:
                Utils.logger('info', 'Internal products loaded successfully')
        else:
            Utils.logger('error', 'Uncaught error | Please follow prerequisites')

    @staticmethod
    def GET():
        product_data = []
        try:
            DbUtils.init_internal()
            conn = DbUtils.init_conn(False)
            results = DbUtils.queryDb(conn, "SELECT * FROM inventory LIMIT 15")
            for product in results["query_data"]:
                system_product = Product(str(product[0]),
                                            str(product[1]),
                                            (product[3]),
                                            (product[2]),
                                            "MySQL Shoppers")
                product_data.append(system_product)
        except Exception as error:
            Utils.logger('error', error)
        return product_data