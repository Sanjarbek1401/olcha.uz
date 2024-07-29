""" class Car:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        return self.odometer / self.time


if __name__ == '__main__':

    my_car = Car()
    print("I'm a car!")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, "
                        "show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
            print("Accelerating...")
        elif action == 'B':
            my_car.brake()
            print("Braking...")
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        my_car.step() """
        
# time_zone = 'GMT+3'
# print(time_zone)
""" 
a = 10

def foo():
    pass    

class Bar:
    pass
   
print(type(a))
print(type(foo))
print(type(Bar)) """

# a = 1
# print(id(a))

# a += 2
# print(id(a))

""" my_list = [1, 2]
print(id(my_list))

my_list.append(3)
print(id(my_list)) """

# x = "100"
# y = int(x)
# print(type(y))

# x =  int('FACE', 16)
# print(x)

# x = (10 + 30 + 6) / 3
# print(x)
""" import math
x = 3.5
y = 5.2
print("Euclidean distance for x=", x, " y=", y, " hypot=", math.hypot(x, y)) """

import math

def calculate_expression(a, b):
    numerator = 12 * a + 25 * b
    denominator = 1 + a**(2**b)
    result = numerator / denominator
    return round(result, 2)

# Example usage
a = 2
b = 3
print(calculate_expression(a, b))  # Output: 25.71
