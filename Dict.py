#Dictionary is a collection where element are ordered , changeable and no duplicate are allowed but it is stored in 
#key value pair format

dicts={"name":"rohit","role":"captain","record":"3 ODI Hundred"}
print(dicts)
print(type(dicts))
print(len(dicts))

#we can also use dict constructor
thisdict = dict(name = "captain", age = 36, country = "mumbai")
print(thisdict)

print(dicts["name"])
print(dicts.get("record"))

#to get all the keys
k=dicts.keys()
print("Keys ", k)

#to get all the values as well
v=dicts.values()
print("Values ",v)

#items() method will return ecan key/value pair as tuple in a list
lt=dicts.items()
print(lt)


for x in dicts:
    print(x,end=" ")
