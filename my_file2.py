# list
My_list = [1,2,3,4,56,67]

my_list2 = list(range(1,7))
print(My_list)
print(my_list2)

my_list3 = list(range(1, 50, 10))
# it will increment each time with diff of 10

print(my_list3)
# operations on list :
# this will return the fifth element
print(my_list2[4])

print(my_list2[-2])
# lets create a slice from the second element to the 4th element
print(my_list2[2:5])

# range of a list
print(len(my_list3))
# max number of list
print(max(My_list))
print(min(My_list))

# add element on to our list
My_list.append(38)
print(My_list)

# reversing our list
My_list.reverse()
print(My_list)

# create another list and add two list together
print(My_list + my_list2 + my_list3)
print(len(my_list3))

