'''
# This is a class for calculating the area of different shapes, including circle, sphere, cylinder, sector and annulus.

import math
class AreaCalculator:

    def __init__(self, radius):
        """
        Initialize the radius for shapes.
        """

    def calculate_circle_area(self):
        """
        calculate the area of circle based on self.radius
        :return: area of circle, float
        """

    def calculate_sphere_area(self):
        """
        calculate the area of sphere based on self.radius
        :return: area of sphere, float
        """

    def calculate_cylinder_area(self, height):
        """
        calculate the area of cylinder based on self.radius and height
        :return: area of cylinder, float
        """

    def calculate_sector_area(self, angle):
        """
        calculate the area of sector based on self.radius and angle
        return: area of sector, float
        """

    def calculate_annulus_area(self, inner_radius, outer_radius):
        """
        calculate the area of annulus based on inner_radius and out_radius
        return: area of sector, float
        """
'''

import math


class AreaCalculator:

    def __init__(self, radius):
        self.radius = radius

    def calculate_circle_area(self):
        return math.pi * self.radius ** 2

    def calculate_sphere_area(self):
        return 4 * math.pi * self.radius ** 2

    def calculate_cylinder_area(self, height):
        return 2 * math.pi * self.radius * (self.radius + height)

    def calculate_sector_area(self, angle):
        return self.radius ** 2 * angle / 2

    def calculate_annulus_area(self, inner_radius, outer_radius):
        return math.pi * (outer_radius ** 2 - inner_radius ** 2)

