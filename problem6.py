# write a python program into get a new email from the user and make sure that it is email in proper format having @ symbol and .

import re


email = input("Enter a email : ")

pattern = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w{2,3}$'

x = re.match(pattern,email)

if x:
    print("Email is valid")
else:
    print("Email is invalid")