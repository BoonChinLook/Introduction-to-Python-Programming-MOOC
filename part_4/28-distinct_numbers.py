# Write your solution here

def distinct_numbers(list1: list):
    newlist = []
    for items in list1:
        if items not in newlist:
            newlist.append(items)
    return sorted(newlist)
    

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]
