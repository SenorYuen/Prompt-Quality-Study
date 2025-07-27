import math

class AreaCalculator:
    """
    This is a class for calculating the area of different shapes, including circle, sphere, cylinder, sector and annulus.
    """

    def __init__(self, radius):
        """
        Initialize the radius for shapes.
        :param radius: float
        """
        self.radius = radius

    def calculate_circle_area(self):
        """
        Calculate the area of a circle based on self.radius.
        :return: area of circle, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_circle_area()
        12.566370614359172
        """
        # Area of a circle = π * radius^2
        return math.pi * self.radius ** 2

    def calculate_sphere_area(self):
        """
        Calculate the surface area of a sphere based on self.radius.
        :return: area of sphere, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_sphere_area()
        50.26548245743669
        """
        # Surface area of a sphere = 4 * π * radius^2
        return 4 * math.pi * self.radius ** 2

    def calculate_cylinder_area(self, height):
        """
        Calculate the surface area of a cylinder based on self.radius and height.
        :param height: height of cylinder, float
        :return: area of cylinder, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_cylinder_area(3)
        62.83185307179586
        """
        # Surface area of a cylinder = 2 * π * radius * (radius + height)
        return 2 * math.pi * self.radius * (self.radius + height)

    def calculate_sector_area(self, angle):
        """
        Calculate the area of a sector based on self.radius and angle.
        :param angle: angle of sector, float
        :return: area of sector, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_sector_area(math.pi)
        6.283185307179586
        """
        # Area of a sector = 0.5 * radius^2 * angle
        return 0.5 * self.radius ** 2 * angle

    def calculate_annulus_area(self, inner_radius, outer_radius):
        """
        Calculate the area of an annulus based on inner_radius and outer_radius.
        :param inner_radius: inner radius of annulus, float
        :param outer_radius: outer radius of annulus, float
        :return: area of annulus, float
        >>> areaCalculator.calculate_annulus_area(2, 3)
        15.707963267948966
        """
        # Area of an annulus = π * (outer_radius^2 - inner_radius^2)
        return math.pi * (outer_radius ** 2 - inner_radius ** 2)