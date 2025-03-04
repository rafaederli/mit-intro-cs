# -------------------- LECTURE 3 NOTES

# ----- WHILE
# While loops can repeat code inside indefinitely! Sometimes they need your intervention to end the program.

# What is printed when you type "RIGHT"?
# where = input("Go left or right? ")
# while where == "right":
#     where = input("Go left or right? ")
# print("You got out!")

# while True:
#     print("nooooooooooooo")

# Expand this code to show a sad face when the user entered the while loop more than 2 times.
# Hint: use a variable as a counter

# where = input("Go left or right? ")
# counter = 0
# while (where == "right"):
#     counter = counter + 1
#     if (counter > 2):
#         print(":(")
#     where = input("Go left or right? ")
# print("You got out!")

# For loops only repeat for however long the sequence is. The loop variables takes on these values in order.
# What do these print?
# for i in range(1, 4, 1):
#     print(i)
# for j in range(1, 4, 2):
#     print(j)
# for me in range(4, 0, -1):
#     print("$" * me)

# Fix this code to use variables start and end in the range, to get the total sum between and including those values.
# For example, if start=3 and end=5 then the sum should be 12.
# mysum = 0
# start = 3
# end = 5
# for i in range(start, end + 1):
#     mysum += i
# print(mysum)

# -------------------- FINGER EXERCISE LECTURE 3
# N = 5
# while N > 0:
#     print("hello world")
#     N = N - 1

for N in range(5):
    print("hello world")