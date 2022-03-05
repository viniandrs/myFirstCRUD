# Singleton to manage the connection to the database and
# store data to change some settings of the database in the future
import mysql.connector

host = "localhost"
user = "db_user"
password = "Pass*1234"
database = "MyFirstDatabase"
table = "Employees"

#idList = []

def getConnection():
    return mysql.connector.connect(host="localhost",
                                    user="db_user",
                                    password="Pass*1234",
                                    database="MyFirstDatabase")
