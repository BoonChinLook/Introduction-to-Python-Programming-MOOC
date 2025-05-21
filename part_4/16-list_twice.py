# Write your solution here
my_items = []
while True:
    item = int(input("New item: "))
    if item == 0:
        print("Bye!")
        break    
    my_items.append(item)
    print(f"The list now: {my_items}")
    print(f"The list in order: {sorted(my_items)}")
