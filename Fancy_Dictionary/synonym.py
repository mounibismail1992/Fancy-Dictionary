import json
from difflib import get_close_matches
data = json.load(open("dictionary.json"))
def translate(w):
    w = w.upper() #Converts everything to uppercase
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:    #match with similar in case of mispelling
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])#ask if similar word is one needed
        if (yn =="Y") or (yn=="y"):
            return data[get_close_matches(w, data.keys())[0]] #print similar word
        elif (yn == "N") or (yn=='n'):
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
word = input("Enter word: ")
output = translate(word)
print(output)
