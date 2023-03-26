# Q11. Create a method named check_angles. The sum of a triangle's three angles should return
# True if the sum is equal to 180, and False otherwise. The method should print whether the
# angles belong to a triangle or not.


class Triangle:
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return print(True, "The angles belong to a triangle")
        return print(False, "The angles does not belong to a triangle")


triangle = Triangle(30, 90, 60)
print(triangle.angle1)
print(triangle.angle2)
print(triangle.angle3)
print(triangle.check_angles())