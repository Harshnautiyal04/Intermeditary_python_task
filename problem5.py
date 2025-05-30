# write a python program to  updadte specific key in a dictionary

dict = {'Name' : 'harsh', 'Age' : 18 , 'City' :'Delhi'}

old_key = input("Enter a key you want to update : ")
new_key = input("Enter a new key : ")

dict[new_key] = dict[old_key]

del dict[old_key]

print(dict)