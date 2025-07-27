class AreaCalculator:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circle_area(self):
        return 3.141592653589793 * self.radius * self.radius

    def calculate_sphere_area(self):
        return 4 * 3.141592653589793 * self.radius * self.radius

    def calculate_cylinder_area(self, height):
        return 2 * 3.141592653589793 * self.radius * (self.radius + height)

    def calculate_sector_area(self, angle):
        return 0.5 * self.radius * self.radius * angle

    def calculate_annulus_area(self, inner_radius, outer_radius):
        return 3.141592653589793 * (outer_radius * outer_radius - inner_radius * inner_radius)