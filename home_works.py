


import time


def give_ticket_number():
    return str(int(time.time()))

def give_ticket():
    number_car=int(input("Enter the number of your car: "))
    if not number_car:
        print("Number car is not true")
        return
    print("number of ticket",number_car,time,time)
give_ticket_number()
give_ticket()
















