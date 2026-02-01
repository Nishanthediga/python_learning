marks={
  "nish":100,
  "yash":99,
  "prish":98,
  "nisch":97,
  # "yash":20,we add same key then old value will get overwrite
  # "prish":90
}
marks["nish"]=98
print(marks["nish"])
print(marks)

#methods of dictionary

nishanth={
  "name":"nishanth",
  "USN":"1MS23IS083",
  "age":20,
  "marks":[90,98,94,99,99], 
}
print(nishanth.items())# returns the list of tuples containig the key and value
print(nishanth.keys())#returns the list of keys
print(nishanth.values())#returns the list of values
nishanth.update({"age":21})
nishanth.update({"grade":"O"})
print(nishanth.get("name"))
print(nishanth.pop("age"))
print(nishanth)
