"""
Name: {Nattakamon Jitjamnong}
SID: {363411760006}
Group: {MIT431}
"""

class Labtop:
    def __init__(self,brand,model,cpu,ram,display,storage,price):
                self.__brand = brand #private member
                self.__model =model
                self.__cpu = cpu
                self.__ram = ram
                self.__display = display
                self.__storage = storage
                self.__price = price
    def get_brand(self):
                return self.__brand
    def get_model(self):
                return self.__model
    def get_cpu(self):
                return self.__cpu
    def get_ram(self):
                return self.__ram
    def get_display(self):
                return self.__display
    def get_storage(self):
                return self.__storage
    def get_price(self):
                return self.__price
    def person_info(self):
                print(f'labtop Brand:{self.__brand}' f'Model:{self.__model}' f'CPU: {self.__cpu}' 
              f'RAM: {self.__ram}' f'Display:{self.__display}' f'Storage:{self.__storage}'f'Price: {self.__price}')
LT = Labtop("ASUS","Vivobook 15X","intel Core i5-12500H","8","15.6","512","27,990")
print(LT.get_brand())
print(LT.get_model())
print(LT.get_cpu())
print(LT.get_ram())
print(LT.get_display())
print(LT.get_storage())
print(LT.get_price())

