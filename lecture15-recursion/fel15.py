# -------------------- LECTURE 15 NOTES

# ----- Recursion
# Complete the function that calculates nº for variables n and p
# def power_recur(n, p):
#     if p == 0:
#         return 1
#     elif p == 1:
#         return n
#     else:
#         return n * power_recur(n, p-1)
    
# print(power_recur(2,3)) # prints 8

# -------------------- FINGER EXERCISE LECTURE 15
# Implement the function that meets the specifications below:

def recur_power(base, exp):
    """
    base: int or float.
    exp: int >= 0

    Returns base to the power of exp using recursion.
    Hint: Base case is when exp = 0. Otherwise, in the recursive
    case you return base * base^(exp-1).
    """
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * recur_power(base, exp - 1)

# Examples:
print(recur_power(2,5))  # prints 32