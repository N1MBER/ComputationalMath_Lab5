import numpy as np

if __name__ == "__main__":
    print("It's a computation file, please run \'main.py\'")


class DiffurSolver:
    type_equation = 0
    x = 0
    y = 0
    end = 0
    x_values = []
    y_values = []
    step = 0
    count_of_steps = 0
    table_value = []

    def __init__(self, types, x0, y0, endSegment, step):
        self.type_equation = types
        self.x = x0
        self.y = y0
        self.end = endSegment
        self.step = step
        self.x_values = []
        self.y_values = []
        self.table_value = []

    def start(self):
        self.count_of_steps = abs(self.end - self.x) / self.step
        i = 0
        print(self.count_of_steps)
        while i <= self.count_of_steps:
            try:
                self.x_values.append(self.x)
                self.y_values.append(self.y)
                self.table_value.append([i, self.x, self.y, self.get_value_of_derivative(self.x, self.y)])
                self.y = self.y + self.step * self.get_value_of_derivative(self.x, self.y)
                self.x = round(self.x + self.step, 8)
                i += 1
            except ZeroDivisionError:
                self.y = self.y + self.step * self.get_value_of_derivative(self.x + 1e-9, self.y)
                self.x = round(self.x + self.step, 8)
                i += 1
                continue

    # def set_value_on_table(self):


    def get_value_of_derivative(self, x, y):
        if self.type_equation == 1:
            return y + (1 + x) * np.power(y, 2)
        elif self.type_equation == 2:
            return np.power(np.e, 2 * x) - 2 * x * y
        elif self.type_equation == 3:
            return y / x - 3
        elif self.type_equation == 4:
            return y * np.power(x + 1, 3)

    def calculate(self, x, y, step):
        try:
            return y + step * self.get_value_of_derivative(x, y)
        except ZeroDivisionError:
            return y + step * self.get_value_of_derivative(x + 1e-9, y)
