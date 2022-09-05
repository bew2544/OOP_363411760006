"""
Name: {Nattakamon Jitjamnong}
SID: {363411760006}
Group: {MIT431}
"""
class MyPet:
    # class attribute
    mypet = []
    def __init__(self,name,age,breed):
        # object attribute
        self.name = name
        self.age = age
        self.breed = breed
        self.mypet.append(self)
    def display_info(self):
        print(f'name: {self.name} Age: {self.age} Breed: {self.breed}')

    def display_all_mypet(self):
        if len(self.mypet) ==0:
            print("You had no pet.")
        else:
            for x in self.mypet
