# -------------------- LECTURE 1 NOTES

# ----- TYPES
# print(type(1234))
# print(type(8.99))
# print(type(9.0))
# print(type(True))
# print(type(False))

# print(type(float(123)))
# print(type(round(7.9)))
# print(type(float(round(7.2))))
# print(type(int(7.2)))
# print(type(int(7.9)))

# ----- EXPRESSIONS
# Python replace complex expressions by one value and it works systematically to evaluate the expression.
# print((13-4)/(12*12))
# print(type(4*3))
# print(type(4.0*3))
# print(int(1/2))

# ----- VARIABLES
# Lines are evaluated one after the other, no skipping around, yet.
# x = 6 (y)
# 6 = x (n)
# x*y = 3+4 (n)
# xy = 3+4 (y)

# These 3 lines are eecuted in order. What are the values of meters and feet variables at each line in the code?
# meters = 100
# print('line 1: meters =', meters)
# feet = 3.2808 * meters
# print('line 2: feet =', feet)
# meters = 200
# print('line 3: meters =', meters)

# Swap values of x and y without binding the numbers directly. Debug (aka fix) this code.
# x = 1
# y = 2
# print('x =', x)
# print('y =', y)
# temp = y # using a temporary variable
# y = x
# print('y =', y)
# x = temp
# print('x =', x)

# -------------------- FINGER EXERCISE LECTURE 1
a = 1
b = 2
c = 3
total = (a + b) * c
print(total)