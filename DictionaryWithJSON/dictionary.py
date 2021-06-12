#This is a program which tells you the meaning of the word you entered

import json
from difflib import get_close_matches   #This module is used to find the closest match of the word entered by the user

print("This a dictionary program written by @real_ashd\n")
#Loading the json file which contains the definitions of the words.
data = json.load(open("data.json"))

#Function to check if the word exist or not, if yes provide the definition
def mean(w):
    w = w.lower()           #Tackling with case sensitive nature of python
    if w in data:
        print("The definition of",w,"is:")
        return data[w]
    elif w.upper() in data:
        print("The definition of",w.upper(),"is:")
        return data[w.upper()]
    elif w.title() in data:
        print("The definition of",w.title(),"is:")
        return data[w.title()]
    elif len(get_close_matches(w,data.keys())) > 0:     #Checking the closest match of the word entered
        yn = input("Did you mean %s instead?\nEnter Y if yes or N if No: " % get_close_matches(w, data.keys())[0])
        if yn.lower() == 'y':
            print("The definition of",get_close_matches(w, data.keys())[0],"is:")
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.lower() == 'n':
            return "The word doesn\'t exist. Please double check it."
        else:
            return "Invalid input. Please try again."
    else:
        return "The word doesn\'t exist. Please double check it."

q='r'
while q!='q':
    word = input("Enter a word: ")
    output = mean(word)

    if type(output) != list:
        print(output)
    else:
        for item in output:
            print(item)
    print('------------------------------------------------------------------')
    q=input("\nEnter q to quit the program or press any other key to search another word : ")
    q=q.lower()
