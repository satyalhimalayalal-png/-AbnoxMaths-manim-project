# This file was auto-created
import numpy as np

# Calculate arctangent of a single value
angle_rad_single = np.rad2deg(np.arctan(1))
print(f"Arctangent of 1: {angle_rad_single} degrees")

# Calculate arctangent of an array
values = np.array([-1, 0, 1])
angles_rad_array = np.arctan(values)
print(f"Arctangent of array values: {angles_rad_array} radians")