import json
from difflib import get_close_matches


data = json.load(open("data.json"))

def tran(wod):
    wod=wod.lower()
    if wod in data:
        return data[wod]
    elif len(get_close_matches(wod, data.keys()))>0:
        wod2 = get_close_matches(wod, data.keys())[0]
        print("Did you mean "+wod2+" instad ")
        des = input("if yes enter y else n")
        if des == "y":
            return data[wod2]
        else:
            return "word does not exist"

    else:
        return ("word does not exist")

wod = input("Enter a word")
ot=tran(wod)

if type(ot)== list:
    for it in ot:
        print(it)
else:
        print(ot)


