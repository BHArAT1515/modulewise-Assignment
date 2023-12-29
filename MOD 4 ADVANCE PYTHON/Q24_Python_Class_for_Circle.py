import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return math.pi * self.radius**2

    def compute_perimeter(self):
        return 2 * math.pi * self.radius

# Example usage:
circle_instance = Circle(3)
area = circle_instance.compute_area()
perimeter = circle_instance.compute_perimeter()
print(f"Area of the circle: {area}")
print(f"Perimeter of the circle: {perimeter}")
