class Interpolation:
    def __init__(self):
        pass

    @staticmethod
    def interpolate_1d(x, y, x_interp):
        y_interp = []
        for xi in x_interp:
            for i in range(len(x) - 1):
                if x[i] <= xi <= x[i + 1]:
                    yi = y[i] + (y[i + 1] - y[i]) * (xi - x[i]) / (x[i + 1] - x[i])
                    y_interp.append(yi)
                    break
        return y_interp

    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        z_interp = []
        for xi, yi in zip(x_interp, y_interp):
            for i in range(len(x) - 1):
                for j in range(len(y) - 1):
                    if x[i] <= xi <= x[i + 1] and y[j] <= yi <= y[j + 1]:
                        z00 = z[i][j]
                        z01 = z[i][j + 1]
                        z10 = z[i + 1][j]
                        z11 = z[i + 1][j + 1]

                        fxy1 = z00 + (z10 - z00) * (xi - x[i]) / (x[i + 1] - x[i])
                        fxy2 = z01 + (z11 - z01) * (xi - x[i]) / (x[i + 1] - x[i])
                        zi = fxy1 + (fxy2 - fxy1) * (yi - y[j]) / (y[j + 1] - y[j])
                        z_interp.append(zi)
                        break
        return z_interp