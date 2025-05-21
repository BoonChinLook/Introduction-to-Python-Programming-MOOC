# Write your solution here
num = int(input("How many items: "))
index = 0
my_list = []
while num > 0:
    index += 1
    item = int(input(f"Item {index}: "))
    my_list.append(item)
    num -= 1

print(my_list)

