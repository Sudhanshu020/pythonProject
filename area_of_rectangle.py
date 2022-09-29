# program to calculate the area of Rectangle

rectangle_length = float(input('Enter the Length of Triangle : '))
rectangle_width = float(input('Enter the Width of Triangle : '))

# format method to get Area of Rectangle up to two decimal places
rectangle_area = f"Area of Rectangle with Length {rectangle_length} and Width {rectangle_width} is : {'{0:.2f}'.format( rectangle_length * rectangle_width )}"
print(rectangle_area)
