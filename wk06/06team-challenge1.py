"""
A point has coordinates x and y
"""
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    """
    get x and y coordinates from user
    """
    def prompt_for_point(self):
        self.x = float(input("Enter x: "))
        self.y = float(input("Enter y: "))
        center = "({}, {})".format(self.x, self.y)
        return center

    """
    display point coordinates in this format: (0,0)
    """
    def display(self):
        print("({}, {})".format(self.x, self.y))


"""
A circle has a center using x and y coordinates from point class and a radius
"""


class Circle:
    def __init__(self, center, radius=1.0):
        center = Point()
        self.center = center
        self.radius = radius

    """
    get center of circle coordinates from user
    """
    def prompt_for_circle(self):
        self.center = Point.prompt_for_point()
        self.radius = float(input("Enter radius: "))
        return self.center, self.radius

    """
    display circle information
    """
    def display(self):
        print("Center:")
        Point().display()
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
    circle1.display()


if __name__ == '__main__':
    main()
