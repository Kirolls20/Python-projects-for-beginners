import json
from difflib import get_close_matches

# Opening The Json file and read it 
with open(r'G:\project\us_dict\dict.json', 'r') as f:
    data = json.load(f)

# Function to get the difinition of any word from json file by "Key" and "value"
def get_meaning(word):
    count = 0
    if word in data:
        if len(data[word]) > 1:
            for i in data[word]:
                count += 1
                print(f'{count}-{i}')
        else:
            print(data[word][0])
    else:
        # Using this method to give us list of similler words that match the given word if not exists.
        close_matches = get_close_matches(word, data.keys())
        print('the word is not exactly right !!')
        print(f'Close Matches  \n {close_matches}')


word = input("Enter a Word ?").lower()
get_meaning(word)
