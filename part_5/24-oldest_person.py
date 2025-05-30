# Write your solution here

def oldest_person(people: list) -> str:
    oldest = people[0]
    for p in people:
        if p[1] < oldest[1]:
            oldest = p
    
    return oldest[0]

if __name__ == "__main__":
    people_list = [("Arthur", 1977), ("Emily", 2014)]

    print(oldest_person(people_list))