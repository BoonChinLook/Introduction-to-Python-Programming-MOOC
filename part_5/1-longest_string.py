# Write your solution here

def longest(strings: list):
    new = sorted(strings, key=len)
    return new[-1]

if __name__ == "__main__":
    strings = ["first", "second", "third"]
    print(longest(strings))