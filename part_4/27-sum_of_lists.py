# Write your solution here

def list_sum(list1: list, list2: list):
    sum = []
    for index in range(len(list1)):
        sums = list1[index] + list2[index]
        sum.append(sums)
    return sum


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]