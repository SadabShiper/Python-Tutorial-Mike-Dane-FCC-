# Three modes --> r, w, a (read, write, append)
# r+ --> reading + writing

employee_file = open("./employees.txt", "r")

# print(employee_file)

# print(employee_file.readable()) # to check whether the file is readable
# Now, it's True, if the mode is set to "w", then file is not readable and the value is False

# print(employee_file.read()) # read the whole file


# print(employee_file.readline()) # read the first line
# print(employee_file.readline()) # read the second line

# print(employee_file.readlines()[2]) # to read exactly the third line of the file
# readlines() function outputs a list


for employee in employee_file.readlines():
    print(employee)
employee_file.close()