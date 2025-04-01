# -------------------- LECTURE 18 NOTES

# ----- Classes
# Write a function that meets this spec.

# class Animal(object):
#     def __init__(self, age):
#         self.age = age
#         self.name = None

#     def __str__(self):
#         return f"animal: {self.name} {self.age}"
#     def get_age(self):
#         return self.age
#     def get_name(self):
#         return self.name
#     def set_age(self, newage):
#         self.age = newage
#     def set_name(self, newname=""):
#         self.name = newname

# def make_animals(L1, L2):
#     """
#     L1 is a list of ints and L2 is a list of str
#     L1 and L2 have the same length
#     Creates a list of Animals the same lenght as L1 and L2
#     An animal object at index i has the age and name corresponding to the same index in L1 and L2, respectively
#     """
#     L3 = []
#     for i in range(len(L1)):
#         animal = Animal(L1[i])
#         animal.set_name(L2[i])
#         L3.append(animal)
#     return L3

# # For example:
# L1 = [2, 5, 1]
# L2 = ["blobfish", "crazyant", "parafox"]
# animals = make_animals(L1, L2)
# print(animals) # This prints a list of animal objects
# for i in animals:
#     print(i)

# class Animal(object):
#     def __init__(self, age):
#         self.age = age
#         self.name = None

#     def __str__(self):
#         return f"animal: {self.name} {self.age}"
#     def get_age(self):
#         return self.age
#     def get_name(self):
#         return self.name
#     def set_age(self, newage):
#         self.age = newage
#     def set_name(self, newname=""):
#         self.name = newname

# class Cat(Animal):
#     def speak(self):
#         print("meow")
#     def __str__(self):
#         return f"cat: {self.name} : {self.age}"

# class Person(Animal):
#     def __init__(self, name, age):
#         Animal.__init__(self, age)
#         self.set_name(name)
#         self.friends = []
#     def get_friends(self):
#         return self.friends.copy()
#     def add_friends(self, fname):
#         if fname not in self.friends:
#             self.friends.append(fname)
#     def speak(self):
#         print("hello")
#     def age_diff(self, other):
#         diff = self.age - other.age
#         print(abs(diff), "year difference")
#     def __str__(self):
#         return f"person: {self.name} : {self.age}"

# Write a function according to this spec:
# def make_pets(d):
#     """
#     d is a dict mapping a Person obj to a Cat obj
#     Prints, on each line, the name of a person, a colon, and the name of that person's cat
#     """
#     for person, cat in d.items():
#         print(f"{person.get_name()}: {cat.get_name()}")

# p1 = Person("ana", 86)
# p2 = Person("james", 7)
# c1 = Cat(1)
# c1.set_name("furball")
# c2 = Cat(1)
# c2.set_name("fluffsphere")

# d = {p1:c1, p2:c2}

# make_pets(d)

# import random

# class Student(Person):
#     def __init__(self, name, age, major=None):
#         super().__init__(name, age)

# -------------------- FINGER EXERCISE LECTURE 19
# In this problem, you will implement two classes according to the specification below: one Container class and one Stack class (a subclass of Container).

# Our Container class will initialize an empty list. The two methods we will have are to calculate the size of the list and to add an element. The second method will be inherited by the subclass. We now want to create a subclass so that we can add more functionality—the ability to remove elements from the list. A Stack will add elements to the list in the same way, but will behave differently when removing an element.

# A stack is a last-in, first-out data structure. Think of a stack of pancakes. As you make pancakes, you create a stack of them with older pancakes going on the bottom and newer pancakes on the top. As you start eating the pancakes, you pick one off the top so you are removing the newest pancake added to the stack. When implementing your Stack class, you will have to think about which end of your list contains the element that has been in the list the shortest amount of time. This is the element you will want to remove and return

class Container(object):
    """
    A container object is a list and can store elements of any type
    """
    def __init__(self):
        """
        Initializes an empty list
        """
        self.myList = []

    def size(self):
        """
        Returns the length of the container list
        """
        return len(self.myList)

    def add(self, elem):
        """
        Adds the elem to one end of the container list, keeping the end
        you add to consistent. Does not return anything
        """
        self.myList.append(elem)

class Stack(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The newest element in the container list is removed
        Returns the element removed or None if the queue contains no elements
        """
        self.myList.pop()