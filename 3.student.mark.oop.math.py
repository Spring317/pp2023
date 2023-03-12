from collections import OrderedDict 
import math 
import numpy as np
import curses
from curses import wrapper
 
#create dictionaries for students, courses and marks(including attendance, midterm and final mark):
students = {}
courses = {}
marks = {}
gpa = {}
sortedGPA = {}



#Create class Course 
class Course:
    
    
    def __init__(self, id, name, credit):
        #Perform encapsulation
        self.__name = name
        self.__id = id
        self.__credit = credit
    
    def get_Name(self):
        return self.__name
    
    def get_ID(self):
        return self.__id

    def get_Credit(self):
        return self.__credit
    
    def get_Course(self):
        courses[self.get_ID()] = {'name': self.get_Name(), 'credit': self.get_Credit()}




#Create class Person
class Person:
    
    def __init__(self, name, dob):
        #Perform encapsulation
        self.__name = name
        self.__dob = dob 
    
    def get_Name(self):
        return self.__name
    
    def get_DOB(self):
        return self.__dob

#Create class Student inherited from class Person
class Student(Person):
    
    #Perform encapsulation
    def __init__(self, name, dob, id):
        super().__init__(name, dob)
        self.__id = id
    
    def get_ID(self):
        return self.__id
    
  

    #get Students' info
    



#Create class Mark
class Mark:
    
    def __init__(self, m1, m2, m3):
        #Perform encapsulation 
        self.__average = m1*0.1 +m2*0.4 + m3*0.5
    
    def get_average(self):
        return self.__average
    
    #Methods for rounding down marks:
    def round_down(n, decimals = 0):
        multiplier = 10 ** decimals
        return math.floor(n * multiplier) / multiplier

    
    #method for calculating the gpa (option 5)
    def calculate_GPA():  
        credit_sum = 0
        mark_sum = 0
        
        for student_id in students:
            for course_id in courses:
                credit_sum += courses[course_id]["credit"]
                mark_sum += marks[student_id][course_id]["mark"] * courses[course_id]["credit"]
                print(credit_sum)
                print(mark_sum) 
            print(mark_sum/credit_sum)   
            gpa[student_id] ={'gpa': Mark.round_down((mark_sum/credit_sum),1)}
            credit_sum = 0
            mark_sum = 0                                                                                                         
            
        data = gpa.items()
        result = list(data)
        numpyGPA = np.array(result)
        return f"{gpa}"
        
    #method to sorted GPA in decending order (Option 6)
    def sorted_GPA():    
        
        #reverse = True give us a dictionary in decending order
        sortedGPA = sorted(gpa.items(), key=lambda x:x[1]['gpa'], reverse= True)
        return f"{sortedGPA}"        

