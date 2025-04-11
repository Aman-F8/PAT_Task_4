# Class to calculate area and perimeter of a single circle at a time
import math  # Import math module to use math.pi for circle calculations
class CircleCalculator:
    def __init__(self, radius):
        self.radius = radius  # Store single radius

    def calculate_area(self):
        # Use math.pi for accurate value of pi
        return [math.pi * self.radius ** 2]

    def calculate_perimeter(self):
        # Formula: 2 * pi * r
        return [2 * math.pi * self.radius]

# List of radii to calculate one at a time
individual_radii = [10, 501, 22, 37, 100, 999, 87, 351]

# Loop through list and create object for each radius
for radius in individual_radii:
    circle_instance = CircleCalculator(radius)
    print(f"Radius: {radius}, Area: {circle_instance.calculate_area()}")
    print(f"Radius: {radius}, Perimeter: {circle_instance.calculate_perimeter()}")