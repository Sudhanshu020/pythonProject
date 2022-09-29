# program to calculate the area of shpere

PI = 3.14
sphere_radius = float(input('Enter the Radius of Sphere : '))

# format method to get Area of Sphere up to two decimal places
sphere_area = f"Area of sphere with radius {sphere_radius} is : {'{0:.2f}'.format(4 * PI * sphere_radius)}"
print(sphere_area)