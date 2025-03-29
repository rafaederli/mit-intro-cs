# -------------------- LECTURE 16 NOTES

# ----- Recursion on Non Numerics
# Modify the code we wrote to return the total length of all strings inside L:
# def total_len_recur(L):
#     if len(L) == 1:
#         return len(L[0])
#     else:
#         return len(L[0]) + total_len_recur(L[1:])
    
# test = ["ab", "c", "defgh"]
# print(total_len_recur(test)) # prints 8

# Write a recursive function according to the specs below.
def in_list_of_lists(L, e):
    """
    L is a list whose elements are lists containing ints.
    Returns True if e is an element within the lists of L and False otherwise
    """
    if (e in L[0]):
        return True
    else:
        if len(L) > 1:
            return in_list_of_lists(L[1:], e)
        else:
            return False
        
test = [[1, 2], [3, 4], [5, 6, 7]]
print(in_list_of_lists(test, 0)) # Prints False
print(in_list_of_lists(test, 3)) # Prints True

# -------------------- FINGER EXERCISE LECTURE 16
# 