# Write your solution here

def no_shouting(my_list: str):
    new_list = []
    for items in my_list:
        if items.isupper() == False:
            new_list.append(items)
    return new_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)