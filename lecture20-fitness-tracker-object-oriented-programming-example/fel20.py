# -------------------- LECTURE 20 NOTES

# from dateutil import parser

# class Workout(object):
#     """A class to keep track of workouts"""

#     # Class variable to compute calories burned from workout time
#     cal_per_hr = 200
    
#     def __init__(self, start, end, calories=None):
#         """Creates a workout class;  start and end are strings representing
#         the start and end time (e.g., "1/1/2021 1:23 PM");  
#         calories is an optional float specifying the calories burned 
#         in the workout"""
#         # note use of dateutil.parser to convert strings to datetime objects
#         self.start = parser.parse(start)  
#         self.end = parser.parse(end)
#         self.icon = '😓'
#         self.kind = 'Workout'
#         self.calories = calories

#     def get_calories(self):
#         """Return the total calories burned in the workout"""
#         if (self.calories == None):
#             # calc the calories based on the length of the workout and cal_per_hr
#             return Workout.cal_per_hr * (self.end - self.start).total_seconds() / 3600.0
#         else:
#             return self.calories

#     def get_duration(self):
#         """Return the duration of the workout, as a datetime.interval object"""
#         return self.end-self.start

#     def get_start(self):
#         """Return the start time of the workout, as a datetime.datetime object"""
#         return self.start

#     def get_end(self):
#         """Return the end time of the workout, as a datetime.datetime object"""
#         return self.end

#     def set_calories(self, calories):
#         """Set the calories of the workout to calories"""
#         self.calories = calories

#     def set_start(self, start):
#         """Set the start time of the workout to the supplied start string"""
#         self.start = parser.parse(start)

#     def set_end(self, end):
#         """Set the start time of the workout to the supplied start string"""
#         self.end = parser.parse(end)

#     def get_kind(self):
#         """Return the kind of the workout as a string"""
#         return self.kind

#     def __eq__(self, other):
#         """Returns true if this workout is equal to another workout, false o.w."""
#         # the \ breaks up the line
#         return type(self) == type(other) and \
#                 self.start == other.start and \
#                 self.end == other.end and \
#                 self.kind == other.kind and \
#                 self.get_calories() == other.get_calories()

#     def __str__(self):
#         """Return a text-based graphical depiction of the workout"""
#         width = 16
#         retstr =  f"|{'–'*width}|\n"
#         retstr += f"|{' ' *width}|\n"
#         retstr += f"| {self.icon}{' '*(width-3)}|\n"  #assume width of icon is 2 chars - len('🏃🏽‍♀️');  doesn't do what you'd epxect
#         retstr += f"| {self.kind}{' '*(width-len(self.kind)-1)}|\n"
#         retstr += f"|{' ' *width}|\n"
#         duration_str = str(self.get_duration())
#         retstr += f"| {duration_str}{' '*(width-len(duration_str)-1)}|\n"
#         cal_str = f"{round(self.get_calories(),1)}"
#         retstr += f"| {cal_str} Calories {' '*(width-len(cal_str)-11)}|\n"

#         retstr += f"|{' ' *width}|\n"
#         retstr +=  f"|{'_'*width}|\n"

#         return retstr

# # w_one = Workout('Jan 1 2021 3:30 PM', 'Jan 1 2021 4:00 PM')
# # print(w_one.get_calories())
# # w_two = Workout('Jan 1 2021 3:30 PM', 'Jan 1 2021 4:00 PM', 300)
# # print(w_two.get_calories())

# class RunWorkout(Workout):
#     def __init__(self, start, end, elev=0, calories=None):
#         super().__init__(start, end, calories)
#         self.icon = "🏃"
#         self.kind = "Running"
#         self.elev = elev
    
#     def get_elev(self):
#         return self.elev
#     def set_elev(self, e):
#         self.elev = e

# -------------------- FINGER EXERCISE LECTURE 20
# In this problem, you will implement two classes according to the specification below: one Container class and one Queue class (a subclass of Container).     

# Our Container class will initialize an empty list. The two methods we will have are to calculate the size of the list and to add an element. The second method will be inherited by the subclass. We now want to create a subclass so that we can add more functionality – the ability to remove elements from the list. A Queue will add elements to the list in the same way, but will behave differently when removing an element.

# A queue is a first-in, first-out data structure. Think of a store checkout queue. The customer who has been in the line the longest gets the next available cashier. When implementing your Queue class, you will have to think about which end of your list contains the element that has been in the list the longest. This is the element you will want to remove and return.

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

class Queue(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The oldest element in the container list is removed
        Returns the element removed or None if the stack contains no elements
        """
        if self.size() == 0:
            return None
        return self.myList.pop(0)