# -------------------- LECTURE 10 NOTES

# ----- Lists
# What is the value of L1, L2, L3 and L at the end?
# L1 = ["re"]
# L2 = ["mi"]
# L3 = ["do"]
# L4 = L1 + L2 # ["re", "mi"]
# L3.append(L4) # ["do", ["re", "mi"]]
# L = L1.append(L3) # ["re", "do"] # <<< Some functions mutate the list and don't return anything. We use these functions for their side effect.

# print(L1)
# print(L2)
# print(L3)
# print(L4)
# print(L)

# Write a function that meets these specs:
# def make_ordered_list(n):
#     """
#     n is a positive int
#     Returns a list containing all ints in order from 0 to n (inclusive)
#     """
#     lst = []
#     for i in range(n + 1):
#         lst.append(i)

#     return lst

# print(make_ordered_list(10))

# Write a function that meets the specification.
# def remove_elem(L, e):
#     """
#     L is a list
#     Returns a new list with elements in the same order as L but without any elements equal to e.
#     """

#     new_list = []
    
#     for i in L:
#         if i != e:
#             new_list.append(i)
    
#     return new_list

# L = [1, 2, 2, 2]
# print(remove_elem(L, 2))
# print(remove_elem(L, 1))
# print(remove_elem(L, 0))

# Write a function that meets these specs:
# def count_words(sen):
#     """
#     sen is a string representing a sentence
#     Returns how many words are in s (i.e. a word is a sequence of characters between spaces.)
#     """
#     words = sen.split(" ")
    
#     return len(words)

# print(count_words("Hello it's me"))

# Write a function that meets these specs:
# def sort_words(sen):
#     """
#     sen is a string representing a sentence
#     Returns a list containing all the words in sen but sorted in alphabetical order.
#     """
#     words = sen.split(" ")
#     words.sort()

#     return words

# print(sort_words("look at this photograph"))

# -------------------- FINGER EXERCISE LECTURE 10
# Implement the function that meets the specifications below:

def all_true(n, Lf):
    """ n is an int
        Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called 
    with n as a parameter. Otherwise returns False. 
    """
    for f in Lf:
        if not f(n):
            return False
    
    return True

# Examples:    
print(all_true(2, [lambda x: x % 2 == 0, lambda x: x > 0]))