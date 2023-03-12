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
    
   
