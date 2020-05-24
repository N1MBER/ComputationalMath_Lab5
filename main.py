from Solver import ConsoleWorker
from Interpolation import ServiceWorker

print("Welcome to differential equations solver!")

while 1:
    print("What you want?\n"
          "\t1. Solve.\n"
          "\t2. Exit\n")
    try:
        answer = int(input("Please choose a variant: ").strip())
        if answer == 1:
            consoleWorker = ConsoleWorker.ConsoleWorker()
            consoleWorker.start()
            del consoleWorker
        elif answer == 2:
            print("Exit...")
            break
    except TypeError:
        ServiceWorker.getReadyAnswer(1)
        continue
    except ValueError:
        ServiceWorker.getReadyAnswer(1)
        continue
    except KeyboardInterrupt:
        print("Exit...")
        break
