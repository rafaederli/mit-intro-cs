# -------------------- LECTURE 13 NOTES

# ----- Exceptions
# def pairwise_div(Lnum, Ldenom):
#     """
#     Lnum and Ldenom are non-empty lists of equal lengths containing numbers
    
#     Returns a new list whose elements are the pairwise division of an element in Lnum by an element in Ldenom.

#     Raise a ValueError if Ldenom contains 0.
#     """

#     if 0 not in Ldenom:
#         div = [(Lnum[i] / Ldenom[i]) for i in range(len(Lnum))]
#     else:
#         raise ValueError("Ldenom contains 0")
    
#     return div

# # L1 = [4, 5, 6]
# # L2 = [1, 2, 3]
# # print(pairwise_div(L1, L2))

# L1 = [4, 5, 6]
# L2 = [1, 0, 3]
# print(pairwise_div(L1, L2))

# def pairwise_div(Lnum, Ldenom):
#     """
#     Lnum and Ldenom are non-empty lists of equal lenths containing numbers
#     Returns a new list whose elements are the pairwise division of an element in Lnum by an element in Ldenom.
#     Raise a ValueError if Ldenom contains 0.
#     """

#     assert len(Lnum) != 0, "Lnum is an empty list"
#     assert len(Ldenom) !=0, "Ldemon is an empty list"
#     assert len(Lnum) == len(Ldenom), "Lnum and Ldenom are lists of different lengths"

#     if 0 not in Ldenom:
#         div = [(Lnum[i] / Ldenom[i]) for i in range(len(Lnum))]
#     else:
#         raise ValueError("Ldenom contains 0")
    
#     return div

# L1 = []
# L2 = [1, 2, 3]
# print(pairwise_div(L1, L2))

# L1 = [4, 5, 6]
# L2 = []
# print(pairwise_div(L1, L2))

# L1 = [4, 5, 6]
# L2 = [1, 2]
# print(pairwise_div(L1, L2))

# L1 = [4, 5, 6]
# # L2 = [1, 0, 3]
# # print(pairwise_div(L1, L2))

# L1 = [4, 5, 6]
# L2 = [1, 2, 3]
# print(pairwise_div(L1, L2))

# -------------------- FINGER EXERCISE LECTURE 13
# Implement the function that meets the specifications below:

def sum_str_lengths(L):
    """
    L is a non-empty list containing either: 
    * string elements or 
    * a non-empty sublist of string elements
    Returns the sum of the length of all strings in L and 
    lengths of strings in the sublists of L. If L contains an 
    element that is not a string or a list, or L's sublists 
    contain an element that is not a string, raise a ValueError.
    """
    # Your code here  

    counter = 0
    def count_strings(lst):
        c = 0
        for element in lst:
            if type(element) is str:
                for char in element:
                    c += 1
            else:
                raise ValueError
        return c
    
    for element in L:
        if type(element) is str:
            for char in element:
                counter += 1
        elif type(element) is list:
            counter += count_strings(element)
        else:
            raise ValueError
    return counter

# Examples:
print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError