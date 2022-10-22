
from tokenize import Name


class Student:

    def setName(self,Name):
        self.setName = Name
    def getName(self,):
        return self.getNmae
    def setRollNumber(self,RollNumber):
        self.setRollNumber = RollNumber
    def getRollNumber(self,):
        return self.getRollNumber


Student_obj=Student() 
Student_obj.Name="rahul"
Student_obj.RollNumber=28
print(Student_obj.Name)
print(Student_obj.RollNumber)