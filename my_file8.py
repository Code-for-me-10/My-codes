

a = 4
print("buzz", a%2==0)

# strings
# already we have covered strings, booleans, loops, lists
# int, float, booleans are considered to be simple data type
# they cannot be broken down!

print("hello, world!")
print(type("hello, world!"))

# operations on strings
# addition sign concatenation

Greetings = "hello"
name = " my name is Snehal !"
college = "Dayanand"
print(Greetings + name + college)

# * operator
print(name*3)
print((Greetings + name) * 4)



#  index operator
hello = "India"
print(hello[0])
print(hello[1])
print(hello[2])
print(hello[3])
print(hello[4])

# format string
My_name = input("Your name: ")
hello = "hello {}".format(My_name)
print(hello)


# case
Name2 = "snehal"
print(Name2.lower())
print(Name2.upper())

# replace letters

print(Name2.replace("s", "f"))

# each letter in python is assigned to specific number
# let's say
print("snehal" > "meghu")
print(ord("s"))
print(chr(77))


x = "snehal"
y = ""
for character in x:
    y = character.upper() + y
print(y)







