import mysql.connector
from validations import *

mydb = mysql.connector.connect(host="localhost", user="root", passwd="manas", database="manas")
mycur = mydb.cursor()

def update(username, isAdmin):
    try:
        connection=mysql.connector.connect(host="localhost", user="root", passwd="manas", database="manas")
        sql_select_Query = "select * from register"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        if isAdmin:
            print("Total number of rows in table: ", cursor.rowcount)
            print()
            name = input("enter your name")
            for row in records:
                if row[0] == name:
                    x = row
                    print("Your current data is: ", row)
                    updatingvalues(x)
        else:
            for row in records:
                if row[0] == username:
                    x = row
                    print("Your current data is: ", row)
                    updatingvalues(x)

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)

    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("No such user Exist. Try different username.")
            print("MySQL connection is closed")


def updating_username(x):
    username = x[0]
    print("your current username is: ", username)
    phone = x[3]
    print("your phone no is: ", phone)
    username = input("enter name* ")
    while validate_name(username) != 1:
        username = input("enter name again* ")
        validate_name(username)
    print("your username will be updated to: ", username)
    mycur = mydb.cursor()
    val = (username, phone)

    sql = "UPDATE register SET name = %s WHERE phone_no= %s"

    mycur.execute(sql, val)
    mydb.commit()
    print("Details Successfully Updated")

def updating_phone(x):
    curr_phone = x[3]
    print("your current phone no is: ", curr_phone)
    new_phone = input("enter phone no* ")
    while validate_phone(new_phone) != 1:
        new_phone = input("enter phone again* ")
        validate_phone(new_phone)
    print("your phone no. will be updated to: ", new_phone)
    mycur = mydb.cursor()
    val = (new_phone, curr_phone)

    sql = "UPDATE register SET phone_no= %s WHERE phone_no= %s"
    mycur.execute(sql, val)
    mydb.commit()

    sql = "UPDATE login SET phone_no= %s WHERE phone_no= %s"
    mycur.execute(sql, val)
    mydb.commit()

def updating_email(x):
    email = x[2]
    print("your current email is: ", email)
    phone = x[3]
    print("your phone no is: ", phone)
    email = input("enter new  email* ")
    while validate_email(email) != 1:
        email = input("enter name again* ")
        validate_email(email)
    print("your email will be updated to: ", email)
    mycur = mydb.cursor()
    val = (email, phone)

    sql = "UPDATE register SET email= %s WHERE phone_no= %s"

    mycur.execute(sql, val)
    mydb.commit()


def updating_dob(x):
    phone = x[3]
    dob = x[1]
    print("your current dob is: ", dob)
    print("your phone no is: ", phone)
    dob = input("enter dob* ")
    while validate_DOB(dob) != 1:
        dob= input("enter dob again* ")
        validate_DOB(dob)
    print("your dob will be updated to: ", dob)
    mycur = mydb.cursor()
    val = (dob, phone)
    sql = "UPDATE register SET DOB= %s WHERE phone_no= %s"
    mycur.execute(sql, val)
    mydb.commit()

def updating_state(x):
    phone = x[3]
    state = x[5]
    print("your current city is: ", state)
    print("your phone no is: ", phone)
    state = input("enter new state ")
    print("your state will be updated to: ", state)
    mycur = mydb.cursor()
    val = (state, phone)
    sql = "UPDATE register SET state= %s WHERE phone_no= %s"
    mycur.execute(sql, val)
    mydb.commit()

def updating_city(x):
    phone = x[3]
    city = x[4]
    print("your current city is: ", city)
    print("your phone no is: ", phone)
    city = input("enter new state ")
    print("your city will be updated to: ", city)
    mycur = mydb.cursor()
    val = (city, phone)
    sql = "UPDATE register SET city= %s WHERE phone_no= %s"
    mycur.execute(sql, val)
    mydb.commit()

def updatingvalues(x):  #####Function calling is left
    c = 'y'
    while c == 'y':
        print("Which Details do you want to update?")
        print("1. Username")
        print("2. DOB")
        print("3. Email")
        print("4. City")
        print("5. State")
        print("6. Phone Number")
        print("7. Exit")
        ch = int(input("Enter Your Choice-"))
        if ch == 1:
            updating_username(x)
        elif ch == 2:
            updating_dob(x)
        elif ch == 3:
            updating_email(x)
        elif ch == 4:
            updating_city(x)
        elif ch == 5:
            updating_state(x)
        elif ch == 6:
            updating_phone(x)
        elif ch == 7:
            exit()
        else:
            break
        c = input("Do You Want To Continue? press y else n:")
