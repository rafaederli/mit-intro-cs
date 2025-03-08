# -------------------- LECTURE 8 NOTES

# ----- Functions
# What is printed if you run this code as a file?
# def add(x, y):
#     return (x + y)
# def mult(x, y):
#     return (x * y)

# add(1, 2) # Nothing
# print(add(2, 3)) # 5
# mult(3, 5) # Nothing
# print(mult(3, 5)) # 15

# Fix the code that tries to write this function
# def is_triangular(n):
#     """
#     n is an int > 0
#     Returns True if n in triangular, i.e. equals a continued summation of natural numbers (1 + 2 + 3 + ... + k), False otherwise
#     """
#     total = 0
#     for i in range(n + 1):
#         if total == n:
#             return True
#     return False

# Functions support modularity
# def bisection_root(x):
#     epsilon = 0.01
#     low = 0
#     high = x
#     ans = (high + low) / 2.0
#     while (abs(ans ** 2 - x) >= epsilon):
#         if ans ** 2 < x:
#             low = ans
#         else:
#             high = ans
#         ans = (high + low) / 2.0
#     return ans

# # print(bisection_root(4))
# # print(bisection_root(123))

# # Write a function that satisfies the following specs. Use bisection_root we already wrote to get an approximation for the sqrt of an integer. For example: print(count_nums_with_sqrt_close_to(10, 0.1)) prints 4 because all these integers have a sqrt within 0.1.

# def count_nums_with_sqrt_close_to (n, epsilon):
#     """
#     n is an int > 2
#     epsilon is a positive number < 1
#     Returns how many integers have a square root within epsilon of n
#     """
#     count = 0
#     for i in range(n ** 3):
#         if abs(bisection_root(i) - n) < epsilon:
#             print(f"sqrt of {i} is {bisection_root(i)}")
#             count += 1
#     return count

# print(count_nums_with_sqrt_close_to(10, 0.1))
# print(count_nums_with_sqrt_close_to(10, 1.0))

# Do a similar with the function call
# def calc(op, x, y):
#     return op(x, y)

# def div(a, b):
#     if b != 0:
#         return a / b
#     print("Denom was 0.")

# res = calc(div, 2, 0) # None

# print(res)

# Write a function that meets these specs
# def is_even(x):
#     return x % 2 == 0

# def apply(criteria, n):
#     """
#     * criteria is a func takes in a number and returns a bool
#     * n is an int
#     Returns how many ints from 0 to n (inclusive) match the criteria (i.e. return True when run with criteria)
#     """
#     count = 0
#     for i in range(n + 1):
#         if criteria(i):
#             count += 1
#     return count

# how_many = apply(is_even, 10)
# print(how_many)

# -------------------- FINGER EXERCISE LECTURE 8
# Implement the function that meets the specifications below:

def same_chars(s1, s2):
    """
    s1 and s2 are strings
    Returns boolean True is a character in s1 is also in s2, and vice 
    versa. If a character only exists in one of s1 or s2, returns False.
    """

    for char in s1:
        if char not in s2:
            return False

    for char in s2:
        if char not in s1:
            return False

    return True

# Examples:
print(same_chars("abc", "cab"))     # prints True
print(same_chars("abccc", "caaab")) # prints True
print(same_chars("abcd", "cabaa"))  # prints False
print(same_chars("abcabc", "cabz")) # prints False