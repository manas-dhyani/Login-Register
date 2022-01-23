import datetime
import mysql.connector
from tabulate import tabulate
import hashlib
import re

mydb = mysql.connector.connect(host="localhost", user="root", passwd="manas", database="manas")

mycur = mydb.cursor()

def login():
    name = input("enter name* ")
    pswd = input("enter password ")
    converted_pswd = hashlib.md5(pswd.encode()).hexdigest()
    #print(converted_pswd)
    try:
        """
        The function compare the encrypted version of pswd from Login DB and entered user pswd to Login User.
        """
        query = "select phone_no from register where name = '{}';".format(name)
        mycur.execute(query)
        myrecords = mycur.fetchall()
        #print(myrecords[0][0])
        phone_no = myrecords[0][0]
        query = "select password from register, login where login.phone='{}'".format(phone_no)
        mycur.execute(query)
        pswd_from_db = mycur.fetchall()
        pswd_from_db = pswd_from_db[0][0]
        print(pswd_from_db)#
        if converted_pswd == pswd_from_db:
            print("{} is successfully loged In.".format(name))
        else:
            print("Username or Password Invalid")
    except:
        print("User Don't Exist")
    #print(converted)


def showdetails():  ######Function calling is left
    mycur.execute("select name, email, phone_no, city, state from register ;")
    records = mycur.fetchall()
    print(tabulate(records, headers=["Username", "Email", "State", "City", "Phone Number"],
                   tablefmt="grid"))  ##In Tabular format


def updating_username():
    u_old = input(" Old Username")
    u_new = input(" New Username")
    q = "update register set username=%s where username=%s ;"
    mycur.execute(q, (u_new, u_old,))
    mydb.commit()
    print("Details Successfully Updated")
    login()


def updating_password():
    p_old = input(" Old Password")
    p_new = input(" New Password")
    cp_new = input(" Confirm Password")
    q = "update login set pwd=%s where pwd=%s ;"
    mycur.execute(q, (p_new, p_old,))
    mydb.commit()
    q1 = "update login set cpwd=%s where cpwd=%s ;"
    mycur.execute(q1, (cp_new, p_old,))
    mydb.commit()
    print("Details Successfully Updated")
    login()
def updating_email():
    e_old = input("Old Email")
    e_new = input("New Email")
    q = "update register set email=%s where email=%s ;"
    mycur.execute(q, (e_new, e_old,))
    mydb.commit()
    print("Details Successfully Updated")
    login()
def updating_city():
    c_old = input("Old City")
    c_new = input("New City")
    q = "update register set city=%s where city=%s ;"
    mycur.execute(q, (c_new, c_old,))
    mydb.commit()
    print("Details Successfully Updated")
    login()
def updating_state():
    s_old = input("Old State")
    s_new = input("New State")
    q = "update register set state%s where state=%s ;"
    mycur.execute(q, (s_new, s_old,))
    mydb.commit()
    print("Details Successfully Updated")
    login()


def updating_phone():
    p_old = int(input("Old Phone Number"))
    p_new = int(input("New Phone Number"))
    q = "update register set phn=%s where phn=%s ;"
    mycur.execute(q, (p_new, p_old,))
    mydb.commit()
    print("Details Successfully Updated")
    login()






def updatingvalues():  #####Function calling is left
        c = 'y'
        while c == 'y':
            print("Which Details do you want to update?")
            print("1. Username")
            #print("2. Password")
            print("3. Email")
            print("4. City")
            print("5. State")
            print("6. Phone Number")
            print("7. Exit")
            ch = int(input("Enter Your Choice-"))
            if ch == 1:
                updating_username()
            #elif ch == 2:
                #updating_passwd()
            elif ch == 3:
                updating_email()
            elif ch == 4:
                updating_city()
            elif ch == 5:
                updating_state()
            elif ch == 6:
                updating_phone()
            elif ch == 7:
                login()
            else:
                break
            c = input("Do You Want To Continue?")




def main():
    while 1:

        print("1.sign up")
        print("2.log in")
        print("3.show users")
        print("4.update details")
        print("5.exit")

        x = int(input(""))

        if x==1:
            register()

        elif x==2:
            login()

        elif x== 3:
            showdetails()

        elif x==4:
            updatingvalues()


        elif x==5:
            exit()

#validation of respective fields

def validate_name(name):
    if len(name) < 5:
        print("your username is short by", 5 - len(name))
        print("re-enter your username again")
        return 0
    else:
        return 1

def validate_DOB(dob):
    """
    The below function datetime.datetime.strptime(dob, '%Y-%m-%d')
    will return string if executed correctly which will make
    if statement True
    """
    try:
        if datetime.datetime.strptime(dob, '%Y-%m-%d'):
            return 1
    except:
        return 0


"""
To understand the code, you need to understand what is the meaning of "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$".
^ means to match the starting of the string, i.e. here it tells the interpreter that the sequence that follows ^ is the format based on which it has to decide which email is valid and which is not.
[...] means to match a set of characters, and [a-z0-9] means to find a sequence/combination of characters that contains characters from small 'a' to small 'z' and numbers from 0 to 9. + means to match 1 or more repetitions. Hence, [a-z0-9]+ means to match all the combinations of small 'a' to small 'z' and numbers from 0 to 9, repeating one or more than one time.
[\._] means to match '.' (dot) and ? means to find 0 or 1 repetitions. Since we don't allow more than one consecutive dot in an email address so [\._]? means it has to match zero or one occurrence of a dot.
We have another [a-z0-9]+ so as to find another combination of small 'a' to small 'z' and numbers from 0 to 9 repeating one or more than one time, which may or may not be a successor of a dot.
[@] means to match @, and \w means to match any alphanumeric character, i.e. [@]\w+ means to match @ followed by any alphanumeric character, repeating one or more than one time
[.]\w{2,3} means to match dot followed by any alphanumeric combination of characters of length 2 or 3. This is used to match the domain names which are of length 2 and 3. If you want to check custom domain names so you can replace this with \w+.
$ means to match the end of the string, i.e. $ means to mark the end of validation sequence.
"""

def validate_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        print("Valid Email")
        return 1
    else:
        print("Invalid Email")
        return 0


def validate_phone(phone):
    regex = '^(\+90[\-\s]?)?[0]?(91)?[789]\d{9}$'
    if(re.search(regex, phone)):
        print("Valid phone no.")
        return 1
    else:
        print("Invalid phone no.")
        return 0

def _password(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(passwd) < 6:
        print('length should be at least 6')
        val = False

    if len(passwd) > 20:
        print('length should be not be greater than 8')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val

def validate_password(pswd):
    """
    Conditions for a valid password are:

        Should have at least one number.
        Should have at least one uppercase and one lowercase character.
        Should have at least one special symbol.
        Should be between 6 to 20 characters long.
    """
    if (_password(pswd)):
        print("Password is valid")
        return 1
    else:
        print("Invalid Password !!Re-enter")
        return 0


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

    query = "insert into login values('{}','{}') ;".format(phone_no, converted)
    mycur.execute(query)
    mydb.commit()

main()




