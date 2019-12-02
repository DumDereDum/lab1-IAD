from sql import *

def addUser(connection, cursor):
    print("Do you really want to add new user?\n\t1. Yes\n\t2. No")
    ans = input("Your answer: ")
    while True:
        if ans == '2':
            return

        elif ans == '1':
            print("Input name, pls \n"
                  "Example: 'Artem'")
            name = input("Name: ")
            while name.isdigit() or name[0].isdigit():
                print("Incorrect answer!\n"
                      "Reply phone number again, pls")
                name = input("Name: ")

            print("Input surname, pls \n"
                  "Example: 'Saratovtsev'")
            surname = input("Surname: ")
            while surname.isdigit() or surname[0].isdigit():
                print("Incorrect answer!\n"
                      "Reply phone number again, pls")
                surname = input("Surname: ")

            name, surname = name.capitalize(), surname.capitalize()

            print("Input phone number, pls \n"
                  "Example: '88005553535'")
            phoneNum = input("Phone number: ")
            while not 10<len(phoneNum)<12 \
                    and (phoneNum[0] != '8' or phoneNum[:2] != '+7'):
                print("Incorrect answer!\n"
                      "Reply phone number again, pls")
                phoneNum = input("Phone number: ")
            if len(phoneNum)==12 and phoneNum[0:2]=='+7':
                phoneNum = '8'+phoneNum[2:]

            print("Do you want to enter the birth date?\n\t1. Yes\n\t2. No")
            answer = input("Your answer: ")
            if answer=='1':
                print("Input the birth date, pls \n"
                      "Example: '01.09.2000'")
                data = input("Birth date: ")
                while not checkData(data):
                    print("Incorrect answer!\n"
                          "Reply birth date again, pls")
                    data = input("Birth date: ")
                d, m, y = int(data[0:2]), int(data[3:5]), int(data[6:10])
                birth = datetime.date(y, m, d)
            else:
                birth = None

            if find(cursor, name=name, surname=surname):
                print("This user already exists")
            else:
                user = (name, surname, phoneNum, birth)
                insertUser(connection, cursor, user)

            print("Do you want to add new User? \n\t1. Yes\n\t2. No")
            answer = input("Your answer: ")
            if answer == '2':
                return

        else:
            print("Incorrect answer!\n"
                  "Do you want to reply again?\n\t1. Yes\n\t2. No")
            ans = input("Your answer: ")

def findUser(connection, cursor):
    print("Do you really want to find user?\n\t1. Yes\n\t2. No")
    ans = input("Your answer: ")
    while True:
        if ans == '2':
            return

        elif ans == '1':
            print("Input name, pls\n"
                "Example: 'Artem'\n"
                "If you don't want to find by name - press Enter\n")
            name = input("Name: ")

            print("Input surname, pls\n"
                  "Example: 'Saratovtsev'\n"
                  "If you don't want to find by surname - press Enter\n")
            surname = input("Surname: ")
            name, surname = name.capitalize(), surname.capitalize()

            if not find(cursor, name=name, surname=surname):
                print("There is no such user")
            else:
                findAndPrint(cursor, name=name, surname=surname)

            print("Do you want to find another User? \n\t1. Yes\n\t2. No")
            answer = input("Your answer: ")
            if answer == '2':
                return

        else:
            print("Incorrect answer!\n"
                  "Do you want to reply again?\n\t1. Yes\n\t2. No")
            ans = input("Your answer: ")


def deleteUser(connection, cursor):
    print("Do you really want to delete user?\n\t1. Yes\n\t2. No")
    ans = input("Your answer: ")
    while True:
        if ans == '2':
            return

        elif ans == '1':
            print("Input name, pls\n"
                "Example: 'Artem'")
            name = input("Name: ")

            print("Input surname, pls\n"
                  "Example: 'Saratovtsev'")
            surname = input("Surname: ")
            name, surname = name.capitalize(), surname.capitalize()

            if not find(cursor, name=name, surname=surname):
                print("There is no such user")
            else:
                Name = (name, surname)
                deleteUserByName(connection, cursor, Name)

            print("Do you want to delete another User? \n\t1. Yes\n\t2. No")
            answer = input("Your answer: ")
            if answer == '2':
                return

        else:
            print("Incorrect answer!\n"
                  "Do you want to reply again?\n\t1. Yes\n\t2. No")
            ans = input("Your answer: ")


def getAgeUser(cursor):
    print("Do you really want to get age of user?\n\t1. Yes\n\t2. No")
    ans = input("Your answer: ")
    while True:
        if ans == '2':
            return

        elif ans == '1':
            print("Input name, pls\n"
                  "Example: 'Artem'\n"
                  "If you don't want to find by name - press Enter")
            name = input("Name: ")

            print("Input surname, pls\n"
                  "Example: 'Saratovtsev'\n"
                  "If you don't want to find by surname - press Enter")
            surname = input("Surname: ")
            name, surname = name.capitalize(), surname.capitalize()

            if not find(cursor, name=name, surname=surname):
                print("There is no such user")
            else:
                age = getAge(cursor, name=name, surname=surname)
                if age:
                    print("Age of this user is", age, "years old")
                else:
                    print("This user did not provide his date of birth")

            print("Do you want to find another User? \n\t1. Yes\n\t2. No")
            answer = input("Your answer: ")
            if answer == '2':
                return

        else:
            print("Incorrect answer!\n"
                  "Do you want to reply again?\n\t1. Yes\n\t2. No")
            ans = input("Your answer: ")


def changeRecord(connection, cursor):
    print("Do you really want to change a record?\n\t1. Yes\n\t2. No")
    ans = input("Your answer: ")
    while True:
        if ans == '2':
            return

        elif ans == '1':
            print("Input name, pls\n"
                  "Example: 'Artem'")
            name = input("Name: ")

            print("Input surname, pls\n"
                  "Example: 'Saratovtsev'")
            surname = input("Surname: ")
            name, surname = name.capitalize(), surname.capitalize()

            if not find(cursor, name=name, surname=surname):
                print("There is no such user")
            else:
                print("What do you want to change:\n\t"
                      "1. Name\n\t"
                      "2. Surname\n\t"
                      "3. Phone number\n\t"
                      "4. Birth date")
                ans1 = input("Your answer: ")

                if ans1 == '1': changeName(connection, cursor, name, surname)
                if ans1 == '2': changeSurname(connection, cursor, name, surname)
                if ans1 == '3': changePhone(connection, cursor, name, surname)
                if ans1 == '4': changeBirth(connection, cursor, name, surname)

            print("Do you want to change? \n\t1. Yes\n\t2. No")
            answer = input("Your answer: ")
            if answer == '2':
                return

        else:
            print("Incorrect answer!\n"
                  "Do you want to reply again?\n\t1. Yes\n\t2. No")
            ans = input("Your answer: ")
