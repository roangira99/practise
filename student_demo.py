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

