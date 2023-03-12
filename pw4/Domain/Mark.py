
import math 
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
    
    
    
    
    
   
    
    
   
           
    