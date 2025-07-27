import math


class AreaCalculator:
    def __init__(self, radius):
        # This method will act as the constructor.
        # This method will Initialize the radius for shapes.
        self.radius = radius

    def calculate_circle_area(self):
        # This method will calculate the area of circle based on self.radius
        # This method will return area of circle as float
        return math.pi * (self.radius ** 2)

    def calculate_sphere_area(self):
        # This method will calculate the area of sphere based on self.radius
        # This method will return area of sphere as float
        return 4 * math.pi * (self.radius ** 2)

    def calculate_cylinder_area(self, height):
        # This method will calculate the area of cylinder based on self.radius and height
        # This method will accept "height" as a float which is the height of cylinder
        # This method will return area of cylinder as float
        return 2 * math.pi * self.radius * (self.radius + height)

    def calculate_sector_area(self, angle):
        # This method will calculate the area of sector based on self.radius and angle
        # This method will get "angle" as a float which is the angle of sector
        # This method will return area of sector as float
        return (angle / (2 * math.pi)) * math.pi * (self.radius ** 2)

    def calculate_annulus_area(self, inner_radius, outer_radius):
        # This method will calculate the area of annulus based on inner_radius and out_radius
        # This method will get "inner_radius" as a float which is the inner radius of sector, 
        # and "outer_radius" as a float which is the outer radius of sector 
        # This method will return area of annulus as float
        return math.pi * ((outer_radius ** 2) - (inner_radius ** 2))