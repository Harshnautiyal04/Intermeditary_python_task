# write a pyhton program to get password fromm the user that contain alpha numeric and nore than 8 and less than 20 characters


pwd = input("Enter password : ")

if pwd.isalnum() and 8 <= len(pwd) <=20:
    print(f"The password is {pwd}.")
else:
    print(f"Sorry,The password {pwd} is invalid the password criteria is not match!")