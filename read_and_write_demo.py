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