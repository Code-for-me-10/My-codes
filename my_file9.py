# tuples

fruits = ("apple", 4, "bananas", 5, "guava", 12, "oranges", 10)
List_of_fruits  = ["apple", 4, "bananas", 5, "guava", 12, "oranges", 10]

print(type(fruits))
print(type(List_of_fruits))

# we can modify elemnts in list. We can't modify elements in tuples!
List_of_fruits[0] = "Mango"
print(List_of_fruits)

# we can perform operations in tuples lie in lists
# slicing

print(fruits[1:6])
print(fruits[0:4])

# recallling

print(fruits[6])

# concatenation of tuples
fruits = fruits[0:4] + ("cherries", 10 )
print(fruits)

# lent of tuple
print(len(fruits))
print(List_of_fruits)

# converting tuples to list
fruits = list(fruits)
fruits.append("mangoes")
fruits = tuple(fruits)
print(fruits)


# un packing of tuples
Fruit = ("mangoes", "bananas", "cherries", "papaya", "strawberries", "Apples", "Watermelon")
print(len(Fruit))
(one, two, three, four, five , six, seven) =  Fruit
print(one)
print(two)
print(three)

for i in range(len(Fruit)):
    print(Fruit[i])