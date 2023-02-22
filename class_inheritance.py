# Inheritance 

class Student: # class definition
    # The init method initializes an instance of your object
    def __init__(self, first, last, courses=None): # the argument 'self' is the instance that's passed in
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = []
        else:
            self.courses = courses

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"{self.first_name} has already enrolled \
in the {course} course.")
            
# Create a class student athlete which inherits from class student
class StudentAthlete(Student):
    
    def __init__(self, first, last, courses=None, sport=None):
        super().__init__(first, last, courses) # calling the __init__ method from the super class
        self.sport = sport
            
courses = ["python","ruby","javascript"]
joe = StudentAthlete("john","schmoe", courses, "football")
print(joe.sport)

# function to check whether an object is an instance of a specific class. Returns Boolean value
# print(isinstance(joe, StudentAthlete))
print(isinstance(joe, Student))