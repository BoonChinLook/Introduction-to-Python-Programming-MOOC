# Write your solution here

def longest_series_of_neighbours(my_list: list):
    my_list.append(-1)
    length = 0
    seq = []
    for index in range(0, len(my_list)):
        after = index + 1
        seq.append(my_list[index])
        if after < len(my_list):
            if my_list[index] - 1 == my_list[after] or my_list[index] + 1 == my_list[after]:
                continue
            else:
                if len(seq) >= length:
                    length = len(seq)
                seq = []
    return length

    
            
if __name__ == "__main__":
    my_list = [1, 2, 3, 5, 6, 9, 10] #3
    print(longest_series_of_neighbours(my_list))
