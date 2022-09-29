# program to convert distance from Kilometer to miles

distance_kilometer = float(input('Enter the distance in Kilometer : '))
# We know that 1 km = 0.62137119 miles.

# format method to get the distance in miles up to two decimal places
distance_miles = f"{distance_kilometer} kilometer in miles is equal to : {'{0:.2f}'.format(distance_kilometer * 0.62137119)} miles"
print(distance_miles)