import databaseManager as dbManager


class Delete:
    def func_DeleteData(self):

        # Get the sql connection
        connection = dbManager.getConnection()
        cursor = connection.cursor()

        id = input("Id to be deleted: ")

        sql = "SELECT * FROM "+dbManager.table+" WHERE Id = %s"
        cursor.execute(sql, [id])

        deleting_row = cursor.fetchone()
        print("Data fetched for id: " + id +
              ":\n" + str(deleting_row))

        try:
            key = input("Are you sure you want to delete "+deleting_row[1] +
                        "? \n1-Yes/2-No ")
            if key == '2':
                return
            
            sql = "Delete From "+dbManager.table+" Where Id = %s"
            cursor.execute(sql, [deleting_row[0]])

            connection.commit()
            print('Data deleted Successfully')

            cursor.close()
            connection.close()

        except:
            print('Something went wrong while deleting, please check')
