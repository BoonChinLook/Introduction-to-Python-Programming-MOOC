# Write your solution here

def histogram(string: str):
    my_dict = {}
    for letter in string:
        if letter not in my_dict:
            my_dict[letter] = []
        my_dict[letter].append("*")
    
    for key, value in my_dict.items():
        value = "".join(value)
        print(f"{key} {value}")


if __name__ == "__main__":
    histogram("abba")