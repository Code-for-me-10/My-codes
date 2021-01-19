# mini  project 2- generating random password

# add relevant modules

from random import randint
# all password is in uppercase

password = ""
for i in range(10):
    i = chr(randint(65, 90))
    password = str(password) + i
print(password)

# upper and lower case

password = ""
for i in range(10):
    i = chr(randint(65, 90))
    for j in range(10):
        j = chr(randint(65, 90)).lower()
    password = str(password) + i + j
print(password)
