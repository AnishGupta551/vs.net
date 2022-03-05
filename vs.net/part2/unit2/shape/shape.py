import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'<Shape x={self.x} y={self.y}>'

    def area(self):
        return self.x*self.y

    def perimeter(self):
        return 2*(self.x+self.y)

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __repr__(self):
        return f'<Shape x={self.x} y={self.y} radius={self.radius}>'

    def area(self):
        return math.pi*self.radius*self.radius

    def circumference(self):
        return 2*(self.radius*math.pi)

class Rectangle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)


class RightTriangle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)

    def area(self):
        return (self.x*self.y)*0.5

    def perimeter(self):
        hyp = math.sqrt((self.x*self.x+self.y*self.y))
        return hyp + self.x + self.y

class Square(Rectangle):
    def __init__(self, x, y):
        super().__init__(x, y)


# Testing out the classes


shape = Shape(20, 35)
circle = Circle(5, 10, 70)
rectangle = Rectangle(10, 15)
triangle = RightTriangle(5, 8)
square = Square(4, 4)

print("Shape")
print(shape)
print(shape.area())
print(shape.perimeter())
print()

print("Circle")
print(circle)
print(circle.area())
print(circle.circumference())
print()

print("Rectangle")
print(rectangle)
print(rectangle.area())
print(rectangle.perimeter())
print()

print("Triangle")
print(triangle)
print(triangle.area())
print(triangle.perimeter())
print()

print("Square")
print(square)
print(square.area())
print(square.perimeter())
print()

new_triangle = triangle
print("New triangle area: ", new_triangle.area())

new_square = square
print("New square area: ", new_square.area())