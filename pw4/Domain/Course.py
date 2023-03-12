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
    
    
