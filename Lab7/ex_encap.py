"""
Name: {Nattakamon Jitjamnong}
SID: {363411760006}
Group: {MIT431}
"""
#encapsulation

class Student:
    def __init__(self,id,name,major):
        self.__id = id # private member
        self.name = name
        self.major = major
    def display_data_object(self):
        print(f'{self.__id} {self.name} {self.major}')
    # getter and setter methonds
    def get_id(self):
        return  self.__id
    def set_id(self,newid):
        self.__id =newid

# outside class
std = Student("006","Nattakamon Jitjamnong","MIT")

#display data of attributes
#print(std.id,std.name,std.major)

# access to private member

# 1. use public method
std.display_data_object()
# 2. name mangling
print(std._Student__id)

std._Student__id = "002"
print(std._Student__id)

# use getter and setter method
print(std.get_id())

std.set_id("004")
std.display_data_object()