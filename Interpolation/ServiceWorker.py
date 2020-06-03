import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

if __name__ == "__main__":
    print("It's a computation file, please run \'main.py\'")


def getReadyAnswer(type_answer):
    if type_answer == 1:
        print("Incorrect input.\n")
    elif type_answer == 2:
        print("No solution.\n")
    elif type_answer == 3:
        print("There is no concrete solution or it doesn't exist.\n")
    elif type_answer == 4:
        print("Convergence condition is not satisfied on this segment.\n")
    elif type_answer == 5:
        print("Counts of iteration reached 2.5 million , solution not found.\n")
    elif type_answer == 6:
        print("The initial approximation is poorly selected, solution not found.\n")
    elif type_answer == 7:
        print("Counts of iteration reached 250 thousand , solution not found.\n")


def make_graph(calculator, equation):
    try:
        "\t1. y' = y + (1+x)y^2\n"
        "\t2. y' = e^2x + y\n"
        "\t3. y' = y/x - 3\n"
        "\t4. y' = x^2 - 2y"
        eq_name = {1: "y' = y + (1+x)y^2",
                   2: "y' = e^2x + y",
                   3: "y' = y/x - 3",
                   4: "y' = x^2 - 2y"}
        ax = plt.gca()
        plt.grid()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        minimum = min(calculator.x_values)
        maximum = max(calculator.x_values)
        for i in calculator.dots_x:
            if i < minimum:
                minimum = i
            elif i > maximum:
                maximum = i
        x = np.linspace(minimum, maximum, 100)
        first_equation = [calculator.interpolation(i) for i in x]
        plt.title("Graph of " + eq_name[equation])
        plt.plot(x, first_equation, color='r', linewidth=2)
        j = 0
        for i in calculator.x_values:
            plt.scatter(i, calculator.y_values[j], color='r', s=40)
            j += 1
        plt.show()
        del x
    except ValueError:
        return
    except ZeroDivisionError:
        return
