class Interpolation:
    """
    This is a class that implements the Linear interpolation operation of one-dimensional and two-dimensional data
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
        """
        # Initialize an empty list to store the interpolated y-coordinates
        y_interp = []
        
        # Iterate over each interpolation point
        for x_val in x_interp:
            # Find the index of the x-coordinate that is just below the interpolation point
            idx = next((i for i, val in enumerate(x) if val > x_val), len(x) - 1) - 1
            
            # Check if the interpolation point is outside the range of x-coordinates
            if idx < 0:
                # If it's below the lowest x-coordinate, use the lowest y-coordinate
                y_interp.append(y[0])
            elif idx >= len(x) - 1:
                # If it's above the highest x-coordinate, use the highest y-coordinate
                y_interp.append(y[-1])
            else:
                # Calculate the interpolated y-coordinate using linear interpolation
                y_val = y[idx] + (y[idx + 1] - y[idx]) * (x_val - x[idx]) / (x[idx + 1] - x[idx])
                y_interp.append(y_val)
        
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
        """
        # Initialize an empty list to store the interpolated z-coordinates
        z_interp = []
        
        # Iterate over each interpolation point
        for x_val, y_val in zip(x_interp, y_interp):
            # Find the indices of the x and y coordinates that are just below the interpolation point
            idx_x = next((i for i, val in enumerate(x) if val > x_val), len(x) - 1) - 1
            idx_y = next((i for i, val in enumerate(y) if val > y_val), len(y) - 1) - 1
            
            # Check if the interpolation point is outside the range of x or y coordinates
            if idx_x < 0:
                # If it's below the lowest x-coordinate, use the lowest z-coordinate
                z_val = z[0][idx_y] + (z[0][idx_y + 1] - z[0][idx_y]) * (y_val - y[idx_y]) / (y[idx_y + 1] - y[idx_y])
            elif idx_x >= len(x) - 1:
                # If it's above the highest x-coordinate, use the highest z-coordinate
                z_val = z[-1][idx_y] + (z[-1][idx_y + 1] - z[-1][idx_y]) * (y_val - y[idx_y]) / (y[idx_y + 1] - y[idx_y])
            elif idx_y < 0:
                # If it's below the lowest y-coordinate, use the lowest z-coordinate
                z_val = z[idx_x][0] + (z[idx_x + 1][0] - z[idx_x][0]) * (x_val - x[idx_x]) / (x[idx_x + 1] - x[idx_x])
            elif idx_y >= len(y) - 1:
                # If it's above the highest y-coordinate, use the highest z-coordinate
                z_val = z[idx_x][-1] + (z[idx_x + 1][-1] - z[idx_x][-1]) * (x_val - x[idx_x]) / (x[idx_x + 1] - x[idx_x])
            else:
                # Calculate the interpolated z-coordinate using bilinear interpolation
                q11 = z[idx_x][idx_y]
                q12 = z[idx_x][idx_y + 1]
                q21 = z[idx_x + 1][idx_y]
                q22 = z[idx_x + 1][idx_y + 1]
                
                r1 = q11 + (q12 - q11) * (y_val - y[idx_y]) / (y[idx_y + 1] - y[idx_y])
                r2 = q21 + (q22 - q21) * (y_val - y[idx_y]) / (y[idx_y + 1] - y[idx_y])
                
                z_val = r1 + (r2 - r1) * (x_val - x[idx_x]) / (x[idx_x + 1] - x[idx_x])
            
            z_interp.append(z_val)
        
        return z_interp