"""
Name: {Nattakamon Jitjamnong}
SID: {363411760006}
Group: {MIT431}
"""

# class relation - inheritance

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def person_info(self):
        print(f'Name: {self.name} Age: {self.age}')
class Student(Person): # Student inherited from Person
    def __init__(self,name,age,major,GPA):
        # 1
        #Person.__init__(self,name,age)
        # 2
        super().__init__(name,age)

        self.major = major
        self.GPA = GPA
    def student_info(self):
        print(f'Name:{self.name} Age: {self.age}'
              f'Major: {self.major}'
              f'GPA: {self.GPA}')

# create object
s1 = Student("Nattakamon Jitjamnong","21","MIT",3.22)
s1.person_info()
s1.student_info()