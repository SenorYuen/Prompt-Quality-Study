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

    # Calculate the area of a circle using the formula: πr^2
    def calculate_circle_area(self):
        """
        calculate the area of circle based on self.radius
        :return: area of circle, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_circle_area()
        12.566370614359172
        """
        return math.pi * (self.radius ** 2)

    # Calculate the area of a sphere using the formula: 4πr^2
    def calculate_sphere_area(self):
        """
        calculate the area of sphere based on self.radius
        :return: area of sphere, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_sphere_area()
        50.26548245743669
        """
        return 4 * math.pi * (self.radius ** 2)

    # Calculate the area of a cylinder using the formula: 2πr(h + r)
    def calculate_cylinder_area(self, height):
        """
        calculate the area of cylinder based on self.radius and height
        :param height: height of cylinder, float
        :return: area of cylinder, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_cylinder_area(3)
        62.83185307179586
        """
        return 2 * math.pi * self.radius * (height + self.radius)

    # Calculate the area of a sector using the formula: (θ/360)πr^2
    def calculate_sector_area(self, angle):
        """
        calculate the area of sector based on self.radius and angle
        :param angle: angle of sector, float
        :return: area of sector, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_sector_area(math.pi)
        6.283185307179586
        """
        # Convert angle from radians to degrees
        angle_in_degrees = math.degrees(angle)
        return (angle_in_degrees / 360) * math.pi * (self.radius ** 2)

    # Calculate the area of an annulus using the formula: π(R^2 - r^2)
    def calculate_annulus_area(self, inner_radius, outer_radius):
        """
        calculate the area of annulus based on inner_radius and out_radius
        :param inner_radius: inner radius of sector, float
        :param outer_radius: outer radius of sector, float
        :return: area of annulus, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_annulus_area(2, 3)
        15.707963267948966
        """
        return math.pi * ((outer_radius ** 2) - (inner_radius ** 2))