# Write your solution here
def first_word(string1):
    space = string1.find(" ")
    word = string1[0:space]
    return word

def second_word(string2):
    start = len(first_word(string2))
    space = string2[start+1:]
    space2 = space.find(" ")
    if space2 != -1:
        word = space[0:space2]
    else:
        word = space[0:]
    return word



def last_word(string3):
    space = string3.rfind(" ")
    word = string3[space+1:len(string3)]
    return word

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "it was a dark and stormy python"

    print(first_word(sentence)) # it
    print(second_word(sentence)) # was
    print(last_word(sentence)) # python