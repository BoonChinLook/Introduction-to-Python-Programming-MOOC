# Write your solution here

def length_of_longest(list1: list):
    best = ""
    for word in list1:
        if len(word) > len(best):
            best = word
    return len(best)

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)