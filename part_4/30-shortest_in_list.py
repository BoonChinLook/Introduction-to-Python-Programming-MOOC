# Write your solution here

def shortest(list1: list):
    short = list1[0]
    for item in list1:
        if len(item) < len(short):
            short = item
    return short

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)