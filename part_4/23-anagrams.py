# Write your solution here

def anagrams(string1, string2):
    if sorted(string1) == sorted(string2):
        return True
    return False

if __name__ == "__main__":
    print(anagrams("tame", "meta"))