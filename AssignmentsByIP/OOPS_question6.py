# Q6. Show a basic implementation of abstraction in python using the abstract classes.
# 1. Create an abstract class in python.
# 2. Implement abstraction with the other classes and base class as abstract class.

from abc import ABC, abstractmethod

class AbstractClass1(ABC):

    @abstractmethod
    def func1(self):
        print("This is abstract method")

class BaseClass(AbstractClass1):
    def func1(self):
        print("This is implemented method from abstract class")


baseClass = BaseClass()
baseClass.func1()

