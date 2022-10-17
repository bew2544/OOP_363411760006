"""
Name: {Nattakamon Jitjamnong}
SID: {363411760006}
Group: {MIT431}
"""

# class relations - dependency

from datetime import date

class Customer:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def customer_info(self):
        print(f'cusid: {self.id} customer: {self.name}')
class Oder:
    def __init__(self,id,Customer,data,total_cost):
        self.id = id
        self.customer = Customer
        self.data = data
        self.total_cost = total_cost
    def oder_info(self):
        print(f'oder id: {self.id}'
              f'customer name: {self.customer.name}'
              f'data: {self.data}'
              f'total cost: {self.total_cost}')

# create object
customer1 = Customer("cus006","Nattakamon Jitjamnong")
order1 = Oder("order001" ,customer1,date.today(),15000.00)

# display data
customer1.customer_info()
order1.oder_info()
