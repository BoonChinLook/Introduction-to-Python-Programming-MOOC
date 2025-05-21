# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(string1):
    word = string1[::-1]
    if word != string1:
        return False
    else:
        return True
    
while True:
    user_input = input("Please type in a palindrome: ")
    is_palindrome = palindromes(user_input)
    if is_palindrome:
        print(f"{user_input} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
    
   
    


