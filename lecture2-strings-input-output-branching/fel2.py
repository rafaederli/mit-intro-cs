# -------------------- LECTURE 2 NOTES

# ----- STRINGS
# What is the value of s1 and s2?
# b = ":"
# c = ") "
# s1 = b + 2 * c
# print(s1)
# f = "a"
# g = " b"
# h = "3"
# s2 = (f + g) * int(h)
# print(s2)

# s = "ABC d3f ghi"
# print(s[3:len(s)-1])
# print(s[4:0:-1])
# print(s[6:3])

# ----- INPUT/OUTPUT
# verb = input("Choose a verb: ")
# print("I can", verb, "better than you!")
# print(verb + 4 * (" " + verb))

# ----- COMPARISON
# number = 5
# guess = int(input("Choose a number: "))
# print(guess == number)

# ----- BRANCHING
# x = int(input("Enter a number for x: "))
# y = int(input("Enter a different number for y: "))
# if x == y:
#     print(x, "is the same as", y)
#     print("These are equal!")

# y = 2
# y = 20
# y = 11
# print(y)
# answer = ""
# x = 11
# if x == y:
#     answer = answer + "M"
# elif x >= y:
#     answer = answer + "i"
# else: 
#     answer = answer + "T"
# print(answer)

# number = 5
# guess = int(input("Guess a number: "))
# if guess < number:
#     print("Guess is too low")
# elif guess > number:
#     print("Guess is too high")
# else:
#     print("Guess is the same as the secret number")

# -------------------- FINGER EXERCISE LECTURE 2
number = int(input("Choose a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("zero")