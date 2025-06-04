# write your solution here

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

id_name = {}
    
with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        id_name[parts[0]] = parts[1].strip() + " " + parts[2].strip()
        
id_courses = {}

with open(exercise_data) as exe_file:
    for line in exe_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue 
        course_id = parts[0] 
        id_courses[course_id] = []
        for course_counts in parts[1:]:
        	id_courses[course_id].append(int(course_counts))
        
for id, name in id_name.items():
    if id in id_courses:
        courses_completed = id_courses[id]
        print(f"{name} {sum(courses_completed)}")

print(id_name)     
print(id_courses)
#print(parts[1:])