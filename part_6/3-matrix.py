# write your solution here

def matrix_sum():
    sums = 0
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            each_row = parts[0:]
            for items in each_row:
                sums += int(items)
    return sums

def matrix_max():
    largest = 0
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            each_row = parts[0:]
            for items in each_row:
                if int(items) > largest:
                    largest = int(items)
    return largest

def row_sums():
    row_totals = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            int_parts = [int(item) for item in parts]
            sums = sum(int_parts)
            row_totals.append(sums)
    return row_totals
            

if __name__ == "__main__":
    #print(matrix_sum())
    #print(matrix_max())
    row_sums()