# Write your solution here

def most_common_character(string: str):
    list1 = []
    new = []
    for items in string:
        count_item = string.count(items)
        list1.append(count_item)
    for items in string:
        if string.count(items) == max(list1) and items not in new:
            new.append(items)
    return '\n'.join(new)

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

  #  second_string = "exemplaryelementary"
   # print(most_common_character(second_string))
