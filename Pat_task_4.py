import math #need to import the math module
#formula to find area of circle
the_list = [10,22]
find_area_of = [math.pi * i ** 2 for i in the_list]
print(find_area_of)

#formula to find perimeter of circle
the_list_num = [10]
find_perimeter_of = [2 * math.pi * j for j in the_list_num]
print(find_perimeter_of)
'''------------------------------------------------------------------------------------------------------------------'''

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.141  # pi as specified

    def area(self):
        # Area formula: pi * radius^2
        area_formula = self.pi * self.radius ** 2
        return area_formula

    def perimeter(self):
        # Area formula: pi * radius^2
        perimeter_formula = 2 * self.pi * self.radius
        return perimeter_formula

# List of radii values
radii_list = [10, 22]

# Create Circle objects for each radius and print the area
for i in radii_list:
    circle = Circle(i)
    print(f"Radius: {i}, Area: {circle.area()}")
    print(f"circumference: {i}, Area: {circle.perimeter()}")

'''------------------------------------------------------------------------------------------------------------------'''

#create a python class called circle
class Circle_formula: #declare a class using class key word
    #__init__ method is the constructor of the class.

    def __init__(self,a): #a is a parameter that will be used to store a list
        self.a = a

    def find_area_of_circle(self):
        #calculate the area using formula
        find_areacircle = [math.pi * i ** 2 for i in self.a] #iterates through each radius i in the list self.a.
        return find_areacircle #return statement returns the list of calculated areas.

    def find_perimeter_of_circle(self):
        # calculate the perimeter using formula
         find_perimeterircle = [2 * math.pi * j for j in self.a] #iterates through each radius j in the list self.a.
         return find_perimeterircle

the_list_of_number = [10,501,22,37,100,999,87,351]
object_circle = Circle_formula(the_list_of_number) #creates an instance (object) of the Circle class and passes the_list_of_number as the argument to the __init__ method.
print(f" Perimeter of circle: {object_circle.find_perimeter_of_circle()}")
print(f" Area of circle: {object_circle.find_area_of_circle()}")

'''------------------------------------------------------------------------------------------------------------------'''

class Find_area_and_perimeter:
    def __init__(self,value):
        self.a = value

    def area_of_circle_formula(self):
        formula_area_of_circle = [math.pi * self.a ** 2]
        return formula_area_of_circle

    def perimeter_of_circle_formula(self):
        formula_perimeter_of_circle = [2 * math.pi * self.a]
        return formula_perimeter_of_circle

the_list_is = [10,501,22,37,100,999,87,351]
for i in the_list_is:
    obj_circle = Find_area_and_perimeter(i)
    print(f"{i}: Area of the circle: {obj_circle.area_of_circle_formula()}")
    print(f"{i}: Area of the perimeter: {obj_circle.perimeter_of_circle_formula()}")





