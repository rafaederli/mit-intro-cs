# -------------------- FINGER EXERCISE LECTURE 17
# Write the class according to the specifications below:

class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        self.r = radius

    def get_radius(self):
        """ Returns the radius of self """
        return self.r

    def set_radius(self, radius):
        """ radius is a number
        Changes the radius of self to radius """
        self.r = radius

    def get_area(self):
        """ Returns the area of self using pi = 3.14 """
        return 3.14 * (self.r ** 2)

    def equal(self, c):
        """ c is a Circle object
        Returns True if self and c have the same radius value """
        return self.r == c.r

    def bigger(self, c):
        """ c is a Circle object
        Returns self or c, the Circle object with the bigger radius """
        return self if self.r > c.r else c

circle1 = Circle(10)
circle2 = Circle(20)

# print(circle1.get_radius())
# print(circle2.get_radius())

# circle1.set_radius(100)
# circle2.set_radius(200)
# print(circle1.get_radius())
# print(circle2.get_radius())

# print(circle1.get_area())
# print(circle2.get_area())

# print(circle1.equal(circle2))

print(f"circle1: {circle1}")
print(f"circle2: {circle2}")
print(circle1.bigger(circle2))