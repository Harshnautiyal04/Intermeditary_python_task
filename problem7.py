#write a python program to reverse a sub string from a string 


str = input("Enter string : ")

s = int(input("Enter a starting number : "))
e = int(input("Enter a ending number : "))
user_sub_s = str[s:e]

result = user_sub_s[::-1]

print(result)
