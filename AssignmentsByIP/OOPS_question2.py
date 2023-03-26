#https://colab.research.google.com/drive/1R5eVoU0PGW9xOphSRDHxO9PSxeHgAvBZ#scrollTo=wRnQJ1adNkC6

# Q.2 Write a Python program to demonstrate Polymorphism.
# 1. Class Vehicle with a parameterized function Fare, that takes input value as fare and
# returns it to calling Objects.
# 2. Create five separate variables Bus, Car, Train, Truck and Ship that call the Fare
# function.
# 3. Use a third variable TotalFare to store the sum of fare for each Vehicle Type.
# 4. Print the TotalFare

class Vehicle:
    def __init__(self, fare):
        self.fare = fare

    def getFare(self):
        return self.fare


class Bus(Vehicle):

    def getFare(self):
        return self.fare

class Ship(Vehicle):

    def getFare(self):
        return self.fare

class Car(Vehicle):

    def getFare(self):
        return self.fare

class Train(Vehicle):

    def getFare(self):
        return self.fare

class Truck(Vehicle):

    def getFare(self):
        return self.fare

bus = Bus(22)
ship = Ship(23)
car = Car(24)
train = Train(25)
truck = Truck(26)


totalFare = bus.getFare() + car.getFare() + train.getFare() + truck.getFare() + ship.getFare()
print("The total fare is ", totalFare)