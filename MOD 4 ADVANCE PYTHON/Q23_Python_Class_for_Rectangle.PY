class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

# Example usage:
rectangle_instance = Rectangle(5, 7)
area = rectangle_instance.compute_area()
print(f"Area of the rectangle: {area}")
