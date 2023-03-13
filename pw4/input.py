
from Domain.Course import Course
from Domain.Student import Student
from Domain.Mark import Mark
import curses
from curses import wrapper

#Create Input for curses display
class Input:
    
    #Create Data
    courses = {}
    students = {}
    marks = {}

    #Display curses UI
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
            user_input_id = stdscr.getstr(column,10 + len(str), 50).decode("utf-8")
            stdscr.refresh()
            column +=2
            stdscr.addstr(column,10, "ENTER COURSE'S NAME: ")
            str = "ENTER COURSE'S NAME: "
            user_input_name = stdscr.getstr(column,10 + len(str), 100).decode("utf-8")
            stdscr.refresh()
            column +=2
            stdscr.addstr(column,10, "ENTER COURSE'S CREDIT: ")
            str = "ENTER COURSE'S CREDIT: "
            user_input_credit = int(stdscr.getstr(column,10 + len(str), 50))
            stdscr.refresh()
            course_info = Course(user_input_id, user_input_name, user_input_credit)
            Input.courses[course_info.get_ID()] = {"name": course_info.get_Name(), "credit": course_info.get_Credit()}
            stdscr.refresh()
                
        column += 2
        stdscr.refresh()
        stdscr.addstr(column, 75, "PRESS ENTER TO CONTINUE")           
        stdscr.getch()
        stdscr.clear()
        
    def get_courses_list():
        return Input.courses

    
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
            user_input_id = stdscr.getstr(column,10 + len(str), 50).decode("utf-8")
            stdscr.refresh()
            column +=2
            stdscr.addstr(column,10, "ENTER STUDENT'S NAME: ")
            str = "ENTER STUDENT'S NAME: "
            user_input_name = stdscr.getstr(column,10 + len(str), 20).decode("utf-8")
            stdscr.refresh()
            column +=2
            stdscr.addstr(column,10, "ENTER STUDENT'S DATE OF BIRTH: ")
            str = "ENTER STUDENT'S DATE OF BIRTH: "
            user_input_dob = stdscr.getstr(column,10 + len(str), 50).decode("utf-8")
            stdscr.refresh()
            student_info = Student(user_input_name, user_input_dob, user_input_id)
            Input.students[student_info.get_ID()] = {"name": student_info.get_Name(),  "dob": student_info.get_DOB()}
        stdscr.refresh()
        column += 2
        stdscr.refresh()
        stdscr.addstr(column, 75, "PRESS ENTER TO CONTINUE")
        stdscr.getch()
        stdscr.clear()
    
    def get_students_list():
        return Input.students
          
    
    #get marks' for students in each course (option 1):
    def input_mark(stdscr = curses.initscr()):

        Input.courses = Input.get_courses_list()
        Input.students = Input.get_students_list()

        curses.echo()
        column = 1
        stdscr.addstr(column,10, "***********************************************************************INPUT STEP*************************************************************************")
        column += 2
        
        stdscr.addstr(column,10, "ENTER THE COURSE ID: ")
        course_id = stdscr.getstr(column,31, 50).decode("utf-8")
        column += 2
        if course_id not in Input.courses:
            stdscr.addstr(column, 10, "COURSE NOT FOUND! PRESS ENTER TO PRECEED")
            stdscr.getch()
            stdscr.clear()
            return
        column +=2
        stdscr.addstr(column, 10, f"MARK FOR STUDENT IN: {Input.courses[course_id]['name']}")
        
        for student_id in Input.students:
            column += 2
            stdscr.addstr(column, 10, f"ENTER THE ATTENDANCE MARK FOR {Input.students[student_id]['name']}: ")
            str = f"ENTER THE ATTENDANCE MARK FOR {Input.students[student_id]['name']}: "            
            attendance = float(stdscr.getstr(column, 10 + len(str), 2))
            column += 2
            stdscr.addstr(column, 10, f"ENTER THE MIDTERM MARK FOR {Input.students[student_id]['name']}: ")
            str = f"ENTER THE MIDTERM MARK FOR {Input.students[student_id]['name']}: "
            midterm = float(stdscr.getstr(column, 10+ len(str), 2))
            column += 2
            stdscr.addstr(column, 10, f"ENTER THE FINAL MARK FOR {Input.students[student_id]['name']}: ")
            str = f"ENTER THE FINAL MARK FOR {Input.students[student_id]['name']}: "
            final = float(stdscr.getstr(column, 10+ len(str), 2))
        
            marks_for_student = Mark(attendance, midterm, final)
            if student_id not in Input.marks:
                Input.marks[student_id] = {}
            
            Input.marks[student_id][course_id] = {'mark': Mark.round_down((marks_for_student.get_average()),1)}
        
        column += 2
        stdscr.addstr(column, 75, "PRESS ENTER TO CONTINUE")
        stdscr.getch()
        stdscr.refresh()
        stdscr.clear()


    def get_marks_list():
        return Input.marks
    
    
   