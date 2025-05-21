# Write your solution here

my_list = []
item = 0
while True:
    print(f"The list is now {my_list}")
    user_input = input("a(d)d, (r)emove or e(x)it: ")
    if user_input == "d":
        item += 1
        my_list.append(item)
    elif user_input == "r":
        item -=1
        my_list.pop(item)
    elif user_input == "x":
        break
print("Bye!")
