"""
Name: {Nattakamon Jitjamnong}
SID: {363411760006}
Group: {MIT431}
"""
"""
OOP Exercise Chapter 6
1. จงเขียนโปรแกรมภาษาไพธอนเพื่อสร้างคลาสพาหนะชื่อ Vehicle ที่ประกอบไปด้วยคุณลักษณะ (attributes) คือ 
ยี่ห้อรถ (brand) 
รุ่นรถ (model)
สีรถ (color)
ความเร็วสูงสุด (max speed)
ราคา (price)
2.จากข้อที่ 1 เขียนโปรแกรมเพื่อสร้างวัตถุ (object) จากคลาส Vehicle โดยรับข้อมูลจากผู้ใช้ตามคุณลักษณะ (attributes)ของคลาส
จากนั้นแสดงข้อมูลทางหน้าจอภาพ
15 นาที
"""
class Vehicle :
    def __init__(self,brand,model,color,maxspeed,price):
        self.brand = brand
        self.model = model
        self.color = color
        self.mexspeed = maxspeed
        self.price = price

    brand = input('Enter your ยี่ห้อรถ (brand) : ')
    model = input('Enter your รุ่นรถ (model) : ')
    color = input('Enter your สีรถ (color) : ')
    maxspeed = input('Enter your ความเร็วสูงสุด (max speed) : ')
    price = input('Enter your ราคา (price) : ')
    print('ยี่ห้อรถ :',brand)
    print('รุ่นรถ :',model)
    print('สีรถ :',color)
    print('ความเร็วสูงสุด :',maxspeed)
    print('ราคา :',price,'บาท')