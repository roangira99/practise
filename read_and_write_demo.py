#opening and reading from a file
#always remember to also close the file
# file_name = "data.txt"
# f = open(file_name)
# #save the contents of the file
# f_contents = f.readline().strip()
# # f_contents = f.read()
# print(f_contents)
# f.close()

# #Iterating through the contents of the file line by line
# file_name = "data.txt"
# f = open(file_name)
# for line in f:
#     print(line.strip()) #the.strip method gets rid of the white space before and after the string
# f.close()

# # Preferred process to read into files
# Use a context manager to open files as demonstrated below:
# # When the file is executed, it closes out the file without having to write the close() method
# file_name = "data.txt"
# with open(file_name) as f:
#     for line in f:
#         print(line.strip()) #the.strip method gets rid of the white space before and after the string

# # Writing to a file
# file_name = "data.txt"
# with open(file_name) as f:
#     for line in f:
#         print(line.strip())
#
# record_to_add = "john,schmoe:python,ruby,javascript"

# # to write to a file you have to open the file with write permissions
# with open(file_name, "w") as to_write: # This replaces everything in the data.txt file with new data
#     to_write.write(record_to_add+"\n")

# # Appending to a file
# file_name = "data.txt"
# with open(file_name) as f:
#     for line in f:
#         print(line.strip())
#
# record_to_add = "john,schmoe:python,ruby,javascript"
#
# with open(file_name, "a+") as to_write: # # append to the file and if file doesn't exist, create the file
#     to_write.write(record_to_add+"\n")

# Function to convert string to parameters for __init__ (For extracting information to create student objects from them)
file_name = "data.txt"

# The function below reads in from the file and extracts the information to creat Students from them
# function to convert string to parameters for __init__
def prep_record(line):
    line = line.split(":") # split the whole string by the colon
    first_name, last_name = line[0].split(",") # take the first element (indexed by 0) then split it based on the comma so as to get two elements i.e first name and last name in a list
    course_details = line[1].rstrip().split(",") # take the second element (indexed by 1) then split it based on the comma to give you the 3 courses in list format. The rstrip() method gets rid of the new line character
    return first_name, last_name, course_details

# function to convert Student object to string for writing to the file
def prep_to_write(first_name, last_name, courses):
    full_name = first_name+','+last_name
    courses = ",".join(courses)
    return full_name+':'+courses

# Preferred process to read into files
# Use a context manager to open files as demonstrated below:
with open(file_name) as f:
    for line in f:
        print(line.strip()) # the strip method gets rid of the whitespace after each line
        first_name, last_name, course_details = prep_record(line) # unapcking the tuple
        print(first_name, last_name, course_details)

to_write = prep_to_write(first_name, last_name, course_details)
print(to_write)
record_to_add = "mark,pillager:python,ruby,javascript"

#  Function to convert Student object to string for write to file

# joe,schmo:python,ruby,javascript
# john,schmoe:python,ruby,javascript
# john,schmoe:python,ruby,javascript