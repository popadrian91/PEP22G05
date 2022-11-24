import time

class Car:
    color = 'yellow'
    motors = ["fw-2KW-engine"]
    lights = 'off'
    #name = 'Masina'
    def __init__(self,name = 'Dacia', color= 'red'):
        #print(self.color)
        #wheels = 4 # this is local to __init__
        self.wheels = 4
        self.construction_date = time.time()
        self.color = color
        self.name = name

    def start_car(self):
        print('Brum.....brum')
        self.lights='on'

    @staticmethod
    def factorial(number):
        result = 1
        for i in range(1, number+1):
            result *= i
        return result

    def __eq__(self, other):#metoda care se ocupa cu verificarea egalitatii dintre 2 obiecte
        print(self.construction_date, other.construction_date)
        if self.color == other.color and self.wheels == other.wheels:
            return True
        else:
            return False

    def __str__(self):
        f= ''
        f = f"name = {self.name} date={self.construction_date} color = {self.color}"
        return f

# car = Car('green')
# print(type(car))
# print(car.color)
#
# time,slice(1000)
#
# car2 = Car()
# print(type(car2))
# print(car2.color)
# car2.color = 'blue'
# print("Car2 is:", car2.color)
# print("Car1 is:", car.color)
#
# car2.motors.append("rw-4KW-engine")
# print("Car2 motor is:", car2.motors)
# print("Car1 motor is:", car.motors)
#
# car2.wheels = 5
# print("car2 wheels is: ", car2.wheels)
# print("car2 wheels is: ", car.wheels)
#
# print("First car is contructed on : ", car.construction_date)
# print("Second car is contructed on : ", car2.construction_date)


print(id(Car))
print(type(Car))
car1 = Car()
print('Color before  change:',car1.color)
print(Car.__init__(car1, color='green'))
print('Color after change:',car1.color)

print('Light before start the car', car1.lights)
car1.start_car()
print('Light after start the car', car1.lights)

# print('Light before start the car', car1.lights)
# print(Car.start_car("<needs object created with class Carr>"car1))
# print('Light after start the car', car1.lights)

print(Car.factorial(5))
print(car1.factorial(5))

car1 = Car()
time.sleep(0.1)
car1.wheels = 5
car2 = Car()
print(car1 == car2)

car1= Car('Dacia')
print(str(car1))
