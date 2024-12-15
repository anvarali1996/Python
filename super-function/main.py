import math
class Shape:
    def __init__(self, color, is_filled) -> None:
        self.color = color
        self.is_filled = is_filled
        
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius) -> None:
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {math.pi * self.radius * self.radius:.4f} cm2")
        return super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width) -> None:
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a Square with an area of { self.width * self.width:.2f} cm2")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height) -> None:
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a Triangle with an area of {self.width * self.height / 2:.2f} cm2")
        return super().describe()


circle = Circle("red", True, 5)
square = Square("blue", False, 6.21)
triangle = Triangle("green", True, 9, 12.5)
circle.describe()
square.describe()
triangle.describe()

# print(triangle.width)
