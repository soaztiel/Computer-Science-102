# Author: Anthony Cavallo
# Date: 09/04/2025
#
# Description:  Given the radius of a sphere, this program computes its 
#               diameter, surface area, and volume.

# A useful value:
PI = 3.14159265359

# Initialize the radius:
radius = 4.0

# Calculate the properties of the sphere:
diameter = radius*2
surface_area = 4*PI*radius
volume = (4/3)*PI*(radius**2)

# Print the results:
print("diameter =", diameter)
print("surface area =", surface_area)
print("volume =", volume)