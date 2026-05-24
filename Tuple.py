#tuple are collection type in which element can are in ordered,unchangeable and duplicate are allowed.
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

#creation of tuple with single element add comma with it otherwise it will be string
tuple_single_element=("apple",)
print(type(tuple_single_element))

tuples=("banana","apple","banana","mango")
print(tuples)
print(len(tuples))
print(type(tuples))

#access of element
print(tuples[1])
print(tuples[:-2])  # it exclude the last element i.e -1 element


#we can change the or update somehow like / same thing we can do for remove and del also
x=list(tuples)
x[0]="pineapple"
tuples=tuple(x)
print(tuples)


#unpacking a tuples
a,b,c,d=tuples
print("unpacking ",a," ",b, " ",c, " ",d)

a,*b=tuples
print("unpacking ",a ," ",b)


#Looping
for i in tuples:
    print(i,end=" ")

print()
print(tuples.count("banana"))
print(tuples.index("pineapple"))