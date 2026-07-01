import json
with open("jsondata.json","r") as f:
   data=json.load(f)
for item in data:
   print(json.dumps(item,indent=4,sort_keys=True))