# Write your solution here
def all_the_longest(list1: list):
    longest = list1[0]
    result = []
    for items in list1:
        if len(longest) < len(items):
            longest = items
    result.append(longest)
    
    for long in list1:
        if len(longest) == len(long) and long not in result:
            result.append(long)
    return result

if __name__ == "__main__":

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']