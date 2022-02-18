# View ALl the Accounts and Passwords
from cryptography.fernet import Fernet

# create crypted key file

'''
def write_key():
    key = Fernet.generate_key()
    with open('G:\project\passwords_manager\key.key', 'wb') as key_file:
        key_file.write(key)

write_key()
'''
def load_key():
    file = open("G:\project\passwords_manager\key.key",'rb')
    key= file.read()
    file.close()
    return key

key= load_key()
fer= Fernet(key)

# View All The Account and Passwords Function
def view():
    with open('G:\project\passwords_manager\passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            data = data.split("|")
            # print(data)
            user = data[0]
            passwd = data[-1]
            try:
                print(f"Account name : {user} , password: {fer.decrypt(passwd.encode()).decode()}")
            except:
                print('Passwords are decrypted successfully')
# Add New Accout and password


def add():
    account = input("Account Name? ")
    pwd = input('Account Password? ')
    if len(pwd) < 4 :
        print('Password is not Secure Enough please make sure to add strong password! ')
    else:
        # Open txt file and store the information in it
        with open('G:\project\passwords_manager\passwords.txt', 'a') as f:
            f.write(f"{account}|{fer.encrypt(pwd.encode()).decode()} \n ")
            print("The Accout is saved !!")


# master_user = admin123
master_user = input('Enter The master User password: ')
if master_user == 'admin123':
    while True:
        choices = input(
            "What mode do you want add or view password (add-view or q if you want to exit) ?")

        if choices == 'q':
            break

        if choices == 'add':
            add()

        elif choices == 'view':
            view()
        else:
            print('Invaild Mode !')
            continue

else:
    print("Invaild Password!! ")
