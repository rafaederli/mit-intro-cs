# -------------------- FINGER EXERCISE LECTURE 5
# Assume you are given a string variable named my_str. Write a piece of Python code that prints out a new string containing the even indexed characters of my_str. For example, if my_str = "abcdefg" then your code should print out aceg.

my_string = "abcdefg"
even_index = ""

for i in range(len(my_string)):
    if (i % 2 == 0):
        even_index += my_string[i]
    else:
        pass

print(even_index)