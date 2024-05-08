import math

class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def calculate_area(self):
        radius = float(input("Enter the Radius of the circle: "))
        return math.pi * radius ** 2

class Rectangle(Shape):
    def calculate_area(self):
        length = float(input("Enter the length of the Rectangle: "))
        width = float(input("Enter the width of the Rectangle: "))
        return length * width

class Triangle(Shape):
    def calculate_area(self):
        base = float(input("Enter the Base of the Triangle: "))
        height = float(input("Enter the Height of the triangle: "))
        return 0.5 * base * height

def main():
    shape_type = input("Enter Shape type (Circle, Rectangle, Triangle): ").lower()

    if shape_type == "circle":
        shape = Circle()
    elif shape_type == "rectangle":
        shape = Rectangle()
    elif shape_type == "triangle":
        shape = Triangle()
    else:
        print("Invalid Shape")
        return

    area = shape.calculate_area()
    print("Area:", area)

if __name__ == "__main__":
    main()


