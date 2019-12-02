from menu import *
import os.path

file = "data.db"
if not os.path.exists(file):
    connection = sqlite3.connect(file)
    cursor = connection.cursor()
    makeTable(cursor)
else:
    connection = sqlite3.connect(file)
    cursor = connection.cursor()

ans=-1
while ans!=0:
    print("\nPlease choose the number of the desired operation:\n"
          "1. Show all records\n"
          "2. Add new record to the phonebook\n"
          "3. Find a record\n"
          "4. Get age of user\n"
          "5. Change a record\n"
          "6. Delete a record\n"
          "7. Delete all records\n"
          "0. Exit")
    ans = int(input("Answer: "))

    if ans == 0: break
    elif ans == 1: printAllUsers(cursor)
    elif ans == 2: addUser(connection, cursor)
    elif ans == 3: findUser(connection, cursor)
    elif ans == 4: getAgeUser(cursor)
    elif ans == 5: changeRecord(connection, cursor)
    elif ans == 6: deleteUser(connection, cursor)
    elif ans == 7: deleteAllUsers(connection, cursor)
