#from abc import ABCMeta, abstractmethod     #import of ABCMeta is compulsory for
from abc import ABC, abstractmethod

#Lecture 69
class Shape(ABC):   #this syntax represents for absract class, ABC when ABC is imported, but metaclass=ABCMeta when

    @abstractmethod    #decorator for making it abstract method and  making it compulsory for child class to implement
    def printarea(self):
        return 0


class Rectangle(Shape):

    def __init__(self):
        self.length = 4
        self.breadth = 3

    def printarea(self):
        return self.breadth * self.length


rect = Rectangle()
print(rect.printarea())


#we cannot create objects for abstract base class, cannot instantiate abstract class