# -------------------- LECTURE 12 NOTES

# ----- Lists
# What is the value returned by this expression?

# print([len(x) for x in ["xy", "abcd", 7, "4.0"] if type(x) == str])

# Step 1: what are all values in the sequence. ["xy", "abcd", 7, "4.0"]
# Step 2: which subset of values does the condition filter out?  ["xy", "abcd", "4.0"]
# Step 3: apply the function to those values. [2, 4, 3]



# -------------------- FINGER EXERCISE LECTURE 12
# Implement the function that meets the specifications below:

def count_sqrts(nums_list):
    """
    nums_list: a list
    Assumes that nums_list only contains positive numbers and that there are no duplicates.
    Returns how many elements in nums_list are exact squares of elements in the same list, including itself.
    """
    squares = [e for e in nums_list if (e ** 2) in nums_list]

    return squares
# Examples:    
print(count_sqrts([3,4,2,1,9,25])) # prints 3