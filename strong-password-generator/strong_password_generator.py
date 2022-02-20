import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.punctuation)
s4 = list(string.digits)

user_input = input(
    'How many characters do you you want the password be ?(Only Number): ')

while True:
    try:
        user_input = int(user_input)
        if user_input < 6:
            print('The password must be 6 characters or above!!')
            user_input = input(
                'How many characters do you you want the password be ?(Only Number): ')
        else:
            break
    except:
        print('Must be Only Number!!')
        user_input = input(
            'How many characters do you you want the password be ?(Only Number): ')

# Shuffle all the characters
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

# s1 , s2 represent letters (upper and lower) ==> 60%
# s3 , s4 represent numbers and signs ==> 40%

part1= round(int(user_input) *30/100)
part2 = round(int(user_input) * 20/100)
# the generated password list 
password = []
for i in range(part1):
  password.append(s1[i] ) # 30% 
  password.append(s2[i]) # 30%


for x in range(part2):
  password.append(s3[x]) # 20%
  password.append(s4[x]) # 20%

generated_pass= " ".join(password)
print(generated_pass)


