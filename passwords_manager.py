# View ALl the Accounts and Passwords 
from cryptography.fernet import Fernet

# View All The Account and Passwords Function
def view():
  with open('G:\project\passwords_manager\passwords.txt','r') as f :
    for line in f.readlines():
      data= line.rstrip()
      data= data.split("|")
      #print(data)
      user = data[0]
      passwd= data[-1]
      print(f"Account name : {user} , password: {passwd} ")

# Add New Accout and password
def add():
  account = input("Account Name? ")
  pwd = input('Account Password? ')
  # Open txt file and store the information in it
  with open('G:\project\passwords_manager\passwords.txt', 'a') as f:
    f.write(f"{account}|{pwd} \n ")
    print("The Accout is saved !!")
    

# master_user = admin123
master_user= input('Enter The master User password: ')
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


