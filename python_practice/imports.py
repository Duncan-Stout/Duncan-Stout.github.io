#import python mudules and specific funtions inside the modules 
# more import examples in imports_pt2.py
import math
from math import pi

#define classes to be imported to other files for use
class vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

class car(vehicle):
    def __init__(self, enginetype):
        super().__init__("car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype


# un-comment print tests for imports
# print("pi is ", pi)
# print("pi is ", math.pi)