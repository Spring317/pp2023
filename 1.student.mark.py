#create dictionaries for students, courses and marks(including attendance, midterm and final mark):
students = {}
course = {}
mark = {}

#get courses' info:
def input_course():
    number_of_course = int(input("Enter the number of the course: "))
    #make sure the number of course cannot be negative
    
    while number_of_course < 0 :
        number_of_course = int(input("Please enter a positive number: "))
    
    for i in range(number_of_course):
        course_id = input("Enter course id (e.g: ict-001): ")
        
        #Make sure that the course id has a ict-xxx format
        while "ict" not in course_id:
            course_id = input("Re-enter course id (e.g: ict-001): ")  
        course_name = input("Enter course's name: ")
        course[course_id] = {'name': course_name}


#get students' info:
def input_students():
    number_of_student = int(input("Enter the number of students in the class: "))
    
    #Make sure that the number of student is not negative
    while number_of_student < 0 : 
        number_of_student = int(input("Please enter a positive number: "))
    
    for i in range(number_of_student):
        student_id = input("Enter the student ID (eg: bi01-001): ")
        
        #Check if student id follows the format bixx-yyy 
        while "bi" not in student_id: 
            student_id = input("Re-enter student id (eg: bi01-001): ")
        
        student_name = input("Enter the student name: ")
        student_dob = input("Enter the student dob: ")
        students[student_id] = {"name": student_name, "dob": student_dob}

    
#get marks' for students in each course (option 1):
def input_mark():

    course_id = input("Enter the course ID: ")
    if course_id not in course:
        print("Course not found!")
        return
    print(f"Marks for student in {course[course_id]['name']}")
    for student_id in students:
        attendance = float(input(f"Enter the attendance mark for {students[student_id]['name']}: "))
        midterm = float(input(f"Enter the midterm mark for {students[student_id]['name']}: "))
        final = float(input(f"Enter the final mark for {students[student_id]['name']}: "))
        if student_id not in mark:
            mark[student_id] = {}
        mark[student_id][course_id] = [attendance, midterm, final]
                
    

#display course (option 2):
def display_course():
    for course_id in course:
        print(f"{course_id}: {course[course_id]['name']}")


#display student (option 3):
def display_student():
    for student_id in students:
        print(f"{student_id}: {students[student_id]['name'],students[student_id]['dob']}")
        

#display mark (option 4):

def display_mark(): 
    
    course_id = input("Enter the course ID: ")
    if course_id not in course:
        print("Course not found!")
        return
    for student_id in students:
        if student_id in mark and course_id in mark[student_id]:
            
            print(f"{students[student_id]['name']}: {mark[student_id][course_id]}")
        else:
            print(f"{students[student_id]['name']}: Marks not available")
        
#Main function: 

input_students()
input_course()

while True:
    
    print("------------------------Options------------------------ ")
    print("1. Input marks for a course")
    print("2. List courses")
    print("3. List students")
    print("4. Show students' marks for a given course")
    print("0. Quit")
    option = input("Please choice an option: ")
    
    if option == "1":
        print("----------------------------------------------------")
        input_mark()
    
    elif option == "2":
        print("----------------------------------------------------")
        display_course()
    
    elif option == "3":
        print("----------------------------------------------------")
        display_student()
    
    elif option == "4":
        print("----------------------------------------------------")
        display_mark()
    
    elif option == "0":
        break
    
    else:
        print("Invalid choice")

    