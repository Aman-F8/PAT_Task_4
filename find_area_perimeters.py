import math  # Import math module to use math.pi for circle calculations

# Formula to find area of a circle using list comprehension
radii_list = [10, 22]  # List of circle radii
areas = [math.pi * radius ** 2 for radius in radii_list]  # Area = π * r² for each radius
print("Areas of circles:", areas)

# Formula to find perimeter (circumference) of a circle using list comprehension
radii_list_single = [10]  # List with one radius
perimeters = [2 * math.pi * radius for radius in radii_list_single]  # Perimeter = 2 * π * r
print("Perimeters of circles:", perimeters)