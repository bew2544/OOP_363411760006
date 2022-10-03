"""
Name: {Nattakamon Jitjamnong}
SID: {363411760006}
Group: {MIT431}
"""
class EV_Car:
        EV_Car = []
        def __init__(brand,model,motor,horsepower,batterrysize,range,price):
            self.brand = brand
            self.model = model
            self.motor = motor
            self.horsepower = horsepower
            self.batterrysize = batterrysize
            self.range = range
            self.price = price
            self.EV_Car.append(self)
        def display_info(self):
            print(f'brand: {self.brand} model: {self.model} motor: {self.motor} horsepower: {self.horsepower} batterrysize: {self.batterrysize} range: {self.range} price: {self.price}')


