# Write your solution here
def everything_reversed(list1: list):
    x = []
    new = list1[::-1]
    for items in new:
        items = items[::-1]
        x.append(items)
    return x

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
        