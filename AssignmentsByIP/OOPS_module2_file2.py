

class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getDetails(self):
       return self.name

class B():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def getDetails(self):
        return self.name

class C(B,A):
    def getDetails(self):
        return self.name

childObj = C("xccxc", 12)
print(childObj.getDetails())