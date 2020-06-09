import analysiscode2

import json

with open('jsondict.json',"r") as json_file:
    jsondict = json.load(json_file)
    for p,y in jsondict.items():
        print(p ,end=" ")
        print(y)

        print()