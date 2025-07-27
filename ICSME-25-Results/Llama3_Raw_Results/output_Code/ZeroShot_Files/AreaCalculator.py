# This is a class for calculating the area of different shapes, including circle, sphere, cylinder, sector and annulus.
import math

class AreaCalculator:
    # Initialize the radius for shapes.
    def __init__(self, radius):
        self.radius = radius  # store the radius as an instance variable

    # Calculate the area of circle based on self.radius
    def calculate_circle_area(self):
        # formula for area of circle: π * r^2
        return math.pi * (self.radius ** 2)

    # Calculate the area of sphere based on self.radius
    def calculate_sphere_area(self):
        # formula for area of sphere: 4 * π * r^2
        return 4 * math.pi * (self.radius ** 2)

    # Calculate the area of cylinder based on self.radius and height
    def calculate_cylinder_area(self, height):
        # formula for area of cylinder: 2 * π * r * (r + h)
        return 2 * math.pi * self.radius * (self.radius + height)

    # Calculate the area of sector based on self.radius and angle
    def calculate_sector_area(self, angle):
        # formula for area of sector: (angle/360) * π * r^2
        return (angle / 360) * math.pi * (self.radius ** 2)

    # Calculate the area of annulus based on inner_radius and outer_radius
    def calculate_annulus_area(self, inner_radius, outer_radius):
        # formula for area of annulus: π * (outer_radius^2 - inner_radius^2)
        return math.pi * ((outer_radius ** 2) - (inner_radius ** 2))