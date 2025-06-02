# Write your solution here

def invert(dictionary: dict):
    my_list = []
    for key, value in dictionary.items():
        my_list.append(value)
        my_list.append(key)
    dictionary.clear()
   
    for item in range(0, len(my_list), 2):
        dictionary[my_list[item]] = my_list[item+1]

if __name__ == "__main__": 
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)