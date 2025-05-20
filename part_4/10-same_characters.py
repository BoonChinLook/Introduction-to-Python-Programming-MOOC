# Write your solution here
def same_chars(string, num1, num2):
    if num1 < len(string) and num2 < len(string):
        if string[num1] == string[num2]:
            return True
        return False
    return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("programmer", 6, 7))
    print(same_chars("programmer", 0, 4))
    print(same_chars("programmer", 0, 12))
    print(same_chars("abc", 0, 3) )