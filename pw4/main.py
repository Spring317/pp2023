
#Add module for Output  
from input import Input
from output import Output
import curses
from curses import wrapper

#Main function: 

def main(stdscr = curses.initscr()):
    input_data = Input
    input_data.front_page()
    input_data.input_students(stdscr= curses.initscr())
    input_data.input_course(stdscr = curses.initscr())
    output_data = Output
    output_data.option_slide(stdscr = curses.initscr())
    


wrapper(main)