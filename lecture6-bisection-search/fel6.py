# -------------------- LECTURE 6 NOTES

# ----- Bisection Search
# Write code to do bisection search to find the cube root of positive cubes within some epsilon. Start with
# cube = 27
# epsilon = 0.01
# low = 0
# high = cube

# guess = (high + low) / 2

# while (abs(guess ** 3 - cube) > epsilon):
#     if (guess ** 3 > cube):
#         high = guess
#     else:
#         low = guess
#     guess = (high + low) / 2

# print(guess)

# -------------------- FINGER EXERCISE LECTURE 6
# Assume you are given an integer 0 \<= N \\<= 1000.
# Write a piece of Python code that uses bisection search to guess N.
# The code prints two lines: count: with how many guesses it took to find N, and answer: with the value of N.
# Hints: If the halfway value is exactly in between two integers, choose the smaller one.

N = 354
counter = 0
low = 0
high = 1001
guess = (high + low) // 2 # If the middle value is exactly between two integers, we must choose the smaller one. I use the '//' operator to return the smaller integer (rounding dow)
while guess != N: # Because we are guessing integers, not floats, I compared the guessed value directly with N.
    if (guess < N):
        low = guess
    else:
        high = guess
    counter += 1
    guess = (high + low) // 2
print(f"count: {counter}")
print(f"answer: {guess}")