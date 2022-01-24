import datetime
import re

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
