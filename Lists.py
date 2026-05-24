list_value=["banana","apple","coconut","grapes","banana"] # list can have different values
print(list_value)
print(len(list_value))
print(type(list_value))

#we can use list() constructor to create list
list_const=list((1,"rudhi","amma"))
list_const.insert(2,"patro")
list_const.append("last item appended")
list_const.extend(list_value)   # we can extend this function to other iterbale object like tuple,dict etc.
print(list_const)
#list_value.clear()
print(list_const)
list_value.sort(reverse=True)
print(list_const[:])
print(list_value)
[print(x,end=" ") for x in list_value]