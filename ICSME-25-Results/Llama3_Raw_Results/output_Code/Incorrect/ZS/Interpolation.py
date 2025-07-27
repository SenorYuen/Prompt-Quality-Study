# This is a class that implements the Linear interpolation operation of one-dimensional and two-dimensional data

class Interpolation:
    def __init__(self):
        pass

    @staticmethod
    def interpolate_1d(x, y, x_interp):
        """
        Linear interpolation of one-dimensional data
        :return: The y-coordinate of the interpolation point, list.
        """
        # Initialize an empty list to store the interpolated y-coordinates
        y_interp = []
        
        # Iterate over each x-coordinate to be interpolated
        for x_val in x_interp:
            # Find the indices of the two x-coordinates in the original data that x_val lies between
            idx = [i for i, val in enumerate(x) if val <= x_val]
            # If x_val is less than the smallest x-coordinate, use the first two points for interpolation
            if not idx:
                idx = [0]
            # If x_val is greater than the largest x-coordinate, use the last two points for interpolation
            elif idx[-1] == len(x) - 1:
                idx = [len(x) - 2]
            else:
                idx = [idx[-1]]
            
            # Calculate the slope of the line segment between the two points
            slope = (y[idx[0] + 1] - y[idx[0]]) / (x[idx[0] + 1] - x[idx[0]])
            
            # Calculate the interpolated y-coordinate using the point-slope form of a line
            y_val = y[idx[0]] + slope * (x_val - x[idx[0]])
            
            # Append the interpolated y-coordinate to the list
            y_interp.append(y_val)
        
        # Return the list of interpolated y-coordinates
        return y_interp

    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        """
        Linear interpolation of two-dimensional data
        :return: The z-coordinate of the interpolation point, list.
        """
        # Initialize an empty list to store the interpolated z-coordinates
        z_interp = []
        
        # Iterate over each point to be interpolated
        for x_val, y_val in zip(x_interp, y_interp):
            # Find the indices of the four points in the original data that the point (x_val, y_val) lies within
            idx_x = [i for i, val in enumerate(x) if val <= x_val]
            idx_y = [i for i, val in enumerate(y) if val <= y_val]
            
            # If the point is outside the bounds of the data, use the nearest point for interpolation
            if not idx_x:
                idx_x = [0]
            elif idx_x[-1] == len(x) - 1:
                idx_x = [len(x) - 2]
            else:
                idx_x = [idx_x[-1]]
            
            if not idx_y:
                idx_y = [0]
            elif idx_y[-1] == len(y) - 1:
                idx_y = [len(y) - 2]
            else:
                idx_y = [idx_y[-1]]
            
            # Get the z-coordinates of the four points
            z11 = z[idx_x[0], idx_y[0]]
            z12 = z[idx_x[0], idx_y[0] + 1]
            z21 = z[idx_x[0] + 1, idx_y[0]]
            z22 = z[idx_x[0] + 1, idx_y[0] + 1]
            
            # Calculate the interpolated z-coordinate using bilinear interpolation
            z_val = (z11 * (x[idx_x[0] + 1] - x_val) * (y[idx_y[0] + 1] - y_val) +
                     z21 * (x_val - x[idx_x[0]]) * (y[idx_y[0] + 1] - y_val) +
                     z12 * (x[idx_x[0] + 1] - x_val) * (y_val - y[idx_y[0]]) +
                     z22 * (x_val - x[idx_x[0]]) * (y_val - y[idx_y[0]])) / ((x[idx_x[0] + 1] - x[idx_x[0]]) * (y[idx_y[0] + 1] - y[idx_y[0]]))
            
            # Append the interpolated z-coordinate to the list
            z_interp.append(z_val)
        
        # Return the list of interpolated z-coordinates
        return z_interp