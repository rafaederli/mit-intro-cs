# -------------------- LECTURE 9 NOTES

# ----- Lambda Functions
# What does this print?
# def do_twice(n, fn):
#     return fn(fn(n))

# print(do_twice(3, lambda x: x**2)) # 81

# ----- Tuples
# Write a function that meets these specs:
# Hint: remember how to check if a character is in a string?

# def char_counts(s):
#     """
#     s is a string of lowercase chars
#     Return a tuple where the first element is the number of vowels in s and the second element is the number of consonants in s
#     """
#     vowels = 0
#     consonants = 0
#     for char in s:
#         if char in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1
#     return (vowels, consonants)

# print(char_counts("abcd"))
# print(char_counts("zcght"))

# Write a function that meets these specs:
# def sum_and_prod(L):
#     """
#     L is a list of numbers
#     Return a tuple where the first value is the sum of all elementsin L and the second value is the product of all elements in L
#     """
#     add = 0
#     mult = 1
#     for i in L:
#         add += i
#         mult *= i
#     return (add, mult)

# print(sum_and_prod([1, 2, 3, 4]))

# -------------------- FINGER EXERCISE LECTURE 9
# Implement the function that meets the specifications below:

def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assumes tA and tB are the same length.
    Returns a tuple where the:
    * first element is the length of one of the tuples
    * second element is the sum of the pairwise products of tA and tB
    """
    # Your code here
    length = len(tA)
    add_mult = 0
    for i in range(length):
        add_mult += tA[i] * tB[i]
    return (length, add_mult)

# Examples:
tA = (1, 2, 3)
tB = (4, 5, 6)
print(dot_product(tA, tB)) # prints (3,32)