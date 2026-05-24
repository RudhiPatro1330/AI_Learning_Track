a=5   #in pyhton variable is created when we assign a value only then have not declare just like other programming language
b="rudhi"
import random

print(1+(random.randrange(1,10)))


c="""
Yes it work when the string literal is not assigned to a value.
"""
print(a,end="/")
print(b,c)

d=str(5)
print(type(d))

fruits=["apple",150,"banana"]
x,y,z=fruits
print(x," ",y," "," ",z)

salaar="prabhas"

for i in salaar:
    print(i,end=" ")

print(len(salaar))


ru="Donki Rudhi Narayan Patro"
li=ru.split(" ")
print(li)

age=23
print(f'"I am  ",ru," and my age is {age}"')
print(ru.count("a"))
print(bool(" "))

numbers=[1,2,3,4,5]
if (count := len(numbers)):
    print(f"the list has {count} element")