class Input:

    def front_page(stdscr = curses.initscr()):
        column = 1    
        stdscr.addstr(column,10, "***************************************************************STUDENTS MANAGEMENT SYSTEM***************************************************************")
        column += 2
        stdscr.addstr(column,10, "************************************************************MADE BY BI12-379 DAO XUAN QUY***************************************************************")
        column += 2
        stdscr.addstr(column,71,"PRESS ANY KEY TO CONTINUE" )
        stdscr.getch()
        stdscr.clear()
        column = 1
       
    #get courses' info:
    def input_course(stdscr = curses.initscr()):
        curses.echo()
        column = 1
        stdscr.addstr(column,10, "***********************************************************************INPUT STEP*************************************************************************")
        column += 2
        stdscr.addstr(column,10, "ENTER NUMBER OF COURSES: ")
        str = "ENTER NUMBER OF COURSES: "
        user_input = stdscr.getstr(column,10 + len(str), 1)
        course_number = int(user_input)
        for i in range (course_number):
            
            column += 2
            stdscr.addstr(column,10, "ENTER COURSE'S ID: ")
            str = "ENTER COURSE'S ID: "
            user_input_id = stdscr.getstr(column,10 + len(str), 50)
            stdscr.refresh()
            column +=2
            stdscr.addstr(column,10, "ENTER COURSE'S NAME: ")
            str = "ENTER COURSE'S NAME: "
            user_input_name = stdscr.getstr(column,10 + len(str), 100)
            stdscr.refresh()
            column +=2
            stdscr.addstr(column,10, "ENTER COURSE'S CREDIT: ")
            str = "ENTER COURSE'S CREDIT: "
            user_input_credit = int(stdscr.getstr(column,10 + len(str), 50))
            stdscr.refresh()
            course_info = Course(user_input_id, user_input_name, user_input_credit)
            courses[course_info.get_ID()] = {"name": course_info.get_Name(), "credit": course_info.get_Credit()}
            stdscr.refresh()
                
        column += 2
        stdscr.refresh()
        stdscr.addstr(column, 75, "PRESS ENTER TO CONTINUE")           
        stdscr.getch()
        stdscr.clear()
    
    
    def input_students(stdscr = curses.initscr()):
        
        column = 1
        stdscr.addstr(column,10, "***********************************************************************INPUT STEP*************************************************************************")
        column += 2
        stdscr.addstr(column,10, "ENTER NUMBER OF STUDENTS: ")
        curses.echo()
        user_input = stdscr.getstr(column,37, 1)
        student_number = int(user_input)
        for i in range (student_number):
            column += 2
            stdscr.addstr(column,10, "ENTER STUDENT'S ID: ")
            str = "ENTER STUDENT'S ID: "
            user_input_id = stdscr.getstr(column,10 + len(str), 50)
            stdscr.refresh()
            column +=2
            stdscr.addstr(column,10, "ENTER STUDENT'S NAME: ")
            str = "ENTER STUDENT'S NAME: "
            user_input_name = stdscr.getstr(column,10 + len(str), 20)
            stdscr.refresh()
            column +=2
            stdscr.addstr(column,10, "ENTER STUDENT'S DATE OF BIRTH: ")
            str = "ENTER STUDENT'S DATE OF BIRTH: "
            user_input_dob = stdscr.getstr(column,10 + len(str), 50)
            stdscr.refresh()
            student_info = Student(user_input_name, user_input_dob, user_input_id)
            students[student_info.get_ID()] = {"name": student_info.get_Name(),  "dob": student_info.get_DOB()}
        stdscr.refresh()
        column += 2
        stdscr.refresh()
        stdscr.addstr(column, 75, "PRESS ENTER TO CONTINUE")
        stdscr.getch()
        stdscr.clear()
    
    #get marks' for students in each course (option 1):
    def input_mark(stdscr = curses.initscr()):

        curses.echo()
        column = 1
        stdscr.addstr(column,10, "***********************************************************************INPUT STEP*************************************************************************")
        column += 2
        
        stdscr.addstr(column,10, "ENTER THE COURSE ID: ")
        course_id = stdscr.getstr(column,31, 50)
        column += 2
        if course_id not in courses:
            stdscr.addstr(column, 10, "COURSE NOT FOUND! ")
            return
        column +=2
        stdscr.addstr(column, 10, f"MARK FOR STUDENT IN: {courses[course_id]['name']}")
        
        for student_id in students:
            column += 2
            stdscr.addstr(column, 10, f"ENTER THE ATTENDANCE MARK FOR {students[student_id]['name']}: ")
            str = f"ENTER THE ATTENDANCE MARK FOR {students[student_id]['name']}: "            
            attendance = float(stdscr.getstr(column, 10 + len(str), 2))
            column += 2
            stdscr.addstr(column, 10, f"ENTER THE MIDTERM MARK FOR {students[student_id]['name']}: ")
            str = f"ENTER THE MIDTERM MARK FOR {students[student_id]['name']}: "
            midterm = float(stdscr.getstr(column, 10+ len(str), 2))
            column += 2
            stdscr.addstr(column, 10, f"ENTER THE FINAL MARK FOR {students[student_id]['name']}: ")
            str = f"ENTER THE FINAL MARK FOR {students[student_id]['name']}: "
            final = float(stdscr.getstr(column, 10+ len(str), 2))
            
            
            
            
            #average*0.2 will return marks and gpa in 4.0 scale
        
            marks_for_student = Mark(attendance, midterm, final)
            if student_id not in marks:
                marks[student_id] = {}
            
            marks[student_id][course_id] = {'mark': Mark.round_down((marks_for_student.get_average()),1)}
            
            stdscr.refresh()
                
        column += 2
        stdscr.refresh()
        stdscr.addstr(column, 75, "PRESS ENTER TO CONTINUE")           
        stdscr.getch()
        stdscr.clear()

