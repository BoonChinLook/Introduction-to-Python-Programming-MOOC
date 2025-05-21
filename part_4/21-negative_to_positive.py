# Write your solution here
num = int(input("Please type in a positive integer: "))
for items in range(-num, num+1):
    if items == 0:
        continue
    print(items)
   