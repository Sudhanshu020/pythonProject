# program to calculate the area of Circle
import math

# constent for Pi
PI = 3.14
circle_radius = float(input('Enter the Radius of Circle : '))

# format method to get Area of Circle up to two decimal places
circle_area = f"Area of Circle with radius {circle_radius} is : {'{0:.2f}'.format(PI * math.pow(circle_radius , 2))}"
print(circle_area)