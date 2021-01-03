
# importing libaries
import json
from difflib import get_close_matches

# loading data
files=open("data.json")
data=json.load(files)



while True:
    # taking user input
    user_input = input("type the word you want to search(type 'x' if want to quit - ").lower()

    # close application
    if user_input == 'x':
        break

    if user_input in data.keys():
        print(data[user_input])
    else:
        # identify typo mistake pf user
        close_match=get_close_matches(user_input,data.keys())
        if close_match == []:
            print("Data not available. Please check the word or type new word")
        else:
            # taking input to get confirmation on close match
            a=input("Do you mean '"+close_match[0]+"' ? type y and n").lower()
            if a== 'y':
                print(data[close_match[0]])
            else:
                print("Cannot find. Please type another word")