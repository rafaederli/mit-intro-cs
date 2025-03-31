# -------------------- LECTURE 18 NOTES

# ----- Classes
# Add code to the init method to check that the type of center is a coordinate obj and the type of radius is an int. If either are not these types, raise a ValueError

# class Coordinate(object):
#     def __init__(self, x, y):
#         """
#         Sets the x and y values
#         """
#         self.x = x
#         self.y = y
    
#     def distance(self, other):
#         """
#         Returns euclidean dist between two Coord obj
#         """
#         x_diff_sq = (self.x - other.x) ** 2
#         y_diff_sq = (self.y - other.y) ** 2
#         return (x_diff_sq + y_diff_sq) ** 0.5
        

# class Circle(object):
#     def __init__(self, center, radius):
#         if type(center) != Coordinate:
#             raise ValueError
#         if type(radius) != int:
#             raise ValueError
#         self.center = center
#         self.radius = radius

#     def is_inside1(self, point):
#         return point.distance(self.center) < self.radius
    
#     def is_inside2(self, point):
#         return self.center.distance(point) < self.radius

# center = Coordinate(2, 2)
# my_circle = Circle(center, 2) # no error
# # my_circle = Circle(2, 2)
# # my_circle = Circle(center, "two")

# point = Coordinate(1, 1)

# print(my_circle.is_inside1(point) == my_circle.is_inside2(point))

# Add two methods to invert fraction object according to the specs below:
# class SimpleFraction(object):
#     """
#     A number represented as fraction
#     """
#     def __init__(self, num, denom):
#         self.num = num
#         self.denom = denom
#     def get_inverse(self):
#         """
#         Returns a float representing 1/self
#         """
#         return self.denom / self.num
#     def invert(self):
#         """
#         Sets self's num to denom and vice versa
#         Returns None
#         """
#         (self.num, self.denom) = (self.denom, self.num)
        
# f1 = SimpleFraction(3, 4)
# print(f1.get_inverse())
# f1.invert()
# print(f1.num, f1.denom)

# class Fraction(object):
#     def __init__(self, n, d):
#         self.num = n
#         self.denom = d
#     def __str__(self):
#         return f"{self.num} / {self.denom}" if self.denom != 1 else f"{self.num}"
#     def reduce(self):
#         def gcd(n, d):
#             while d != 0:
#                 (d, n) = (n % d, d)
#             return n
#         if self.denom == 0:
#             return None
#         elif self.denom == 1:
#             return Fraction(self.num, 1)
#         else:
#             greatest_common_divisor = gcd(self.num, self.denom)
#             top = int(self.num / greatest_common_divisor)
#             bottom = int(self.denom / greatest_common_divisor)
#             return Fraction(top, bottom)
        
# f1 = Fraction(3, 4)
# f2 = Fraction(1, 4)
# f3 = Fraction(5, 1)

# print(f1)
# print(f2)
# print(f3)

# a = Fraction(1, 4)
# b = Fraction(3, 1)

# print(a)
# print(b)

# f1 = Fraction(5, 1)
# print(f1.reduce())

# -------------------- FINGER EXERCISE LECTURE 18
# Write the class according to the specifications below:

class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        self.radius = radius

    def get_radius(self):
        """ Returns the radius of self """
        return self.radius

    def __add__(self, c):
        """ c is a Circle object 
        Returns a new Circle object whose radius is 
        the sum of self and c's radius """
        return Circle(self.radius + c.radius)

    def __str__(self):
        """ A Circle's string representation is the radius """
        return f"{self.radius}"