"""
Name: {Nattakamon Jitjamnong}
SID: {363411760006}
Group: {MIT431}
"""
# polymorphsim

# function build-in
mylist = [10,20,30,40,50]
x = 100

print(mylist,type(mylist))
print(x, type(x))


class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f'I am a Dog, My name is {self.name}'f'and I am {self.age} year old.')

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'I am a Cat, My name is {self.name}'f'and I am {self.age} year old.')

# function and object polymorphsim
def funcpoly (obj):
    obj.info()

# create objects
dog1 = Dog("Lulu",10)
cat1 = Cat("samock",8)

funcpoly(dog1)
funcpoly(cat1)

# class method polymorphsim
mypet = [dog1,cat1]

for x in mypet:
    x.info()