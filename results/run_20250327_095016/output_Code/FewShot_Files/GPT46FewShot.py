class Interpolation:
    """
    This is a class that implements the Linear interpolation operation of one-dimensional and two-dimensional data.
    """

    def __init__(self):
        pass

    @staticmethod
    def interpolate_1d(x, y, x_interp):
        """
        Linear interpolation of one-dimensional data
        :param x: The x-coordinate of the data point, list.
        :param y: The y-coordinate of the data point, list.
        :param x_interp: The x-coordinate of the interpolation point, list.
        :return: The y-coordinate of the interpolation point, list.
        >>> interpolation = Interpolation()
        >>> interpolation.interpolate_1d([1, 2, 3], [1, 2, 3], [1.5, 2.5])
        [1.5, 2.5]
        """
        y_interp = []  # List to store interpolated y values
        for xi in x_interp:
            # Find the interval [x[i], x[i+1]] where xi is located
            for i in range(len(x) - 1):
                if x[i] <= xi <= x[i + 1]:
                    # Perform linear interpolation
                    yi = y[i] + (y[i + 1] - y[i]) * (xi - x[i]) / (x[i + 1] - x[i])
                    y_interp.append(yi)
                    break
        return y_interp

    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        """
        Linear interpolation of two-dimensional data
        :param x: The x-coordinate of the data point, list.
        :param y: The y-coordinate of the data point, list.
        :param z: The z-coordinate of the data point, 2D list.
        :param x_interp: The x-coordinate of the interpolation point, list.
        :param y_interp: The y-coordinate of the interpolation point, list.
        :return: The z-coordinate of the interpolation point, list.
        >>> interpolation = Interpolation()
        >>> interpolation.interpolate_2d([1, 2, 3], [1, 2, 3], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1.5, 2.5], [1.5, 2.5])
        [3.0, 7.0]
        """
        z_interp = []  # List to store interpolated z values
        for xi, yi in zip(x_interp, y_interp):
            # Find the rectangle [x[i], x[i+1]] x [y[j], y[j+1]] where (xi, yi) is located
            for i in range(len(x) - 1):
                for j in range(len(y) - 1):
                    if x[i] <= xi <= x[i + 1] and y[j] <= yi <= y[j + 1]:
                        # Perform bilinear interpolation
                        z1 = z[j][i]
                        z2 = z[j][i + 1]
                        z3 = z[j + 1][i]
                        z4 = z[j + 1][i + 1]

                        # Interpolation weights
                        t = (xi - x[i]) / (x[i + 1] - x[i])
                        u = (yi - y[j]) / (y[j + 1] - y[j])

                        # Calculate interpolated z value
                        zi = (1 - t) * (1 - u) * z1 + t * (1 - u) * z2 + (1 - t) * u * z3 + t * u * z4
                        z_interp.append(zi)
                        break
        return z_interp