# -------------------- LECTURE 11 NOTES

# ----- Lists
# Write a function that meets the specification.
# def remove_all(L, e):
#     """
#     L is a list
#     Mutates L to remove all elements in L that are equal to e
#     Returns None
#     """

#     L_copy = L[:]
#     L.clear()

#     for element in L_copy:
#         if element != e:
#             L.append(element)

#     return L

# L = [1, 2, 2, 2]
# remove_all(L, 2)
# print(L)

# -------------------- FINGER EXERCISE LECTURE 11
# Implement the function that meets the specifications below:

def remove_and_sort(Lin, k):
    """ Lin is a list of ints
        k is an int >= 0
    Mutates Lin to remove the first k elements in Lin and 
    then sorts the remaining elements in ascending order.
    If you run out of items to remove, Lin is mutated to an empty list.
    Does not return anything.
    """
    Lin.pop(0)
    Lin.sort()

# Examples:
L = [1,6,3]
k = 1
remove_and_sort(L, k)
print(L)   # prints the list [3, 6]