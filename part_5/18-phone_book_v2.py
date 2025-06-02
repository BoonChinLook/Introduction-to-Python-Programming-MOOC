# Write your solution here
my_dict = {}

while True:

    user_input = int(input("command (1 search, 2 add, 3 quit): "))

    if user_input == 2:
        user_name = input("name: ")
        user_number = input("number: ")
        if user_name in my_dict:
            my_dict[user_name].append(user_number)
        else:
            my_dict[user_name] = [user_number]
        print("ok!")
    elif user_input == 1:
        user_name = input("name: ")
        if user_name in my_dict and my_dict != "":
            for item in my_dict[user_name]:
                print(f"{item}")
        else:
            print("no number")
            
    elif user_input == 3:
        print("quitting...")
        break
    
         

