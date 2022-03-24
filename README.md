# Login-Register

As we know almost every site whether it is e-com, social-networking, tourism or 
e-booking each of them requires LOGIN AND REGISER interface to register 
his/her user or to login into his/her account. 
It is to authenticate it users to be able to protect their private content and give 
them personalized experience. <br />
For eg. in a chat app you would not want anyone Login is basically required for 
the application to identify which user is making the request and accordingly, 
serve related data to him/her. For example: When you login in Quora, your 
notifications are displayed, feeds are tailored according to your interests, etc.
Registration is the first step of identifying the user. <br />
To access your conversations with other users or get their hands on your private 
media, similarly, logging in a music or video streaming apps lets them 
understand your taste of music/video and recommend other items accordingly. <br />

# FUNCTIONS AND MODULES 
 **MODULES**
➢ import mysql.connecter:  <br />
By importing this package, we can establish the connection between SQL 
and Python.  <br />
➢ Import datetime <br />
This package provides basic functions for display date related values in the 
program.  <br />
➢ import random:  <br />
This package has functionality to generate random numbers and select 
numbers within a range.  <br />
➢ Import tabulate <br />
By importing this package, we are able to display details of table in sql in tabular 
form in output window of python. <br />
➢ Import re <br />
By importing this package, we can work with regex which supports regular
function. <br />
➢ Import haslib <br />
In haslib, md5 ( Merkle–Damgård) is a hash function accepts sequence of bytes
and returns 128 bit hash value. Next one is, encode() : Converts the string
into bytes to be acceptable by hash function. Lastly, hexdigest() : Returns the 
encoded data in hexadecimal format. <br />

# FUNCTIONS
➢ connect(): This function establishes connection between 
Python and MySQL. <br />
➢ cursor(): It is a special control structure that facilitates the 
row-by-row processing of records in the result set.  <br />
The syntax is: 
<cursorobject>=<connectionobject>.cursor() <br />
➢ execute(): This function is use to execute the sql query 
and retrieve records using python. <br />
  The syntax is: 
<cursor object>.execute(<sql query string>) <br />
➢ fetchall():This function will return all the rows from the 
result set in the form of a tuple containing the records.  <br />
➢ commit(): This function provides changes in the 
database physically.  <br />
 
 The Image below shows the use-case diagram for the project.
  
![](Readme%20Images/main.JPG)
  
There are 2 tables in the project with phone_no as the Primary Key (PK).
 
![](Readme%20Images/tables.JPG)
  
The Description of table Register. All user data except password is saved here, phone_no as Primary Key.
  
![](Readme%20Images/register%20desc.JPG)
 
The Description of table Login. The user pswd is saved using md5 encryption and phone_no when user register/sign_up.
 
![](Readme%20Images/Login.JPG)    

When user try to login, its pswd is encrypted by md5 encryption and compared to encrpted pswd stored in login table. The username is taken to search the phone no for the user and then a join query is used to find the user registered pswd in login table. If on comparison they are same the user is loged in successfully.
  
![](Readme%20Images/reglogin.JPG)  
  
  
