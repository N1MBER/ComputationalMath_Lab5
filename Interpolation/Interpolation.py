if __name__ == "__main__":
    print("It's a computation file, please run \'main.py\'")


class Interpolator:
    y_diff = []
    x_values = []
    y_values = []
    y_graph_values = []
    dots_x = []
    dots_y = []
    equation_type = 0
    step = 0

    def __init__(self, x, y, types):
        self.x_values = x
        self.y_values = y
        self.step = self.x_values[1] - self.x_values[0]
        self.y_graph_values = []
        self.y_diff = []
        self.equation_type = types
        self.dots_x = []
        self.dots_y = []

    def separated_differences(self, differences):
        if len(differences) == 1:
            return self.y_values[self.x_values.index(differences[0])]
        else:
            first = differences[0:len(differences) - 1]
            second = differences[1:len(differences)]
            return (self.separated_differences(second) - self.separated_differences(first)) / (
                    differences[-1] - differences[0])

    def interpolation(self, x):
        interpolation = self.y_diff[0][-1]
        n = len(self.x_values) - 2
        t = (x - self.x_values[-1]) / self.step
        i = 1
        while n >= 0:
            k = 1
            factor = t
            while k <= i - 1:
                factor *= (t + k) / (k + 1)
                k += 1
            interpolation += factor * self.y_diff[i][n]
            n -= 1
            i += 1
        return interpolation

    def finite_differences(self):
        i = 1
        self.y_diff.append(self.y_values)
        while i < len(self.x_values):
            line = []
            j = 0
            while j < len(self.y_diff[i - 1]) - 1:
                result = self.y_diff[i - 1][j + 1] - self.y_diff[i - 1][j]
                line.append(result)
                j += 1
            self.y_diff.append(line)
            i += 1
