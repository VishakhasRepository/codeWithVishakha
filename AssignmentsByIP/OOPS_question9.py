# Q9. Create a class, Triangle. Its init() method should take self, angle1, angle2, and angle3 as
# arguments.


class Triangle:
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3


triangle = Triangle(30, 40, 60)
print(triangle.angle1)
print(triangle.angle2)
print(triangle.angle3)
