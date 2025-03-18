# -------------------- LECTURE 14 NOTES

# ----- Dictionaries
# def find_grades(grades, students):
#     """
#     grades is a dict mapping student names (str) to grades (str)
#     students is a list of student names
#     Returns a list containing the grades for students (in same order)
#     """
#     grades_students = [grades[name] for name in students]
    
#     return grades_students

# d = {"Ana": "B", "Matt": "C", "John": "B", "Katy": "A"}
# print(find_grades(d, ["Matt", "Katy"])) # returns ["C", "A"]

# Write a function according to these specs
# def find_in_L(Ld, k):
#     """
#     Ld is a list of dicts
#     k is an int
#     Returns True if k is a key in any dicts of Ld and False otherwise
#     """
#     flag = False
#     for dictionary in Ld:
#         if k in dictionary:
#             flag = True
#     return flag

# d1 = {1:2, 3:4, 5:6}
# d2 = {2:4, 4:6}
# d3 = {1:1, 3:9, 4:16, 5:25}

# print(find_in_L([d1, d2, d3], 2)) # returns True
# print(find_in_L([d1, d2, d3], 25)) # returns True

# # Write a function that meets this spec
# def count_matches(d):
#     """
#     d is a dict
#     Returns how many entries in d have the key equal to its value
#     """
#     counter = 0
#     for key, value in d.items():
#         if key == value:
#             counter += 1
#     return counter

# d = {1:2, 3:4, 5:6}
# print(count_matches(d)) # prints 0

# d = {1:2, "a":"a", 5:5}
# print(count_matches(d)) # prints 2

# -------------------- FINGER EXERCISE LECTURE 14
# Question 1: Implement the function that meets the specifications below:
# def keys_with_value(aDict, target):
#     """
#     aDict: a dictionary
#     target: an integer or string
#     Assume that keys and values in aDict are integers or strings.
#     Returns a sorted list of the keys in aDict with the value target.
#     If aDict does not contain the value target, returns an empty list.
#     """
#     keys = []
#     for key, value in aDict.items():
#         if value == target:
#             keys.append(key)
#     return keys

# # Examples:
# aDict = {1:2, 2:4, 5:2}
# target = 2   
# print(keys_with_value(aDict, target)) # prints the list [1,5]

# # Question 2: Implement the function that meets the specifications below:
def all_positive(d):
    """
    d is a dictionary that maps int:list
    Suppose an element in d is a key k mapping to value v (a non-empty list).
    Returns the sorted list of all k whose v elements sums up to a 
    positive value.
    """
    keys = []

    for key, value in d.items():
        if sum(value) > 0:
            keys.append(key)
    keys.sort()
    
    return keys

# Examples:
d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d))   # prints the list [1, 2]