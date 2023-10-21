from random import randint
import turtle


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


# Define a class named Gui that inherits from Rectangle


class Gui(Rectangle):
    def draw(self, canvas):
        # Draw the rectangle on the canvas using turtle graphics
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


# Define a class named GuiPoint that inherits from Point
class GuiPoint(Point):
    def draw(self, canvas, size=5, color="blue"):
        # Draw a point on the canvas using turtle graphics
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


54


# Create a random rectangle with corner points
rectangle = Gui(
    Point(randint(0, 400), randint(0, 100)), Point(randint(20, 100), randint(10, 400))
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
user_point = GuiPoint(float(input("Guess X: ")), float(input("Guess Y: ")))
user_area = float(input("Guess area of the rectangle: "))

print("Your point was inside rectangle: ", user_point.inside_rectangle(rectangle))
print("Your area was of by: ", rectangle.area() - user_area)

# Initialize a turtle graphics canvas
myturtle = turtle.Turtle()

# Draw the rectangle and user's point on the canvas
rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)

# Finish and display the turtle graphics
turtle.done()
