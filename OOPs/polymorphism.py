class shape:
    def area(self):
        pass
class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
class Rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def calculate_area(shape: shape):
    return shape.area()
circle = Circle(3)
rectangle = Rectangle(7, 3)

print(calculate_area(circle))
print(calculate_area(rectangle))