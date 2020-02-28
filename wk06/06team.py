"""
A point has coordinates x and y
"""
class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y
        
    """
    get x and y coordinates from user
    """
    def prompt_for_point(self):        
        self.x = input("Enter x: ")
        self.y = input("Enter y: ")
        
    """
    display point coordinates in this format: (0,0)
    """
    def display(self):
        print("({}, {})".format(self.x, self.y))
        
"""
A circle has a center using x and y coordinates from point class and a radius
"""
class Circle(Point):
    def __init__(self, radius = 1.0):
        super().__init__()
        self.radius = radius    
     
    """
    get center of circle coordinates from user
    """
    def prompt_for_circle(self):
        super().prompt_for_point()
        self.radius = input("Enter radius: ")
        return self.x, self.y, self.radius
        
    """
    display circle information
    """
    def display(self):
        super().display()
        print("Radius: {}".format(self.radius))
 
 
"""
create a point, prompt for user entry,
  display what was entered, repeat for circle
"""
def main():
    point1 = Point()
    print("Point:")
    point1.prompt_for_point()
    print()
    point1.display()
    print()
    circle1 = Circle()
    circle1.prompt_for_circle()
    print()
    print("Center:")
    circle1.display()
        
  
if __name__ == '__main__':
    main()      