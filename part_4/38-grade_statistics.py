# Write your solution here
import math
def user_inputs():
    store_inputs = []
    while True:
        completed = input("Exam points and exercises completed: ")
        if completed == "":
            break
        split = completed.split(" ")
        store_inputs.append(split)
    return store_inputs   

def exercise_points(my_grades: list):
    grade = []
    for exam, points in my_grades:
        points = int(points)
        exam = int(exam)
        grades = exam + math.floor(points//10)
        grade.append(grades)
    return grade

#can do count() here instead of elements later maybe
def scoring(grade):
    score = []
    for scores in grade:
        if scores >= 28:
            score.append(5)
        elif scores >= 24:
            score.append(4)
        elif scores >= 21:
            score.append(3)
        elif scores >= 18:
            score.append(2)
        elif scores >= 15:
            score.append(1)
        else:
            score.append(0)
    return score

def passed(marks, scoring, grades):
    end_result = []
    for scores in scoring:
        if scores == 0:
            end_result.append("failed")
        elif scores == 5:
            end_result.append("passed")
        elif scores == 4:
            end_result.append("passed")
        elif scores == 3:
            end_result.append("passed")
        elif scores == 2:
            end_result.append("passed")
        elif scores == 1:
            end_result.append("passed")
    #less than 10 points exam fail
    for items in grades:
        if int(items[0]) < 10 and scores != 0 and "passed" in end_result:
            end_result.append("failed")
            end_result.remove("passed")
    pass_percent = (end_result.count("passed")/len(end_result))*100
    return pass_percent

def mean_score(marks):
    return  sum(marks)/len(marks)

def grading(score_list, grades):
    for index in range(len(grades)):  # Iterate using index
        if int(grades[index][0]) < 10 and score_list[index] != 0:
            score_list[index] = 0

    counter = 5
    for counts in range(counter + 1):
        print(f"{counter}: {score_list.count(counter)*"*"}")
        counter -= 1

def main():
    grades = user_inputs()
    marks = exercise_points(grades)
    score_list = scoring(marks)
    pass_percent = passed(marks, score_list, grades)
    avg_points = mean_score(marks)
    print("Statistics: ") 
    print(f"Points average: {avg_points:.1f}")
    print(f"Pass percentage: {pass_percent:.1f}") 
    print("Grade distribution:")
    grade_distribution = grading(score_list, grades) 
    
main()