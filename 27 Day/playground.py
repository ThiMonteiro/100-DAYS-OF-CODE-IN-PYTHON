# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# # print(add(3, 5, 8, 9, 4))
#
# def calculate(**kwargs):
#     print(kwargs)
#
#
# calculate(add=7, multiply=9)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GT_R")
print(my_car.make, my_car.model, my_car.colour)