"""
File: check07b.py
Author: Br. Burton

Demonstrates abstract base classes.
"""

#TODO: Import anything you need for Abstract Base Classes / methods
from abc import ABC, abstractmethod
import math

#TODO: convert this to an ABC
class Shape(ABC):
    def __init__(self):
        self.name = ""
        super().__init__()

    #TODO: Add an abstractmethod here called get_area
    @abstractmethod
    def get_area(self):
        pass
    
    def display(self):
        print("{} - {:.2f}".format(self.name, self.get_area()))

#TODO: Create a Circle class here that derives from Shape
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.name = "Circle"
        self.radius = 0.0
        
    def get_area(self):
        area = math.pi * self.radius ** 2
        return area

#TODO: Create a Rectangle class here that derives from Shape
class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.name = "Rectangle"
        self.width = 0.0
        self.length = 0.0
        
    def get_area(self):
        area = self.width * self.length
        return area

def main():

    #TODO: Declare your list of shapes here
    shapes = []
    command = ""

    while command != "q":
        command = input("Please enter 'c' for circle, 'r' for rectangle or 'q' to quit: ")

        if command == "c":
            radius1 = float(input("Enter the radius: "))
            #TODO: Declare your Circle here, set its radius, and
            # add it to the list
            circle1 = Circle(radius1)
            shapes.append(circle1)
        
        elif command == "r":
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            #TODO: Declare your Rectangle here, set its length
            # and width, and add it to the list
            rectangle1 = Rectangle(width, length)
            shapes.append(rectangle1)

    # Done entering shapes, now lets print them all out:

    #TODO: Loop through each shape in the list, and call its display function
    for shape in shapes:
        shape.display()

if __name__ == "__main__":
    main()
