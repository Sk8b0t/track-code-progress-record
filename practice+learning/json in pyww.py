import json
with open("learnJson.json","r") as f:
    data=json.load(f)
for det in data["emp details"]:
    print(det)
#json.load(takes string objects) and json.loads(takes file ovject)
data2={
     "sayan":"biswas",
     "val":["vandel","phantom"],
     "fridge":("roti",696),
     "bool value":True
 }
print(json.dumps(data2,indent=4,sort_keys=True))

with open("newfile.json","w") as f:
    f.write(json.dumps(data2,indent=4,sort_keys=False))
    
#indent-> for spacing stuff
#sort_keys-> for alphabetically sorting the keys
