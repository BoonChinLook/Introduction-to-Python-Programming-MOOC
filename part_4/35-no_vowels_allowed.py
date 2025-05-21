# Write your solution 

def no_vowels(string: str):  
    new_string = string
    vowels = ["a", "e", "i", "o", "u"] 
    for items in vowels:
            new_string = new_string.replace(items, "")
    return new_string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))