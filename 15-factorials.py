# Write your solution here

def factorials(n: int):
    my_dict = {}
    for i in range(1, n+1):
        if i == 1:
            my_dict[i] = i
        else:
            my_dict[i] = my_dict[i-1]*i
    return my_dict


if __name__ == "__main__":
    k = factorials(5)
    print(k)
    print(k[1])
    print(k[3])
    print(k[5])