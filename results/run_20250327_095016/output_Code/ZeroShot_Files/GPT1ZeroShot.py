import math

class AreaCalculator:

    def __init__(self, radius):
        """
        Initialize the radius for shapes.
        """
        self.radius = radius

    def calculate_circle_area(self):
        """
        Calculate the area of a circle based on self.radius.
        :return: area of circle, float
        """
        return math.pi * self.radius ** 2

    def calculate_sphere_area(self):
        """
        Calculate the surface area of a sphere based on self.radius.
        :return: area of sphere, float
        """
        return 4 * math.pi * self.radius ** 2

    def calculate_cylinder_area(self, height):
        """
        Calculate the surface area of a cylinder based on self.radius and height.
        :return: area of cylinder, float
        """
        base_area = math.pi * self.radius ** 2
        lateral_surface_area = 2 * math.pi * self.radius * height
        return 2 * base_area + lateral_surface_area

    def calculate_sector_area(self, angle):
        """
        Calculate the area of a sector based on self.radius and angle (in radians).
        :return: area of sector, float
        """
        return 0.5 * self.radius ** 2 * angle

    def calculate_annulus_area(self, inner_radius, outer_radius):
        """
        Calculate the area of an annulus based on inner_radius and outer_radius.
        :return: area of annulus, float
        """
        outer_area = math.pi * outer_radius ** 2
        inner_area = math.pi * inner_radius ** 2
        return outer_area - inner_area