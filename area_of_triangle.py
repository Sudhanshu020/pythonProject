# program to calculate the area of Triangle

triangle_height = float(input('Enter the Height of Triangle : '))
triangle_base = float(input('Enter the Base of Triangle : '))

# format method to get Area of Triangle up to two decimal places
triangle_area = f"Area of Triangle with Height {triangle_height} and Base {triangle_base} is : {'{0:.2f}'.format(( triangle_height * triangle_base ) / 2)}"
print(triangle_area)