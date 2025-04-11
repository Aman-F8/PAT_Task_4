# Create a class to represent a circle with methods to calculate area and perimeter
class Circle:
    def __init__(self, radius):
        self.radius = radius  # Store the radius value
        self.pi = 3.141  # Using a fixed value of pi

    def area(self):
        # Area formula: pi * radius^2
        area = self.pi * self.radius ** 2
        return area  # Return calculated area

    def perimeter(self):
        # Perimeter formula: 2 * pi * radius
        perimeter = 2 * self.pi * self.radius
        return perimeter  # Return calculated perimeter

# List of radii values
circle_radii = [10, 22]

# Create Circle objects and display area and perimeter
for radius in circle_radii:
    circle_obj = Circle(radius)  # Create object with current radius
    print(f"Radius: {radius}, Area: {circle_obj.area()}")  # Print area
    print(f"Radius: {radius}, Perimeter: {circle_obj.perimeter()}")  # Print perimeter