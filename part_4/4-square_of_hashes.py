# Copy here code of line function from previous exercise
def line(length, text):
    if text == "":
        print("*"*length)
    else:
        print(text[0]*length)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    hash = size
    while size > 0:
        line(hash, "#")
        size -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
