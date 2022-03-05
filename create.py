import databaseManager as dbManager
import datetime as dt


class Create:
    def func_CreateData(self):

        # Get the sql connection
        connection = dbManager.getConnection()
        cursor = connection.cursor()

        name = input("Name: ")
        age = int(input("Age: "))
        email = input("Email: ")

        try:
            sql = "INSERT INTO "+dbManager.table + \
                " (Name, Age, Email, created) VALUES (%s, %s, %s, %s)"
            values = (name, age, email, dt.datetime.today())

            # Execute the sql query
            cursor.execute(sql, values)

            # Commit the data
            connection.commit()
            print('Data Saved Successfully')

            userid = cursor.lastrowid
            #dbManager.idList.append(userid)
            # Close the cursor and the connection
            cursor.close()
            connection.close()

            print("Foi cadastrado o novo usuário de ID:", userid)

        except:
            print('Somethng wrong, please check')
