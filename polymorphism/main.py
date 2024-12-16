from abc import ABC, abstractmethod

import math
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return math.pi * self.radius **2
    
class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side

    def area(self):
        return self.side ** 2
    
class Triangle(Shape):
    def __init__(self, base, height) -> None:
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5
    
class Pizza(Circle): 
    def __init__(self, topping, radius) -> None:
        super().__init__(radius)
        self.topping = topping
        

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("Pepperoni", 15)]

for shape in shapes:
    print(f"{shape.area():.2f}")


# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2
    
# class Square(Shape):
#     def __init__(self, side) -> None:
#         self.side = side

#     def area(self):
#         return self.side ** 2
    
# class Triangle(Shape):
#     def __init__(self, base, height) -> None:
#         self.base = base
#         self.height = height

#     def area(self):
#         return self.base * self.height * 0.5
    
# class Pizza(Circle): 
#     def __init__(self, topping, radius) -> None:
#         super().__init__(radius)
#         self.topping = topping

# shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("Pepperoni", 15)]

# for shape in shapes:
#     print(f"{shape.__class__.__name__} area: {shape.area():.2f}")
