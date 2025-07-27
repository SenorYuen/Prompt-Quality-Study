class Interpolation:
    def __init__(self):
        pass

    @staticmethod
    def interpolate_1d(x, y, x_interp):
        """
        Linear interpolation of one-dimensional data
        :param x: List of x-coordinates of the data points
        :param y: List of y-coordinates of the data points
        :param x_interp: List of x-coordinates where interpolation is required
        :return: List of y-coordinates at the interpolation points
        """
        y_interp = []
        for xi in x_interp:
            # Find the interval [x_i, x_i+1] where x_i <= xi < x_i+1
            for i in range(len(x) - 1):
                if x[i] <= xi <= x[i + 1]:
                    # Linear interpolation formula
                    yi = y[i] + (y[i + 1] - y[i]) * (xi - x[i]) / (x[i + 1] - x[i])
                    y_interp.append(yi)
                    break
        return y_interp

    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        """
        Linear interpolation of two-dimensional data
        :param x: List of x-coordinates of the data points
        :param y: List of y-coordinates of the data points
        :param z: 2D list (matrix) of z-values corresponding to each (x, y) pair
        :param x_interp: List of x-coordinates where interpolation is required
        :param y_interp: List of y-coordinates where interpolation is required
        :return: List of z-coordinates at the interpolation points
        """
        z_interp = []
        for xi, yi in zip(x_interp, y_interp):
            # Find the bounding box for (xi, yi)
            for i in range(len(x) - 1):
                if x[i] <= xi <= x[i + 1]:
                    for j in range(len(y) - 1):
                        if y[j] <= yi <= y[j + 1]:
                            # Bilinear interpolation formula
                            f00 = z[i][j]
                            f10 = z[i + 1][j]
                            f01 = z[i][j + 1]
                            f11 = z[i + 1][j + 1]
                            
                            # Calculate weights
                            t = (xi - x[i]) / (x[i + 1] - x[i])
                            u = (yi - y[j]) / (y[j + 1] - y[j])
                            
                            # Interpolated value
                            z_val = (1 - t) * (1 - u) * f00 + t * (1 - u) * f10 + (1 - t) * u * f01 + t * u * f11
                            z_interp.append(z_val)
                            break
        return z_interp