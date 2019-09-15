import numpy as np
import sys


def havelhakimi(degrees):

    print("Performing Havel-Hakimi theorem")
    print(degrees)

    while -1 not in degrees:
        sub = np.int(degrees[-1])
        degrees = np.delete(degrees, -1)

        print(degrees)

        if len(degrees) >= sub:
            for i in range(sub):
                degrees[-1 - i] = degrees[-1 - i] - 1
        else:
            print("Not graphable:", sub, "exceeds length", len(degrees), "of array")
            break

        degrees.sort()
        print(degrees)
        if degrees[0] == 0 and degrees[-1] == 0:
            print("Obviously graphable")
            break

    else:
        print("Not graphable: a degree cannot be negative")


if __name__ == "__main__":
    int_list = np.array([])

    for i in sys.argv[1:]:
        try:
            i = int(i)
            int_list = np.append(int_list, i)
        except ValueError:
            print(i, "is not an integer")
            exit()

    int_list.sort()
    havelhakimi(int_list)