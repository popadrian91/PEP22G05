import time

class Car:
    color = 'yellow'
    motors = ["fw-2KW-engine"]

    def __init__(self, color= 'red'):
        #print(self.color)
        #wheels = 4 # this is local to __init__
        self.wheels = 4
        self.construction_date = time.time()
        self.color = color

car = Car('green')
print(type(car))
print(car.color)

time,slice(1000)

car2 = Car()
print(type(car2))
print(car2.color)
car2.color = 'blue'
print("Car2 is:", car2.color)
print("Car1 is:", car.color)

car2.motors.append("rw-4KW-engine")
print("Car2 motor is:", car2.motors)
print("Car1 motor is:", car.motors)

car2.wheels = 5
print("car2 wheels is: ", car2.wheels)
print("car2 wheels is: ", car.wheels)

print("First car is contructed on : ", car.construction_date)
print("Second car is contructed on : ", car2.construction_date)