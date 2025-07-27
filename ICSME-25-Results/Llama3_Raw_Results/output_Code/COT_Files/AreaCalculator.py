import math

class AreaCalculator:
    # Constructor method to initialize the radius
    def __init__(self, radius):
        # Initialize the radius for shapes
        self.radius = radius

    # Method to calculate the area of a circle
    def calculate_circle_area(self):
        # Calculate the area of circle based on self.radius
        # The formula for the area of a circle is πr^2
        area = math.pi * (self.radius ** 2)
        return area

    # Method to calculate the area of a sphere
    def calculate_sphere_area(self):
        # Calculate the area of sphere based on self.radius
        # The formula for the area of a sphere is 4πr^2
        area = 4 * math.pi * (self.radius ** 2)
        return area

    # Method to calculate the area of a cylinder
    def calculate_cylinder_area(self, height):
        # Calculate the area of cylinder based on self.radius and height
        # The formula for the area of a cylinder is 2πr^2 + 2πrh
        area = 2 * math.pi * (self.radius ** 2) + 2 * math.pi * self.radius * height
        return area

    # Method to calculate the area of a sector
    def calculate_sector_area(self, angle):
        # Calculate the area of sector based on self.radius and angle
        # The formula for the area of a sector is (angle/360) * πr^2
        # However, since the angle is given in radians, we use the formula (angle/2π) * πr^2 = (angle/2) * r^2
        area = (angle / 2) * (self.radius ** 2)
        return area

    # Method to calculate the area of an annulus
    def calculate_annulus_area(self, inner_radius, outer_radius):
        # Calculate the area of annulus based on inner_radius and outer_radius
        # The formula for the area of an annulus is π(outer_radius^2 - inner_radius^2)
        area = math.pi * ((outer_radius ** 2) - (inner_radius ** 2))
        return area