class Output:

    def option_slide(stdscr = curses.initscr()):
        while True:
            column = 1
            stdscr.addstr(column,10, "***********************************************************************OPTIONS:*************************************************************************")
            column += 2
            stdscr.addstr(column,66, "1. INPUT MARKS FOR STUDENTS IN COURSES")
            column += 2
            stdscr.addstr(column,66, "2. LIST STUDENTS")
            column += 2
            stdscr.addstr(column,66, "3. LIST COURSES")
            column += 2
            stdscr.addstr(column,66, "4.SHOW MARKS OF STUDENTS IN A GIVEN COURSE")
            column += 2
            stdscr.addstr(column,66, "5. CALCULATE GPA FOR STUDENTS")
            column += 2
            stdscr.addstr(column,66, "6. SORT GPA LIST IN DECENDING ORDER")
            column += 2
            stdscr.addstr(column, 60, "PLEASE TYPE THE NUMBER OF OPTION TO PERFORM IT: ")
            str = "PLEASE TYPE THE NUMBER OF OPTION TO PERFORM IT: "
            option = int(stdscr.getstr(column, 60 + len(str), 1))
            stdscr.clear()
            column = 1
            if option == 1:
                stdscr.addstr(column,10, "***********************************************************************OPTIONS: 1*************************************************************************")
                column += 2
                Input.input_mark()
                

            elif option == 2:
                stdscr.addstr(column,10, "***********************************************************************OPTIONS: 2*************************************************************************")
                column += 2
                Output.display_student(column)
                
               
            
            elif option == 3:
                stdscr.addstr(column,10, "***********************************************************************OPTIONS: 3*************************************************************************")
                column += 2
                Output.display_course(column)
            
            
            elif option == 4:
                stdscr.addstr(column,10, "***********************************************************************OPTIONS: 4*************************************************************************")
                column += 2
                Output.display_mark(column)

            elif option == 5:
                stdscr.addstr(column,10, "***********************************************************************OPTIONS: 5*************************************************************************")
                column += 2
                Output.display_GPA(column)

            elif option == 6:
                stdscr.addstr(column,10, "***********************************************************************OPTIONS: 6*************************************************************************")
                column += 2
                Output.sort_GPA(column)    
            
            elif option == 0: 
                stdscr.clear()
                break
                
        
    
        stdscr.getch()
    #display course (Option 2)    
    def display_course(column, stdscr = curses.initscr()):
        
        for course_id in courses:
            
            stdscr.addstr(column, 75, f"{course_id} |  {courses[course_id]['name']}")
            column += 2
        column +=2
        stdscr.addstr(column, 75, "PRESS ENTER TO CONTINUE")           
        stdscr.getch()
        stdscr.clear()
    #display student (option 3):
    
    def display_student(column, stdscr = curses.initscr()):
        
        for student_id in students:
            stdscr.addstr(column, 75, f"{student_id} | {students[student_id]['name'],students[student_id]['dob']}")
            column +=2
        column += 2
        stdscr.addstr(column, 75, "PRESS ENTER TO CONTINUE")           
        stdscr.getch()
        stdscr.clear()
    #display marks (option 4)
    def display_mark(column, stdscr = curses.initscr()): 
        
        
        stdscr.addstr(column,10, "***********************************************************************INPUT STEP*************************************************************************")
        column += 2
        stdscr.addstr(column,10, "ENTER THE COURSE ID: ")
        course_id = stdscr.getstr(column,31, 50)
        column += 2
        if course_id not in courses:
            stdscr.addstr(column, 10, "COURSE NOT FOUND! ")
            return
        column +=2
        
        for student_id in students:

            if student_id in marks and course_id in marks[student_id]:
                
                stdscr.addstr(column,75, f"{students[student_id]['name']}: {marks[student_id][course_id]['mark']}")
            
            else:
                stdscr.addstr(column,75, f"{students[student_id]['name']}: MARKS NOT AVAILABLE")
            column += 2
        
        column += 2
        stdscr.addstr(column, 75, "PRESS ENTER TO CONTINUE")           
        stdscr.getch()
        stdscr.clear()
    
    def display_GPA(column, stdscr = curses.initscr()):
        stdscr.addstr(column, 60, Mark.calculate_GPA())
        column += 2
        stdscr.addstr(column, 75, "PRESS ENTER TO CONTINUE")           
        stdscr.getch()
        stdscr.clear()

    def sort_GPA(column, stdscr = curses.initscr()):
        stdscr.addstr(column, 60,Mark.sorted_GPA())
        column += 2
        stdscr.addstr(column, 75, "PRESS ENTER TO CONTINUE")           
        stdscr.getch()
        stdscr.clear()

#Main function: 

def main(stdscr = curses.initscr()):
    input_data = Input
    input_data.front_page()
    input_data.input_students(stdscr= curses.initscr())
    input_data.input_course(stdscr = curses.initscr())
    output_data = Output
    output_data.option_slide(stdscr = curses.initscr())
    


wrapper(main)