# -------------------- LECTURE 20 NOTES

from dateutil import parser

class Workout(object):
    """A class to keep track of workouts"""

    # Class variable to compute calories burned from workout time
    cal_per_hr = 200
    
    def __init__(self, start, end, calories=None):
        """Creates a workout class;  start and end are strings representing
        the start and end time (e.g., "1/1/2021 1:23 PM");  
        calories is an optional float specifying the calories burned 
        in the workout"""
        # note use of dateutil.parser to convert strings to datetime objects
        self.start = parser.parse(start)  
        self.end = parser.parse(end)
        self.icon = '😓'
        self.kind = 'Workout'
        self.calories = calories

    def get_calories(self):
        """Return the total calories burned in the workout"""
        if (self.calories == None):
            # calc the calories based on the length of the workout and cal_per_hr
            return Workout.cal_per_hr * (self.end - self.start).total_seconds() / 3600.0
        else:
            return self.calories

    def get_duration(self):
        """Return the duration of the workout, as a datetime.interval object"""
        return self.end-self.start

    def get_start(self):
        """Return the start time of the workout, as a datetime.datetime object"""
        return self.start

    def get_end(self):
        """Return the end time of the workout, as a datetime.datetime object"""
        return self.end

    def set_calories(self, calories):
        """Set the calories of the workout to calories"""
        self.calories = calories

    def set_start(self, start):
        """Set the start time of the workout to the supplied start string"""
        self.start = parser.parse(start)

    def set_end(self, end):
        """Set the start time of the workout to the supplied start string"""
        self.end = parser.parse(end)

    def get_kind(self):
        """Return the kind of the workout as a string"""
        return self.kind

    def __eq__(self, other):
        """Returns true if this workout is equal to another workout, false o.w."""
        # the \ breaks up the line
        return type(self) == type(other) and \
                self.start == other.start and \
                self.end == other.end and \
                self.kind == other.kind and \
                self.get_calories() == other.get_calories()

    def __str__(self):
        """Return a text-based graphical depiction of the workout"""
        width = 16
        retstr =  f"|{'–'*width}|\n"
        retstr += f"|{' ' *width}|\n"
        retstr += f"| {self.icon}{' '*(width-3)}|\n"  #assume width of icon is 2 chars - len('🏃🏽‍♀️');  doesn't do what you'd epxect
        retstr += f"| {self.kind}{' '*(width-len(self.kind)-1)}|\n"
        retstr += f"|{' ' *width}|\n"
        duration_str = str(self.get_duration())
        retstr += f"| {duration_str}{' '*(width-len(duration_str)-1)}|\n"
        cal_str = f"{round(self.get_calories(),1)}"
        retstr += f"| {cal_str} Calories {' '*(width-len(cal_str)-11)}|\n"

        retstr += f"|{' ' *width}|\n"
        retstr +=  f"|{'_'*width}|\n"

        return retstr

# w_one = Workout('Jan 1 2021 3:30 PM', 'Jan 1 2021 4:00 PM')
# print(w_one.get_calories())
# w_two = Workout('Jan 1 2021 3:30 PM', 'Jan 1 2021 4:00 PM', 300)
# print(w_two.get_calories())



# -------------------- FINGER EXERCISE LECTURE 20
# 