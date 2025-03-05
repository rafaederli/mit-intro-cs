# -------------------- LECTURE 4 NOTES

# ----- Loops
# Write a program that loops a for loop over some range and prints how many even numbers are in that range. Try it with:
# ranges = [range(5), range(10), range(2, 9, 3), range(-4, 6, 2), range(5, 6)]
# for range in ranges:
#     counter = 0
#     for i in range:
#         if (i % 2 == 0):
#             counter += 1
#     print(counter)

# The sequence of values in a for loop isn't limited to numbers.

# Assume you are given a string of lowercase letters in variable s. Count how many unique letters there are in the string. For example, if s = "abca", then your code prints 3.
# string = "abca"
# u_letters = ""

# for letter in string:
#     if letter not in u_letters:
#         u_letters += letter
#     else:
#         pass
# print(f"Unique letters: {len(u_letters)}")

# Guess and check can't test an infinite number of values. You have to stop at some point.

# Hardcode a number as a secret number.
# Write a program that checks through all the numbers from 1 to 10 and prints the secret value if it's in that range. If it's not found, it doesn't print anything.

# secret_number = 4
# found = False
# for i in range(10 + 1):
#     if (i == secret_number):
#         print(f"Your number is {i}")
#     else:
#         pass

# How does the program look if I change the requirement to be: If it's not found, prints that it didn't find it.

# for i in range(10 + 1):
#     if (i == secret_number):
#         found = True

# if found:
#     print("The number was found")
# else:
#     print("The number was not found")

# Booleans can be used as signals that something happened. We call them Boolean flags.

# Operations on some floats introduces a very small error. The small error can have a big effect if operations are done many times!

# -------------------- FINGER EXERCISE LECTURE 4

N = 27

for i in range(abs(N) + 1):
    if (i ** 3 > abs(N)):
        print("Error: It is not a perfect cube.")
        break
    else:
        if (i ** 3 == abs(N)):
            if (N < 0):
                print(f"Cube root: {-i}")
                break
            else:
                print(f"Cube root: {i}")
                break