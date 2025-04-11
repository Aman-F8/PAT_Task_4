# Class to calculate area and perimeter for multiple radii
import math  # Import math module to use math.pi for circle calculations

class CircleBatchCalculator:
    def __init__(self, radii_list):
        self.radii_list = radii_list  # Store the list of radii

    def find_areas(self):
        # Calculate area for each radius in the list
        return [math.pi * radius ** 2 for radius in self.radii_list]

    def find_perimeters(self):
        # Calculate perimeter for each radius in the list
        return [2 * math.pi * radius for radius in self.radii_list]

# List of radii to calculate area and perimeter
radii_values = [10, 501, 22, 37, 100, 999, 87, 351]

# Create object and call methods
circle_batch = CircleBatchCalculator(radii_values)
print(f"Perimeters of circles: {circle_batch.find_perimeters()}")
print(f"Areas of circles: {circle_batch.find_areas()}")