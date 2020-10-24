#Python JSON

import json

print(dir(json))

x='{"Name":"Ganesh","Age":29,"City":"Partur"}'
print(x)
print(type(x))

#Convert JSON to python
y=json.loads(x)
print(y)
print(type(y))

print("\n")
#Convert python to JSON
di={"Name":"Mangesh","Age":25,"City":"Pune"}
print(di)
print(type(di))

y=json.dumps(di)
print(y)
print(type(y))

#Use "indent" parameter to make reading easier converted JSON String
print(json.dumps(di,indent=5))

#Order the results
print(json.dumps(di, indent=5,sort_keys=True))
