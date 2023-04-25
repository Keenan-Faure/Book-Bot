import mysql.connector
import sys, os
from pathlib import Path
import datetime;

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../../src'))
from utils import *

class DbUtils:

    """
    Displays the `error`, `info`, `warning` type 
    `messages` along with the 
    message and `timestamp` on the console/terminal
    """
    @staticmethod
    def logger(status: str='info', message:str=""):
        if(status == "error"):
            print("Error | " + message + " | " + str(datetime.datetime.now()))
        elif(status == "warning"):
            print("Warn | " + message + " | " + str(datetime.datetime.now()))
        elif(status == "info"):
            print("Info | " + message + " | " + str(datetime.datetime.now()))

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
            DbUtils.logger("warning", error)
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
            if("insert into" in query):
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

    """
    Inserts products into database
    if database does not exist it creates it
    if products do not exist it 
    """
    @staticmethod
    def init_internal():
        mysql_conn = DbUtils.init_conn()
        db_exists = False
        if(mysql_conn != None):
            databases = DbUtils.queryDb(mysql_conn, "show databases")
            for i in range(len(databases["query_data"])):
                if('dbclover' == (databases["query_data"][i][0]).lower()):
                    db_exists = True
                    break
            if(db_exists == False):
                DbUtils.queryDb(mysql_conn, "CREATE DATABASE dbClover")
        
        else:
            DbUtils.logger("warning", "Unable to load Internal Products")

        if(db_exists == True):
            mysql_conn_db = DbUtils.init_conn(False)
            DbUtils.checkInventory(mysql_conn_db)
            DbUtils.queryDb(mysql_conn_db, "SELECT COUNT(*) FROM inventory")

            product_count = DbUtils.queryDb(mysql_conn_db, "SELECT COUNT(*) FROM inventory")
            count = product_count["query_data"][0][0]
            if(count != 15):
                DbUtils.queryDb(mysql_conn_db,"DELETE FROM INVENTORY")
                DbUtils.queryDb(
                    mysql_conn_db,
                    "INSERT INTO inventory(Code, Title, Price, Quantity)"
                    "values('GenImp-V-AA','Amos Bow','1170','0'),"
                    "('GenImp-Amos','Amos Bow','1170','2'),"
                    "('GenImp-SkywardAtlas','Skyward Atlas','1150','5'),"
                    "('GenImp-A-GC','Onis Royale - Arataki Itto','779.9','10'),"
                    "('GenImp-S-CP','The Transcendent One Returns - Shenhe','1759.9','2'),"
                    "('GenImp-RedHornStone','Redhorn Stonethresher','1050.0','4'),"
                    "('GenImp-MemoryDust','Memory of Dust','1350','0'),"
                    "('GenImp-KaguraVerity','Kaguras Verity	','2550.0','9'),"
                    "('GenImp-S-HC','Drifting Luminescence - Sangonomiya Kokomi','2350.5','2'),"
                    "('GenImp-R-EP','Reign of Serenity - Raiden Shogun','3559.0','0'),"
                    "('GenImp-ThunderingPulse','Thundering Pulse','1170.5','1'),"
                    "('GenImp-K-CS','The Herons Court - Kamisato Ayaka','1750.0','12'),"
                    "('GenImp-X-AP','Invitation to Mundane Life - Xiao','2150.0','0'),"
                    "('GenImp-H-PP','Moment of Bloom - Hu Tao','2600.5','5'),"
                    "('GenImp-K-AS','Leaves in the Wind - Kaedehara Kazuya','3400.9','10')")
                DbUtils.logger('info', 'Successfully created internal products')
            else:
                DbUtils.logger('info', 'Internal products loaded successfully')

DbUtils.init_internal()