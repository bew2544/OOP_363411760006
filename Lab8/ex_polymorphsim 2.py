"""
Name: {Nattakamon Jitjamnong}
SID: {363411760006}
Group: {MIT431}
"""
# polymorphsim and inheritance
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f'My name is {self.name},'f'I am{self.age} years old.')

class Teacher(Person):
    def __init__(self,name,age,major):
        super().__init__(name,age)
        self.major = major
    def introduce(self):
        print(f'My name is {self.name},' f'I am{self.age} years old.'f'I am teacher in {self.major} major.')
class Student(Person):
    def __init__(self,name,age,major):
        super().__init__(name,age)
        self.major = major
    def introduce(self):
        print(f'My name is {self.name},' f'I am{self.age} years old.'f'I am Student in {self.major} major.')
# create object

p = Person ("Nattakamon Jitjamnong",21)
t = Teacher ("Puriwat Lertkrai",36,"MIT")
s = Student ("Piyapong Seananut",38,"AC")

department = [p,t,s]

for x in department:
    x.introduce()
