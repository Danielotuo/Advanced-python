class Point:
    def __init__(self, x, y):
        # Initialize Point object with x and y coordinates
        self.x = x
        self.y = y
    
    def inside_rectangle(self, lowleft, upright):
        # Check if the Point is within the specified rectangle
        if lowleft[0] < self.x < upright[0] \
        and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False
    
# Create a Point object with coordinates (4, 5)
point1 = Point(4, 5)

# Check if point1 is inside the rectangle defined by (2, 3) and (6, 8)
is_inside = point1.inside_rectangle((2, 3), (6, 8))
print(is_inside)  # Print the result (True or False) to the console




