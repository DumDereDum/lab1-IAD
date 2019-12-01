import sqlite3
import datetime


def makeTable(cursor):
    cursor.execute("""
            CREATE TABLE users (
                    id          INTEGER PRIMARY KEY,
                    name        TEXT,
                    surname     TEXT,
                    phoneNum    TEXT,
                    birthdate   INTEGER )
        """)


def insertUser(connection, cursor, user):
    query = "INSERT INTO users (name, surname, phoneNum, birthdate) VALUES (?, ?, ?, ?)"
    cursor.execute(query, user)
    connection.commit()


def deleteUserByName(connection, cursor, name):
    query = 'DELETE FROM users WHERE  name = ? AND surname = ?'
    cursor.execute(query, name)
    connection.commit()


def deleteUserByPhone(connection, cursor, phone):
    query = 'DELETE FROM users WHERE  phoneNum = ?'
    cursor.execute(query, phone)
    connection.commit()


def deleteAllUsers(connection, cursor):
    query = 'DELETE FROM users;'
    cursor.execute(query)
    connection.commit()


def printAllUsers(cursor):
    query = 'SELECT * FROM users'
    table = cursor.execute(query)
    i=0
    for row in table:
        i+=1
        for x in row:
            print(x, end=" ")
        print()
    if i==0:
        print("The list is empty")


def findAndPrint(cursor, name='%%', surname='%%'):
    query = 'SELECT * FROM users WHERE name LIKE ? AND surname LIKE ?'
    user = ('%'+name+'%', '%'+surname+'%')
    table = cursor.execute(query, user)
    for row in table:
        print(row)


def find(cursor, name='%%', surname='%%'):
    query = 'SELECT * FROM users WHERE name LIKE ? AND surname LIKE ?'
    user = ('%'+name+'%', '%'+surname+'%')
    table = cursor.execute(query, user)
    i = 0
    for row in table:
        i+=1
    if i>0:
        return True
    return False


def changeName(connection, cursor, name, surname):
    print("Input name, pls \n"
          "Example: 'Artem'")
    newname = input("Name: ")
    while newname.isdigit() or name[0].isdigit():
        print("Incorrect answer!\n"
              "Reply phone number again, pls")
        newname = input("Name: ")
    query = "UPDATE users SET name = ? WHERE name = ? AND surname = ?"
    smth = (newname, name, surname)
    cursor.execute(query, smth)
    connection.commit()


def changeSurname(connection, cursor, name, surname):
    print("Input surname, pls \n"
          "Example: 'Saratovtsev'")
    newSurname = input("Surname: ")
    while newSurname.isdigit() or newSurname[0].isdigit():
        print("Incorrect answer!\n"
              "Reply phone number again, pls")
        newSurname = input("Surname: ")
    query = "UPDATE users SET surname = ? WHERE name = ? AND surname = ?"
    smth = (newSurname, name, surname)
    cursor.execute(query, smth)
    connection.commit()


def changePhone(connection, cursor, name, surname):
    print("Input phone number, pls \n"
          "Example: '88005553535'")
    phoneNum = input("Phone number: ")
    while not 10 < len(phoneNum) < 12 \
            and (phoneNum[0] != '8' or phoneNum[:2] != '+7'):
        print("Incorrect answer!\n"
              "Reply phone number again, pls")
        phoneNum = input("Phone number: ")
    if len(phoneNum) == 12 and phoneNum[0:2] == '+7':
        phoneNum = '8' + phoneNum[2:]
    query = "UPDATE users SET phoneNum = ? WHERE name = ? AND surname = ?"
    smth = (phoneNum, name, surname)
    cursor.execute(query, smth)
    connection.commit()


def changeBirth(connection, cursor, name, surname):
    print("Input the birth date, pls \n"
          "Example: '01.09.2000'")
    data = input("Birth date: ")
    while not checkData(data):
        print("Incorrect answer!\n"
              "Reply birth date again, pls")
        data = input("Birth date: ")
    d, m, y = int(data[0:2]), int(data[3:5]), int(data[6:10])
    birth = datetime.date(y, m, d)
    query = "UPDATE users SET birthdate = ? WHERE name = ? AND surname = ?"
    smth = (birth, name, surname)
    cursor.execute(query, smth)
    connection.commit()

def getAge(cursor, name='%%', surname='%%'):
    query = 'SELECT * FROM users WHERE name LIKE ? AND surname LIKE ?'
    user = ('%' + name + '%', '%' + surname + '%')
    user1 = cursor.execute(query, user)
    date = list(user1)[0][4]
    if date == None:
        return
    y, m, d = int(date[0:4]), int(date[6:7]), int(date[9:10])
    t1 = datetime.datetime(y, m, d)
    t2 = datetime.datetime.now()
    delta = (t2-t1)
    return delta.total_seconds()//31536000


def checkData(date):
    d, m, y = int(date[0:2]), int(date[3:5]), int(date[6:10])
    try:
        datetime.date(y, m, d)
        return True
    except:
        return False


def isThereTable(curcor):
    try:
        query = 'SELECT * FROM users'
        cursor.execute(query)
        return True
    except:
        return False


#def isThereTable(cursor, tableName):
#    query = " SELECT count(*) FROM sqlite_master WHERE type='table' AND name=? "
#    tableName = (tableName,)
#    res = cursor.execute(query, tableName)
#    if res:
#        return True
#    return False


if __name__ == '__main__':

    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    print(connection)

    printAllUsers(cursor)

    #getAge(cursor, name='Artem', surname="Sara")
    user = ('Artem', "Sar1")
    changeResord(connection, cursor, user)
    print()
    printAllUsers(cursor)
    #name = "Artem"
    #surname = "Saratovtsev"
    #phone = "+79632317965"
    #b = "01.09.2000"

    #print(b[0:2], b[3:5], b[6:10])
    #aa, bb, cc = int(b[0:2]), int(b[3:5]), int(b[6:10])
    ##aa = 80
    #if checkData(cc, bb, aa):
    #    birth = datetime.date(cc, bb, aa)
    #    print(birth)
    #else:
    #    print("Uncorrent data")


    #print(1)
    #printAllUsers(cursor)
    #for i in range(5):
    #    user = (name+str(i), surname, phone, birth)
    #    insertUser(cursor, user)
    #user = (name, surname, '+79632319999', birth)
    #insertUser(cursor, user)
    #printAllUsers(cursor)
    #print(2)
    #user = (name+"2", surname)
    #user = ("*", surname)
    #deleteUserByName(cursor, user)
    #printAllUsers(cursor)
    #print(3)
    #phone = ('+79632319999', )
    ##user = ("*", surname)
    #deleteUserByPhone(cursor, phone)
    #printAllUsers(cursor)
    #print(4)
    #name = '0'
    #find(cursor, name=name)

    #print(5)
    #deleteAllUsers(cursor)
    #printAllUsers(cursor)

