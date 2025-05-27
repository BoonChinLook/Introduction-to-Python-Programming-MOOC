# Write your solution here

def dict_of_numbers() -> dict:
    my_dict = {}
    other_dict = {}
    twenty = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    for item in range(len(twenty)):
        my_dict[item] = twenty[item]
       

    i = 20
    while i < 100:
        if i % 10 == 0:
            my_dict[i] = tens[i//10]
            i+= 1
        else:
            my_dict[i] = tens[i//10] + "-" + twenty[i%10]
            i+= 1

    return my_dict
    
if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])