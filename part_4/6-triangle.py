# Copy here code of line function from previous exercise
def line(length, text):
    if text == "":
        print("*"*length)
    else:
        print(text[0]*length)

def triangle(size):
    # You should call function line here with proper parameters
    counter = 1
    while counter -1 < size:
      line(counter, "#")
      counter += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
