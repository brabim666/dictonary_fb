'''

Facebook Email Bruter v3.1
Developers: Ñasir Ali (Tiger6117)

'''
import os
import re

class Color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print('''
       __               _                 _    
      / _|             | |               | |   
     | |_ __ _  ___ ___| |__   ___   ___ | | __
     |  _/ _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /
     | || (_| | (_|  __/ |_) | (_) | (_) |   < 
     |_| \__,_|\___\___|_.__/ \___/ \___/|_|\_\\
                Email Bruter By the_late_brabim

''')


def close_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)


import os
import re

def validation(user_input, FOR):
    if FOR == 'email':
        pattern = r"^[^@]+@[^@]+\.[^@]+$"
        return bool(re.match(pattern, user_input))
    elif FOR == 'file':
        pattern = r"\.txt$"
        return bool(re.search(pattern, user_input))

try:
    user_email = input("Enter email: ").lower()

    if validation(user_email, 'email'):
        emails_list = input("Provide emails' list: ")

        if validation(emails_list, 'file'):
            with open(emails_list, "r") as file:
                emails = set(file.read().split('\n'))

            check = 0
            with open("Found.txt", "a") as f:
                for email in emails:
                    email = email.lower().replace(" ", "")
                    if len(user_email) == len(email):
                        email_ = email.split("@")
                        user_email_ = user_email.split("@")
                        if user_email_[1] == email_[1]:
                            if user_email_[0][0] == email_[0][0] and user_email_[0][-1] == email_[0][-1]:
                                feed = "{} --> {}\n".format(user_email, email)
                                f.write(feed)
                                check = 1
                                
            if check:
                with open("Found.txt", "r") as data:
                    emails = data.read().split('\n')
                    print("Total email(s) found: {}".format(len(emails) - 1))
                    print("You can check email(s) in Found.txt")
            else:
                if os.path.exists("Found.txt"):
                    os.remove("Found.txt")
                print("Email not found in the email(s) list :(")
                input(".")
				
        else:
            print("Invalid emails file (use .txt file only)")
    else:
        print("Invalid email!!!")
        exit(1)

except Exception as e:
    print('Error:', e)
