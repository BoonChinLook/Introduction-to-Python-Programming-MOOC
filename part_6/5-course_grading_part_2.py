# write your solution here

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points:")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"

id_name = {}
    
with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        id_name[parts[0]] = parts[1].strip() + " " + parts[2].strip()
        
id_courses = {}

#exercise points
with open(exercise_data) as exe_file:
    for line in exe_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue 
        course_id = parts[0] 
        id_courses[course_id] = []
        for course_counts in parts[1:]:
        	id_courses[course_id].append(int(course_counts))

#exam points      
exam_points = {}
with open(exam_data) as points_file:
    for line in points_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exam_id = parts[0]
        exam_points[exam_id] = []
        for points in parts[1:]:
            exam_points[exam_id].append(int(points))


for id, name in id_name.items():
    if id in id_courses or id in exam_points:
        courses_completed = id_courses[id]
        exams_completed = exam_points[id]
        exercise_points = sum(courses_completed)//4
        exam_totals = sum(exams_completed)
        totals = exam_totals + exercise_points
       
        grade = ""
        if totals < 15:
            grade = "0"
        elif totals < 18:
            grade = "1"
        elif totals < 21:
            grade = "2"
        elif totals < 24:
            grade = "3"
        elif totals < 28:
            grade = "4"
        elif totals > 27:
            grade = "5"
        
        print(f"{name} {grade}")

#print(exam_points)
#print(id_name)     
#print(id_courses)
#print(parts[1:])