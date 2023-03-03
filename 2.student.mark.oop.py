#create dictionaries for students, courses and marks(including attendance, midterm and final mark):
students = {}
courses = {}
marks = {}


class Course:
    def __init__(self, id, name):
        self.__name = name
        self.__id = id
    def get_Name(self):
        return self.__name
    def get_ID(self):
        return self.__id
    def set_Course(self):
        courses[self.get_ID()] = {'name': self.get_Name()}

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
            course_info = Course(course_id, course_name) 
            course_info.set_Course()
        
    def display_course():
        for course_id in courses:
            print(f"{course_id}: {courses[course_id]['name']}")




class Person:
    
    def __init__(self, name, dob):
        self.__name = name
        self.__dob = dob 
    
    def get_Name(self):
        return self.__name
    
    def get_DOB(self):
        return self.__dob


class Student(Person):
    
    def __init__(self, name, dob, id):
        super().__init__(name, dob)
        self.__id = id
    
    def get_ID(self):
        return self.__id
    
    def get_Student(self):
        students[self.get_ID()] = {"name": self.get_Name(), "dob": self.get_DOB()}

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
            student_info = Student(student_name, student_dob, student_id)
            student_info.get_Student()
    

#display student (option 3):
    def display_student():
        for student_id in students:
            print(f"{student_id}: {students[student_id]['name'],students[student_id]['dob']}")



class Mark:

    def __init__(self, attendance, midterm, final):
       self.__attendance = attendance
       self.__midterm = midterm
       self.__final = final
    def get_attendance(self):
        return self.__attendance
    def get_midterm(self):
        return self.__midterm
    def get_final(self):
        return self.__final

    def get_all_Mark(self, student_id, course_id):
         if student_id not in marks:
            marks[student_id] ={}
         marks[student_id][course_id] = [self.get_attendance(), self.get_midterm(), self.get_final()]
#get marks' for students in each course (option 1):
    def input_mark():

        course_id = input("Enter the course ID: ")
        if course_id not in courses:
            print("Course not found!")
            return
        print(f"Marks for student in {courses[course_id]['name']}")
        for student_id in students:
            attendance = float(input(f"Enter the attendance mark for {students[student_id]['name']}: "))
            midterm = float(input(f"Enter the midterm mark for {students[student_id]['name']}: "))
            final = float(input(f"Enter the final mark for {students[student_id]['name']}: "))
            marks_for_student = Mark(attendance, midterm, final)
            marks_for_student.get_all_Mark(student_id, course_id)
                
    

    def display_mark(): 
    
        course_id = input("Enter the course ID: ")
        if course_id not in courses:
            print("Course not found!")
            return
        for student_id in students:
            
            if student_id in marks and course_id in marks[student_id]:
                print(f"{students[student_id]['name']}: {marks[student_id][course_id]}")
            
            else:
                print(f"{students[student_id]['name']}: Marks not available")
        
#Main function: 

courses_data = Course
students_data = Student
marks_data = Mark

students_data.input_students()
courses_data.input_course()

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
        marks_data.input_mark()
    
    elif option == "2":
        print("----------------------------------------------------")
        courses_data.display_course()
    
    elif option == "3":
        print("----------------------------------------------------")
        students_data.display_student()
    
    elif option == "4":
        print("----------------------------------------------------")
        marks_data.display_mark()
    
    elif option == "0":
        break
    
    else:
        print("Invalid choice")

    