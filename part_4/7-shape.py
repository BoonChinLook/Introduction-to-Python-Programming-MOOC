# Copy here code of line function from previous exercise
def line(length, text):
    if text == "":
        print("*"*length)
    else:
        print(text[0]*length)

def triangle(width, symbol):
    # You should call function line here with proper parameters
    counter = 0
    while counter < width:
        counter += 1
        line(counter, symbol)

def rect(width, height, filler):
    # You should call function line here with proper parameters
    char = 0
    while char < height:
        print(width*filler)
        char += 1

def shape(width, symbol, height, filler):
    triangle(width, symbol)
    rect(width, height, filler)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "o")