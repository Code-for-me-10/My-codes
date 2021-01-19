# functions
# syntax
# def function_name(argument):
#  (line telling a function what to do to produce a result)
#    return result

# def squared(x):
#   result = x**2
#   return result
# print(squared(2))
# print(squared(5))

def squared(x, y):
    result = x**2 + y**2
    return result
print(squared(2, 4))
print(squared(5, 3))

# New function
def born(country):
    return print("I am From " +country)

born(" India")
