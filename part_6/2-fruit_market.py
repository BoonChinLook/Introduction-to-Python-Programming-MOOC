# write your solution here
def read_fruits() -> dict:
    with open("fruits.csv") as new_file:
        my_dict = {}
        for line in new_file:
            split = line.split(";")
            my_dict[split[0]] = float(split[1])
    return my_dict

if __name__ == "__main__":
    print(read_fruits())