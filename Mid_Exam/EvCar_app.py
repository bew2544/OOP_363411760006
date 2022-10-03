from EV_Car import EV_Car

"""
1.เพิ่มข้อมูล EV_Car
2.แสดงข้อมูล EV_Car
3.ออกจากระบบ
"""
def display_option_system():
    print("\n---Welcome, to Ev_Car data store system---")
    print("1. add car data.")
    print("2. display car data.")
    print("3. exit.")

    select = int(input("select(1-3)? :"))
    if select ==1:
        input_ev_car_data()
    elif select ==2:
        display_ev_car()
    elif select ==3:
        print("Log out successfully.")
        exit(0)
    else:
        print("Please, enter 1-3 only. Thank.\n")


def display_ev_car():
    if len(ev_car_list) == 0:
        print("You had no car data.")
    else:
        print(f"Your had {len(ev_car_list)} following:")
    for x in ev_car_list:
        x.display_info()

def input_ev_car_data():
    brand = input("Enter your car brand:")
    model = input("Enter your car model:")
    motor = int(input("Enter your car motor:"))
    horsepower = int(input("Enter your car horsepower:"))
    batterrysize = input("Enter your car batterrysize:")
    range = int(input("Enter your car range:"))
    price = int(input("Enter your car price:"))

    ev_car_list.append(EV_Car(brand,model,motor,horsepower,batterrysize,range,price ))

ev_car_list = []
s=0
while s == 0:
    display_option_system()
