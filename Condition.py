#we will see the if else comdition

a=1330
b=1331

if a > b:
    print("a is greater than b")
elif a == b:
    print("a is same as b values")
else:
    print("b is bigger than a")

print("A") if a > b else print(" = ") if a==b else print("B")


#pass parameter is used as a null operation just as placeholder we use it .

if b > a:
   pass
else:
    print(a)

age = 16

if age < 18:
    pass  # TODO: Add underage logic later
else:
  print("Access granted")
