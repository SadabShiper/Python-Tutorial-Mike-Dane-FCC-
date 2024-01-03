employee_file = open("./employees.txt", "a")

# print(employee_file.read()) # won't work in append mode

employee_file.write("\nKelly - Customer Services")

# employee_file = open("./employees.txt", "w") employee_file.write("\nKelly - Customer Services") --> This will overwrite the entire file with only one line --> Kelly - Customer Services



employee_file.close()