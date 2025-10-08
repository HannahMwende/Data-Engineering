# A list to store all students as dictionaries
students = []

#Function to add a new student information and store it in the students list
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = float(input("Enter student grade: "))

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }
 
    students.append(student)
    print(f"Student {name} added")



# Function to display all students' information
def view_students():
    if not students:
        print("No students found.")
        return
    for student in students:
        print(student)



# Function to calculate and return the average grade of all students
def get_average_grade():
    if not students:
        print("No students to calculate average.")
        return 0
    avg = sum(student['grade'] for student in students) / len(students)
    print("Average grade:", avg)


#calling the functions to demonstrate their functionality
add_student()
view_students() 
get_average_grade()