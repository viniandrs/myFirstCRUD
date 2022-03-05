import databaseManager as dbManager

class Read:
    def func_ReadData(self):

        # Get the sql connection
        connection = dbManager.getConnection()
        cursor = connection.cursor()

        sql = "SELECT * FROM "+dbManager.table
        cursor.execute(sql)

        results = cursor.fetchall()
        
        cursor.close()
        connection.close()

        for result in results:
            print(result)