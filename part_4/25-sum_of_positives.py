# Write your solution here
def sum_of_positives(my_list):
    sum = 0
    for items in my_list:
        if items > 0:
            sum += items
    return sum


if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)