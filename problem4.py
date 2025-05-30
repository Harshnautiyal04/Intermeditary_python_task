# write a python program to store students records, user will be able to delete ant students from a record on run time

n = int(input("Enter number : "))

std_lst = []

for i in range(n):
    std_lst.append(input("Enter student name to store in a student list : "))


print(f"Student list = {std_lst}")

std_dlt = input("Enter student name to remove from a student list : ")

std_lst.remove(std_dlt)

print(f"Student list after removing the {std_dlt} from the list = {std_lst}")