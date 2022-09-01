from datetime import datetime
import getpass
import sys
import passsave

username = open('username.txt', 'r')
password = open('password.txt', 'r')

stu = username.read()
stp = password.read()

user_name = input("Enter User Name : ")

if user_name == stu:
    stu = username.close()
    pass_word = getpass.getpass('Enter Password : ',stream=sys.stderr)
    if pass_word == stp:
        stp = password.close()
        passsave.passave()
    else:
        print("Password Wrong")
else:
    print("Username not match")