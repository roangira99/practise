## Building Student class

# class Student:
#     pass

# shaka = Student()
# robert = Student()
# print(shaka)
# print(jackie)

# shaka = Student()
# shaka.first_name = "shaka"
# shaka.last_name = "stuntin"
#
# jackie = Student()
# jackie.first_name = "jackie"
# jackie.last_name = "briggs"
# print(shaka.first_name, shaka.last_name)
# print(jackie.first_name, jackie.last_name)

# # We can use the init method, which initializes an instance of our object
# # The first argument 'self' is for the instance that's passed in, in this case, shaka.
# class Student:
#
#     def __init__(self, first, last, courses):
#         self.first_name = first
#         self.last_name = last
#         self.courses = courses
# # We have two arguments because self is automatically passed in by python when we
# # call the class
# courses_1 = ['python', 'rails', 'javascript']
# courses_2 = ['java', 'rails', 'c']
# shaka = Student("shaka", "stuntin",courses_1)
# jackie = Student("jackie", "briggs",courses_2)
#
# print(shaka.first_name, shaka.last_name, shaka.courses)
# print(jackie.first_name, jackie.last_name, jackie.courses)

# What if during creation the student has no courses they are enrolled in?
# We give the class an option to not provide courses when the object is created

# class Student:
#     # We set the default for courses when nothing is passed in to None
#     def __init__(self, first, last, courses = None):
#         self.first_name = first
#         self.last_name = last
#         # This if-else statement implements an empty list when no courses are present
#         # Otherwise, the courses will be displayed when passed
#         if courses == None:
#             self.courses = []
#         else:
#             self.courses = courses
#
# courses_1 = ['python', 'rails', 'javascript']
# courses_2 = ['java', 'rails', 'c']
# shaka = Student("shaka", "stuntin")
# jackie = Student("jackie", "briggs",courses_2)
#
# print(shaka.first_name, shaka.last_name, shaka.courses)
# print(jackie.first_name, jackie.last_name, jackie.courses)

# class Student:
#
#     def __init__(self, first, last, courses = None):
#         self.first_name = first
#         self.last_name = last
#         if courses == None:
#             self.courses = []
#         else:
#             self.courses = courses
#
#     def add_course(self, course):
#         if course not in self.courses:
#             self.courses.append(course)
#         else:
#             print(f"{self.first_name} is already\
#  enrolled in the {course} course")
#
#     def remove_course(self, course):
#         if course in self.courses:
#             self.courses.remove(course)
#         else:
#             print(f"{course} not found")
#
# courses_1 = ['python', 'rails', 'javascript']
# courses_2 = ['java', 'rails', 'c']
# shaka = Student("shaka", "stuntin",courses_1)
# jackie = Student("jackie", "briggs",courses_2)
#
# print(shaka.first_name, shaka.last_name, shaka.courses)
# print(jackie.first_name, jackie.last_name, jackie.courses)
# shaka.add_course("java")
# shaka.add_course("rails")
# print(shaka.first_name, shaka.last_name, shaka.courses)
# jackie.remove_course("c")
# jackie.remove_course("c")
# jackie.remove_course("python")
# print(jackie.first_name, jackie.last_name, jackie.courses)

# NB: Setting courses=None in the init method allows a new student object to be 
# created without having any courses selected

# Adding special/dunder methods to the class
class Student:

    def __init__(self, first, last, courses = None):
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
            print(f"{self.first_name} is already\
 enrolled in the {course} course")

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} not found")

    def __len__(self):
        return len(self.courses)

    def __repr__(self):
        return f"Student('{self.first_name}','{self.last_name}',{self.courses})"

    # Using the dunder str method:
    def __str__(self):
        return f"First name: {self.first_name.capitalize()}\nLast name: {self.last_name.capitalize()}\
        \nCourses: {', '.join(map(str.capitalize, self.courses))}"
        # In the above case we use the map function and provide it with the capitalize method, and
        # it will run it on each element in the list (the list is the iterable in this case)

# courses_1 = ['python', 'rails', 'javascript']
# courses_2 = ['java', 'rails', 'c']
# shaka = Student("shaka", "stuntin",courses_1)
# jackie = Student("jackie", "briggs",courses_2)
# print(shaka)
# print(repr(shaka))
# print(len(shaka))
# print(jackie)
# print(repr(jackie))
# print(dir(shaka))
# print(shaka.__dict__)

# storing and retreiving information about students using files
file_name = "data.txt"
shaka = Student("shaka", "stuntin", ["python", "ruby", "javascript"]) 
print(shaka.find_in_file(file_name)) # checking whether record already exists
print(shaka.add_to_file(file_name)) # add student to the file
dalia = Student("dalia", "nirva", ["python", "ruby", "javascript"])
print(dalia.find_in_file(file_name))
print(dalia.add_to_file(file_name))
