# Write your solution here
def line(length, text):
    if text == "":
        print("*"*length)
    else:
        print(text[0]*length)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")