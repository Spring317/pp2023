from input import Input
from Domain.Mark import Mark
import numpy as np
import curses

#Create curses Output
class Output:
    
    #create gpa
    gpa = {}

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
        
        for course_id in Input.courses:
            
            stdscr.addstr(column, 75, f"{course_id} |  {Input.courses[course_id]['name']}")
            column += 2
        column +=2
        stdscr.addstr(column, 75, "PRESS ENTER TO CONTINUE")           
        stdscr.getch()
        stdscr.clear()

    #display student (option 3):
    
    def display_student(column, stdscr = curses.initscr()):
        
        for student_id in Input.students:
            stdscr.addstr(column, 75, f"{student_id} | {Input.students[student_id]['name'], Input.students[student_id]['dob']}")
            column +=2
        column += 2
        stdscr.addstr(column, 75, "PRESS ENTER TO CONTINUE")           
        stdscr.getch()
        stdscr.clear()

    #display marks (option 4)

    def display_mark(column, stdscr = curses.initscr()): 
        
        
        
        stdscr.addstr(column,10, "ENTER THE COURSE ID: ")
        course_id = stdscr.getstr(column,31, 50).decode("utf-8")
        column += 2
        if course_id not in Input.courses:
            stdscr.addstr(column, 10, "COURSE NOT FOUND! PRESS ENTER TO PRECEED. ")
            stdscr.getch()
            stdscr.clear()

            return
        
        column +=2
        
        for student_id in Input.students:

            if student_id in Input.marks and course_id in Input.marks[student_id]:
                
                stdscr.addstr(column,75, f"{Input.students[student_id]['name']}: {Input.marks[student_id][course_id]['mark']}")
            
            else:
                stdscr.addstr(column,75, f"{Input.students[student_id]['name']}: MARKS NOT AVAILABLE")
            column += 2
        
        column += 2
        stdscr.addstr(column, 75, "PRESS ENTER TO CONTINUE")           
        stdscr.getch()
        stdscr.clear()
    
    def calculate_GPA():  
        credit_sum = 0
        mark_sum = 0
        
        for student_id in Input.students:
            for course_id in Input.courses:
                credit_sum += Input.courses[course_id]["credit"]
                mark_sum += Input.marks[student_id][course_id]["mark"] * Input.courses[course_id]["credit"]
                print(credit_sum)
                print(mark_sum) 
            print(mark_sum/credit_sum)   
            Output.gpa[student_id] ={'gpa': Mark.round_down((mark_sum/credit_sum),1)}
            credit_sum = 0
            mark_sum = 0                                                                                                         
            
        data = Output.gpa.items()
        result = list(data)
        numpyGPA = np.array(result)
        return f"{Output.gpa}"
    
    def sorted_GPA():    
        
        #reverse = True give us a dictionary in decending order
        sortedGPA = sorted(Output.gpa.items(), key=lambda x:x[1]['gpa'], reverse= True)
        return f"{sortedGPA}"

    def display_GPA(column, stdscr = curses.initscr()):
        stdscr.addstr(column, 60, Output.calculate_GPA())
        column += 2
        stdscr.addstr(column, 75, "PRESS ENTER TO CONTINUE")           
        stdscr.getch()
        stdscr.clear()

    def sort_GPA(column, stdscr = curses.initscr()):
        stdscr.addstr(column, 60,Output.sorted_GPA())
        column += 2
        stdscr.addstr(column, 75, "PRESS ENTER TO CONTINUE")           
        stdscr.getch()
        stdscr.clear()        

    
    
    
    