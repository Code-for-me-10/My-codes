# booleans
print(True)
print("True")

print(type(True))  # bool type
print(type("True")) # string type

print(5==5)
print(5==6)

# loops
# 1. if
x = 10
y = 5
if x%y == 0:
    print(True)
else:
    print(False)

# 2. while
number = 1
while number < 10:
    print(number)
    if number == 7:
      break
    number = number + 1

# incorporating else in while loop
print("---------------------------------------else loop-----------------------------------------------------")
number2 = 5
while number2 < 10:
    print(number2)
    number2 = number2 + 1
else:
    print("number is no longer less than 10")


Number3= (int(input("Enter your number")))
if Number3 == 0:
    print("zero")
elif Number3 == 1:
    print("one")
elif Number3 == 2:
    print("Two")
elif Number3 == 3:
    print("Three")
elif Number3 == 4:
    print("Four")
elif Number3 == 5:
    print("Five")
elif Number3 == 6:
    print("Six")
elif Number3 == 7:
    print("Seven")
elif Number3 == 8:
    print("Eight")
elif Number3 == 9:
    print("Nine")
elif Number3 == 10:
    print("Ten")
else:
    print("oops..! Check Your number.")