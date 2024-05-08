import math

class Shape:
    
     def circle_area(self, radius):
        return math.pi * self.radius ** 2

     def rectangle_area(self, length, width):
        return self.length * self.width

     def triangle_area(self, base, height):
        return 0.5 * self.base * self.height

    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.circle_area(self.radius)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.rectangle_area(self.length, self.width)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
         return self.triangle_area(self.base, self.height)

def main():
    choice = input("Enter shape (circle, rectangle, triangle): ")

    if choice == "circle":
        radius = float(input("Enter the Radius of the circle: "))
        circle = Circle(radius)
        area = circle.calculate_area()
        print("Area of the Circle:", area)

    elif choice == "rectangle":
        length = float(input("Enter the length of the Rectangle: "))
        width = float(input("Enter the width of the Rectangle: "))
        rectangle = Rectangle(length, width)
        area = rectangle.calculate_area()
        print("Area of the Rectangle:", area)

    elif choice == "triangle":
        base = float(input("Enter the Base of the Triangle: "))
        height = float(input("Enter the Height of the triangle: "))
        triangle = Triangle(base, height)
        area = triangle.calculate_area()
        print("Area of the Triangle:", area)

    else:
        print("Invalid Shape Choice!")

if __name__ == "__main__":
    main()

