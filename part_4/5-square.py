# Copy here code of line function from previous exercise
def line(length, text):
    if text == "":
        print("*"*length)
    else:
        print(text[0]*length)

def square(size, character):
    # You should call function line here with proper parameters
    char = 0
    while char < size:
        line(size, character)
        char += 1
   

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")