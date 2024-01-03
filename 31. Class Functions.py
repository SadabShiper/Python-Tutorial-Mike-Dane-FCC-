class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name # The name of the student's name is going to be equal to the name that we passed in.
        self.major = major # The name of the student's major is going to be equal to the major that we passed in.
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        
    def good_cgpa(self):
        if self.gpa >= 3.8:
            return True
        else:
            return False
    

student1 = Student("Jim", "Business", 3.9, False)
student2 = Student("Shiper", "Science", 3.19, True)

print(student1.name)
print(student1.good_cgpa())
print(student2.good_cgpa())