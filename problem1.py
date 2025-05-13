#write a python program to get any file with extension to display onlu that file extension
# import os

# file = input("Enter a file with extention : ")

# file_name, file_extention = os.path.splitext(file)

# print("File name is",file_name)

# print("Extention is",file_extention

#write a python program to check extention of a file , if file extension is ".mp3" then display a message. "This file is not allowed"

import os

file = input("Enter a file with extention : ")

file_name, file_extention = os.path.splitext(file)

print("File name is",file_name)

print("Extention is",file_extention)


if file_extention == ".mp3":
    print("This file is not allowed!")
    