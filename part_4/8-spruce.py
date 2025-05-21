# Write your solution here
# You can test your function by calling it within the following block
def spruce(size):
    print("a spruce!")
    rows = 1
    longest_row = ((size*2)-1)//2
    end_row = longest_row
    while longest_row >= 0:
        print(" "*longest_row + "*"*rows)
        rows += 2
        longest_row -= 1
    print(" "*end_row + "*")
    

if __name__ == "__main__":
    spruce(3)