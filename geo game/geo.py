from random import randint


class Point:
    def __init__(self, x, y):
        # Initialize Point object with x and y coordinates
        self.x = x
        self.y = y

    def inside_rectangle(self, rectangle):
        # Check if the Point is within the specified rectangle
        if (
            rectangle.point1.x < self.x < rectangle.point2.x
            and rectangle.point1.y < self.y < rectangle.point2.y
        ):
            return True
        else:
            return False


class Rectangle:
    # Initialize Rectangle object with two corner points
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        # Calculate the area of the rectangle
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


# Create a random rectangle with corner points
rectangle = Rectangle(
    Point(randint(0, 9), randint(0, 9)), Point(randint(10, 19), randint(10, 19))
)

print(
    "Rectangle Coordinates: ",
    rectangle.point1.x,
    ",",
    rectangle.point1.y,
    "and",
    rectangle.point2.x,
    ",",
    rectangle.point2.y,
)

# Get the user's guessed point and area for the rectangle
user_point = Point(float(input("Guess X: ")), float(input("Guess Y: ")))
user_area = float(input("Guess area of the rectangle: "))

print("Your point was inside rectangle: ", user_point.inside_rectangle(rectangle))

print("Your area was of by: ", rectangle.area() - user_area)
