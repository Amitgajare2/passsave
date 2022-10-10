from datetime import datetime
import json
import os

# ---------------------------- SAVE PASSWORD ------------------------------- #
def saved_entries():

    # GETTING THE USER INPUTS
    user_website = input("Enter website name : ")
    user_email = input("Enter email : ")
    user_name = input("Enter username : ")
    user_password = input("Enter password : ")

    new_data = {
        user_website: {
            'email': user_email,
            'username': user_name,
            'password': user_password
            }
        }
    if len(user_website) != 0 and len(user_password) != 0:

        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open('data.json','w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            is_correct = 'add successful'
            if is_correct:
                with open('data.json','w') as data_file:
                    json.dump(data, data_file, indent=4)
    else:
        # IF WEBSITE OR EMAIL ENTRY IS BLANK
        print("Please Enter Right Information")
# ---------------------------- UPDATE ------------------------------- #
def write_json(date, filename="data.json"):
    with open(filename,"w") as f:
        json.dump(date, f, indent=4)

# ---------------------------- COLOR ------------------------------- #
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
    # return print(clo)

#os.system("cls")
os.system('clear')
name = colored(64,224,208, "@amitgajare_")
banner = colored(255,105,180, f'''
█▀█ ▄▀█ █▀ █▀ █▀ ▄▀█ █ █ █▀▀
█▀▀ █▀█ ▄█ ▄█ ▄█ █▀█ ▀▄▀ ██▄
{name}\t\tV1.0''')

listoption = colored(100,149,237, '''
1. Add New Password
2. Search Password
3. Update Details
4. Exit
''')

print(banner)

i=1
while i:
    print(listoption)
    select_option = input(colored(255,255,0, "Select Option :- "))

    if select_option == '1':
        saved_entries()
    elif select_option == '2':
        # Opening JSON file
        with open('data.json') as json_file:
            data = json.load(json_file)
            webname = input("Enter Website Name :- ")
            print("\n",data[webname],"\n")
            json_file.close()

    elif select_option == '3':
        webkey = input("Enter Website Name :- ")
        with open("data.json") as json_file:
            data = json.load(json_file)
            temp = data[webkey]

            print("What do you want to change?\n1. Email\n2. Username\n3. Password\n4. All")
            select_key = input("Select Option :- ")
            if select_key=="1":
                up_email = input("Enter New Email :- ")
                y = {"email":up_email}
                temp.update(y)  
                json_file.close()
                write_json(data)
            elif select_key=="2":
                up_user = input("Enter New Username :- ")
                p = {"username":up_user}
                temp.update(p)  
                json_file.close()
                write_json(data)
            elif select_key=="3":
                up_pass = input("Enter New Password :- ")
                c = {"password":up_pass}
                temp.update(c)  
                json_file.close()
                write_json(data)
            elif select_key=="4":
                up_email = input("Enter New Email :- ")
                up_user = input("Enter New Username :- ")
                up_pass = input("Enter New Password :- ")
                kk = {
                "email":up_email,
                "username":up_user,
                "password":up_pass
                }
                temp.update(kk)  
                json_file.close()
                write_json(data)
            else:
                print("Please Select Right Option...")
                
    elif select_option == '4':
        exit()
    else:
        print("Please Enter Right Option...")
        
