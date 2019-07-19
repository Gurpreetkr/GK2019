"""
Student
    Name
    Phone
    Email
    Password
    IsCollegeTraining
    CollegeName
    RollNumber

"""

"""
class Student:
    pass

s1 = Student()
s2 = Student()

s1.Name = "Joban"
s1.Phone = "+91 98744 56642"
s1.Email = "joban@example.com"
s1.Password = "pass4150"
s1.IsCollegeTarining = True
s1.CollegeName = "ABC International"
s1.RollNum = 4

s2.Name = "Kia"
s2.Phone = "+91 77665 66774"
s2.Email = "kia@example.com"
s2.Password = "pass1915"
s2.IsCollegeTarining = True
s2.CollegeName = "ABC International"
s2.RollNum = 19

students = [s1, s2]

print(s1.__dict__)
print(s2.__dict__)

# Challenge : No Standardization
# Solution : COnstructors
"""

class Student:

    schoolName = "NSPS"

    # self is a reference varible which will hold hashcode of current object
    # __init__ is known as constructor
    # Constructor is property of class
    def __init__(self, name, phoneNumber, email, password, isCollegeTraining, collegeName, rollNum ):
        print("self is:", self)
        self.fullName = name
        self.phone = phoneNumber
        self.email = email
        self.password = password
        self.isCollegeTraining = isCollegeTraining
        self.collegeName = collegeName
        self.rollNum = rollNum

    #Over-Writing -> A new constructor will be created and old will be removed
    # def __init__(self, name, phone):
    #     self.name = name
    #     self.phone = phone

    # showStudentDetails function is property of class
    def showStudentDetails(self):
        print("***************************")
        print("Details of",self.fullName)
        print("phone:\t",self.phone)
        print("Roll:\t",self.rollNum)
        print("***************************")

s1 = Student("Joban","+91 78653 56792", "joban@example.com", "pass4150", True, "NSPS International", 4)
print("s1 is:", s1)

s2 = Student("Kia","+91 78456 78792", "kia@example.com", "pass1915", True, "NSPS International", 19)
print("s2 is:", s2)

s1.age = 22
s1.vehicleNum = "PB10YZ4150"

s1.fullName = "JOban Malra"
s2.fullName = "Kia Kally"

# del s1.age
# del s1.phone

# print(s1.__dict__)
# print(s2.__dict__)

# s1.showStudentDetails()  or # Student.showStudentDetails(s1)
#  s2.showStudentDetails()

Student.showStudentDetails(s1)
Student.showStudentDetails(s2)

print()

print(s1.__dict__)
print(Student.__dict__)