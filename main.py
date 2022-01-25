import mysql.connector
from tabulate import tabulate
import hashlib
from validations import *
from update import update
mydb = mysql.connector.connect(host="localhost", user="root", passwd="manas", database="manas")

mycur = mydb.cursor()

def login():
    name = input("enter name* ")
    pswd = input("enter password ")
    converted_pswd = hashlib.md5(pswd.encode()).hexdigest()
    print(converted_pswd)#
    try:
        query = "select phone_no from register where name = '{}';".format(name)
        mycur.execute(query)
        myrecords = mycur.fetchall()
        print(myrecords[0])#
        phone_no = myrecords[0][0]
        query = "select password, isAdmin from login where login.phone='{}'".format(phone_no)
        mycur.execute(query)
        result_from_db = mycur.fetchall()
        pswd_from_db = result_from_db[0][0]
        isAdmin = result_from_db[0][1]
        print(pswd_from_db)
        print(isAdmin)
        if converted_pswd == pswd_from_db:
            print("{} is successfully loged In.".format(name))
            if isAdmin:
                update(name, True)
            else:
                update(name, False)
        else:
            print("Username or Password Invalid")
    except:
        print("User Don't Exist")
    #print(converted)

def showdetails():  ######Function calling is left
    mycur.execute("select name, email, phone_no, city, state, DOB from register ;")
    records = mycur.fetchall()
    print(tabulate(records, headers=["Username", "Email", "Phone Number", "City", "State", "DOB"],
                   tablefmt="grid"))  ##In Tabular format

def main():
    while 1:

        print("1.sign up")
        print("2.log in")
        print("3.show users")
        print("4.exit")

        x = int(input(""))

        if x==1:
            register()

        elif x==2:
            login()

        elif x== 3:
            showdetails()

        elif x==4:
            exit()



def register():

    # input data for respective fields

    name = input("enter name* ")
    while validate_name(name) != 1:
        name = input("enter name* ")
        validate_name(name)
    print(name)

    DOB = input("enter your date of birth in format YYYY-MM-DD* ")
    while validate_DOB(DOB) != 1:
        print("invalid dob enter/enter again")
        DOB = input("enter your date of birth in format YYYY-MM-DD: ")
        validate_DOB(DOB)
    print("dob entered successfully")
    print(DOB)

    Email = input("enter your email id* ")
    while validate_email(Email) != 1:
        Email = input("enter email id*: ")
        validate_email(Email)
    print(Email)

    phone_no = input("enter your phone number* ")
    while validate_phone(phone_no) != 1:
        phone_no = input("enter your phone number* ")
        validate_phone(phone_no)
    print(phone_no)

    pswd = input("enter password* ")
    while validate_password(pswd) != 1:
        pswd = input("enter password* ")
        validate_password(phone_no)
    print(pswd)

    city = "NULL"
    city = input("enter city ")
    print(city)

    state = "NULL"
    state = input("enter state ")
    print(state)

    phone_no = str(phone_no)
    #Store data
    query = "insert into register values('{}','{}','{}','{}','{}','{}') ;".format(name, DOB, Email, phone_no, city, state)
    mycur.execute(query)
    mydb.commit()

    converted = hashlib.md5(pswd.encode()).hexdigest()

    query = "insert into login values('{}','{}', '{}') ;".format(phone_no, converted, 0)
    mycur.execute(query)
    mydb.commit()

main()




