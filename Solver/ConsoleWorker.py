from Solver import DiffurSolver
from prettytable import PrettyTable
from Interpolation import Interpolation
from Interpolation import ServiceWorker

if __name__ == "__main__":
    print("It's a computation file, please run \'main.py\'")


class ConsoleWorker:
    x0 = 0
    y0 = 0
    type_equation = 0
    step = 0
    end_segment = 0

    def __int__(self):
        self.x0 = 0
        self.y0 = 0
        self.type_equation = 0
        self.step = 0
        self.end_segment = 0

    def start(self):
        self.chooseType()
        self.set_start_value()
        self.set_end_segment()
        self.chooseStep()
        solver = DiffurSolver.DiffurSolver(self.type_equation, self.x0, self.y0, self.end_segment, self.step)
        solver.start()
        print_table(solver.table_value)
        make_interpolation(solver)
        del solver

    def chooseType(self):
        print("Please choose a equation:\n"
              "\t1. y' = y + (1+x)y^2\n"
              "\t2. y' = e^2x + y\n"
              "\t3. y' = y/x - 3\n"
              "\t4. y' = y(x+1)^3")
        while 1:
            try:
                answer = int(input("Type: ").strip())
                if answer < 1 or answer > 4:
                    ServiceWorker.getReadyAnswer(1)
                    continue
                else:
                    self.type_equation = answer
                    break
            except ValueError:
                ServiceWorker.getReadyAnswer(1)
                continue
            except TypeError:
                ServiceWorker.getReadyAnswer(1)
                continue

    def set_start_value(self):
        print("Please input a x0 and y0\n")
        while 1:
            try:
                answer = list(input("x0 and y0: ").strip().split(" "))
                if len(answer) == 2:
                    x0 = float(answer[0].strip())
                    y0 = float(answer[1].strip())
                    self.x0 = x0
                    self.y0 = y0
                    break
                else:
                    ServiceWorker.getReadyAnswer(1)
                    continue
            except ValueError:
                ServiceWorker.getReadyAnswer(1)
                continue
            except TypeError:
                ServiceWorker.getReadyAnswer(1)
                continue

    def set_end_segment(self):
        print("Please input a end of segment\n")
        while 1:
            try:
                answer = float(input("End of segment: ").strip())
                if answer > self.x0:
                    self.end_segment = answer
                    break
                else:
                    ServiceWorker.getReadyAnswer(1)
                    continue
            except ValueError:
                ServiceWorker.getReadyAnswer(1)
                continue
            except TypeError:
                ServiceWorker.getReadyAnswer(1)
                continue

    def chooseStep(self):
        print("Please choose a step\n")
        while 1:
            try:
                answer = float(input("Step: ").strip())
                if answer > 0:
                    self.step = answer
                    break
                else:
                    ServiceWorker.getReadyAnswer(1)
                    continue
            except ValueError:
                ServiceWorker.getReadyAnswer(1)
                continue
            except TypeError:
                ServiceWorker.getReadyAnswer(1)
                continue


def print_table(table_value):
    th = ["i", "x", "y", "y'"]
    table = PrettyTable(th)
    for element in table_value:
        table.add_row(element)
    print(table)


def make_interpolation(solver):
    interpolator = Interpolation.Interpolator(solver.x_values, solver.y_values, 1)
    interpolator.start()
    ServiceWorker.make_graph(interpolator)
