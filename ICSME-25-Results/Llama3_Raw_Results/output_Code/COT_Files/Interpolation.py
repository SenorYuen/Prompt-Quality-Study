class Interpolation:
    def __init__(self):
        pass

    @staticmethod
    def interpolate_1d(x, y, x_interp):
        y_interp = []
        for x_val in x_interp:
            for i in range(len(x) - 1):
                if x[i] <= x_val <= x[i + 1]:
                    slope = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
                    y_val = y[i] + slope * (x_val - x[i])
                    y_interp.append(y_val)
                    break
        return y_interp

    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        z_interp = []
        for x_val, y_val in zip(x_interp, y_interp):
            for i in range(len(x) - 1):
                for j in range(len(y) - 1):
                    if x[i] <= x_val <= x[i + 1] and y[j] <= y_val <= y[j + 1]:
                        q11 = z[i][j]
                        q12 = z[i][j + 1]
                        q21 = z[i + 1][j]
                        q22 = z[i + 1][j + 1]
                        r1 = q11 + (q12 - q11) * (y_val - y[j]) / (y[j + 1] - y[j])
                        r2 = q21 + (q22 - q21) * (y_val - y[j]) / (y[j + 1] - y[j])
                        z_val = r1 + (r2 - r1) * (x_val - x[i]) / (x[i + 1] - x[i])
                        z_interp.append(z_val)
                        break
                else:
                    continue
                break
        return z_interp