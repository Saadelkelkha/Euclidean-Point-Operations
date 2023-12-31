# Import the Point class from the ex1 module
from p import Point

# Create a Point object with coordinates of constructor
point0 = Point()
# Create a Point object with coordinates (76, 47)
point1 = Point(76, 47)

# Print the Euclidean distance between the point and itself
print("The distance is:", point0.Distance(point1))

# Print the Euclidean norm of the point
print("The norm is:", point1.Norm())

