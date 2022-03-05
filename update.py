import databaseManager as dbManager

class Update:
    def func_UpdateData(self):

        # Get the sql connection
        connection = dbManager.getConnection()
        cursor = connection.cursor()

        id = input("Id to be updated: ")

        sql = "SELECT * FROM "+dbManager.table+" WHERE Id = %s"
        cursor.execute(sql, [id])

        updating_row = cursor.fetchone()
        print("Data fetched for id: " + id +
              ":\n" + str(updating_row) + "\n")

        try:
            new_name = input("New name: ")
            new_age = input("New age: ")
            new_email = input("New email: ")

            sql = "UPDATE " + dbManager.table +\
                " SET name = %s, age = %s, email = %s WHERE id = %s"
            new_values = (new_name, new_age, new_email, id)
            cursor.execute(sql, new_values)

            connection.commit()
            print('Data Updated Successfully')

            cursor.close()
            connection.close()

        except:
            print('Something went wrong while updating, please check')
