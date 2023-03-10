# Classes
# !!!!! Check the read_and_write_demo.py file to get explanations of function functionality !!!!!

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
            
    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{self.first_name} is not enrolled in the {course} course.")

    # function to check whether an object exists in the file
    def find_in_file(self, filename):
        with open(filename) as f:
            for line in f:
                first_name, last_name, course_details = Student.prep_record(line.strip()) # unapcking the tuple and reference the static method(prep_record) using the class name
                student_read_in = Student(first_name, last_name, course_details) # creating a student object
                if self == student_read_in: # comparing the instance of the student we're passing in to the student that is read in from the file to see if they are equal
                    return True
            return False

    def add_to_file(self, filename):
        if self.find_in_file(filename):
            return "Record already exists"
        else:
            record_to_add = Student.prep_to_write(self.first_name, self.last_name, self.courses)
            with open(filename, "a+") as to_write:
                to_write.write(record_to_add+"\n")
            return "Record added"

    # The function below reads in from the file and extracts the information to creat Students from them
    # function to convert string to parameters for __init__
    @staticmethod
    def prep_record(line):
        line = line.split(":") # split the whole string by the colon
        first_name, last_name = line[0].split(",") # take the first element (indexed by 0) then split it based on the comma so as to get two elements i.e first name and last name in a list
        course_details = line[1].rstrip().split(",") # take the second element (indexed by 1) then split it based on the comma to give you the 3 courses in list format. The rstrip() method gets rid of the new line character
        return first_name, last_name, course_details
    
    @staticmethod
    def prep_to_write(first_name, last_name, courses):
        full_name = first_name+','+last_name
        courses = ",".join(courses)
        return full_name+':'+courses
    
    # special method for altering the default functinality of the equality operator
    def __eq__(self, other):
        return self.first_name == other.first_name \
        and self.last_name == other.last_name

    def __len__(self):
        return len(self.courses)
    
    def __repr__(self):
        return f"Student('{self.first_name}', {self.last_name}', {self.courses})"

    # custom dunder str method
    def __str__(self):
        return f"First name: {self.first_name.capitalize()}\nLast name: {self.last_name.capitalize()}\
            \nCourses: {', '.join(map(str.capitalize, self.courses))}" # the map function runs the capitalize method on each element of the list

# storing and retreiving information about students using files
file_name = "data.txt"
shaka = Student("shaka", "stuntin", ["python", "ruby", "javascript"]) 
print(shaka.find_in_file(file_name)) # checking whether record already exists
print(shaka.add_to_file(file_name)) # add student to the file
dalia = Student("dalia", "nirva", ["python", "ruby", "javascript"])
print(dalia.find_in_file(file_name))
print(dalia.add_to_file(file_name))
craig = Student("craig", "marduk", ["java", "c++", "SQL"])
print(craig.find_in_file(file_name))
print(craig.add_to_file(file_name))
