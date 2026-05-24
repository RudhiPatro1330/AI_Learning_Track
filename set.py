#set where item in the collection are unordered , unchangeable and no duplicate are allowed

sets={"apple","banana","mango","apple"}  # duplicate element will be automatically removed from it
print(sets)
print(type(sets))
print(len(sets))

#we use set construction to create set collection
sets_1=set({"BMW","JAGUAR","AUDI"})
print(sets_1)

#we can add items
sets.add("watermelon")
print(sets)

#to add items from another set to ur current set we use update method
sets.update(sets_1)
print(sets)

#to remove any item we use reomve()/discard we mostly use discard as it will not throw any error if the item is not present in the set.
sets.discard("apple")  #specified item
sets.pop()   #random items from it i.e set
print(sets)

#but in frozenset it is an immutable set that we cannot add or remove items once created
f=frozenset({"apple"})
#f.add("mango") we can't able to perform this
print(f)