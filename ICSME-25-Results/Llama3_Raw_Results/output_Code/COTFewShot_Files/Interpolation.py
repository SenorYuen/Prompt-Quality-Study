class Interpolation:
    def __init__(self):
        pass

    @staticmethod
    def interpolate_1d(x, y, x_interp):
        y_interp = []
        for x_val in x_interp:
            if x_val <= x[0]:
                y_interp.append(y[0])
            elif x_val >= x[-1]:
                y_interp.append(y[-1])
            else:
                for i in range(len(x) - 1):
                    if x_val >= x[i] and x_val <= x[i + 1]:
                        slope = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
                        y_val = y[i] + slope * (x_val - x[i])
                        y_interp.append(y_val)
                        break
        return y_interp

    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        z_interp = []
        for i in range(len(x_interp)):
            x_val = x_interp[i]
            y_val = y_interp[i]
            if x_val <= x[0] and y_val <= y[0]:
                z_interp.append(z[0][0])
            elif x_val >= x[-1] and y_val >= y[-1]:
                z_interp.append(z[-1][-1])
            elif x_val <= x[0] and y_val >= y[-1]:
                z_interp.append(z[0][-1])
            elif x_val >= x[-1] and y_val <= y[0]:
                z_interp.append(z[-1][0])
            else:
                for j in range(len(x) - 1):
                    if x_val >= x[j] and x_val <= x[j + 1]:
                        for k in range(len(y) - 1):
                            if y_val >= y[k] and y_val <= y[k + 1]:
                                q11 = z[j][k]
                                q12 = z[j][k + 1]
                                q21 = z[j + 1][k]
                                q22 = z[j + 1][k + 1]
                                r1 = q11 + (q12 - q11) * (y_val - y[k]) / (y[k + 1] - y[k])
                                r2 = q21 + (q22 - q21) * (y_val - y[k]) / (y[k + 1] - y[k])
                                z_val = r1 + (r2 - r1) * (x_val - x[j]) / (x[j + 1] - x[j])
                                z_interp.append(z_val)
                                break
                        break
        return z_interp