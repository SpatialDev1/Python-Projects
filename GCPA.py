def get_details():
    name = input("Enter your name: ")
    department = input("Enter your department: ")
    num_of_courses = int(input("Enter the number of courses you're offering: "))
    personal_details = {"name": name, "department": department}
    # course_details = {}
    course_details = []
    for i in range(num_of_courses):
        course_code = input("Enter course code: ")
        credit_unit = int(input("Enter credit unit: "))
        while True:
            score = int(input("Enter your score (0-100): "))
            if 0 <= score <= 100:
                break
        single_course = {
            "course_code": course_code,
            "credit_unit": credit_unit,
            "score": score
        }
        # course_details.append([course_code, credit_unit, score])
        course_details.append(single_course)
    return personal_details, course_details




def get_grade(details):
    grades = []
    for course in details:
        if 70<= course["score"] <=100:
            grade = "A"
            grades.append(grade)
        elif 60 <= course["score"] <= 69:
            grade = "B"
            grades.append(grade)
        elif 50 <= course["score"] <= 59:
            grade = "C"
            grades.append(grade)
        elif 45 <= course["score"] <= 49:
            grade = "D"
            grades.append(grade)
        elif 40 <= course["score"] <= 44:
            grade = "E"
            grades.append(grade)
        else:
            grade = "F"
            grades.append(grade)


    return grades

def calc(details):
    total_credit_units = 0
    total_grade_points = 0
    for course in details:
        score = course["score"]
        credit_unit = course["credit_unit"]
        if 70 <= score <= 100:
            grade_point = 5
        elif 60 <= score <= 69:
            grade_point = 4
        elif 50 <= score <= 59:
            grade_point = 3
        elif 45 <= score <= 49:
            grade_point = 2
        elif 40 <= score <= 44:
            grade_point = 1
        else:
            grade_point = 0


        total_credit_units += credit_unit
        total_grade_points += credit_unit * grade_point

    if total_credit_units > 0:
        gpa = total_grade_points / total_credit_units
    else:
        gpa = 0.0

    return total_credit_units, total_grade_points, gpa

def class_of_degree(gpa):
    if 4.5 <= gpa <= 5.0:
        return "First class"
    elif 3.5 <= gpa <= 4.49:
        return "Second class upper"
    elif 2.4 <= gpa <= 3.49:
        return "Second class lower"
    elif 1.5 <= gpa <= 2.39:
        return "Third class"
    elif 1.00 <= gpa <= 1.49:
        return "Pass"
    else:
        return "Fail"


def save_to_file(personal_details, total_credit_units, total_grade_points, gpa, grad_class, course_details, grades):
    filename = "CGPA_Report.txt"
    with open(filename, "w") as file:
        file.write("========================================\n")
        file.write("           UNIVERSITY GPA REPORT        \n")
        file.write("========================================\n")
        file.write(f"Student Name: {personal_details['name'].title()}\n")
        file.write(f"Department: {personal_details['department'].title()}\n")
        file.write("----------------------------------------\n")
        file.write("Course Details:\n")
        for idx, course in enumerate(course_details):
            file.write(f"  - {course['course_code']}: Units = {course['credit_unit']}, Score = {course['score']}, Grade = {grades[idx]}\n")
        file.write("----------------------------------------\n")
        file.write(f"Total Credit Units: {total_credit_units}\n")
        file.write(f"Total Grade Points: {total_grade_points}\n")
        file.write(f"Semester GPA: {gpa:.2f}\n")
        file.write(f"Class of Degree: {grad_class}\n")
        file.write("========================================\n")
    print(f"\n Results successfully saved to '{filename}'!")



def main():
    personal_details, course_details = get_details()

    grades = get_grade(course_details)

    total_credit_units, total_grade_points, gpa = calc(course_details)

    grad_class = class_of_degree(gpa)

    save_to_file(personal_details, total_credit_units, total_grade_points, gpa, grad_class, course_details, grades)

if __name__ == "__main__":
    main()


