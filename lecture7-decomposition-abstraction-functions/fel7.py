# -------------------- LECTURE 7 NOTES

# ----- Functions
# Write a code that satisfies the following specs
# def div_by(n, d):
#     """
#     n and d are ints > 0
#     Returns True if d divides n evenly and False otherwise
#     """
#     return (n % d == 0)

# print(div_by(10, 3))
# print(div_by(195, 13))

# Write code that satisfies the following specs
# def is_palindrome(s):
#     """
#     s is a string
#     Returns True if s is a palindrome and False otherwise
#     """
#     it_is = True

#     for i in range(len(s)):
#         if s[i] != s[len(s) - 1 - i]:
#             it_is = False
    
#     return it_is

# print(is_palindrome("2222"))

# -------------------- FINGER EXERCISE LECTURE 7
# Question 1: Implement the function that meets the specifications below:
def eval_quadratic(a, b, c, x):
    """
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    Returns the value of the quadratic ax² + bx + c.
    """
    equation = (a * (x ** 2) + b * x + c)
    return equation

# Examples:    
print(eval_quadratic(1, 1, 1, 1)) # prints 3

# Question 2: Implement the function that meets the specifications below:
def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    """
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    Evaluates one quadratic with coefficients a1, b1, c1, at x1.
    Evaluates another quadratic with coefficients a2, b2, c2, at x2.
    Prints the sum of the two evaluations. Does not return anything.
    """
    equation1 = (a1 * (x1 ** 2) + b1 * x1 + c1)
    equation2 = (a2 * (x2 ** 2) + b2 * x2 + c2)
    eq_sum = equation1 + equation2
    return eq_sum

# Examples:    
two_quadratics(1, 1, 1, 1, 1, 1, 1, 1) # prints 6
print(two_quadratics(1, 1, 1, 1, 1, 1, 1, 1)) # prints 6 then None