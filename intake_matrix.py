from enum import Enum
import sympy as sy

def intake_matrix():
    class Matrixgrid(Enum):
        two_xtwo = 1
        two_xthree = 2
        three_xthree = 3
        three_xfour = 4
        five_xfive = 5

    userIn = 0
    matrix_in = 0
    matrix_grid_in = Matrixgrid.two_xthree
    matrixOptions = ["1- 2x2",
                     "2- 2x3",
                     "3- 3x3",
                     "4- 3x4",
                     "5- 5x5"]

    def console_pauser():
        print("Press any key to continue...")
        input()

    while matrix_in > 4 or matrix_in < 1:
        print("----------Please Choose a setup for your system of linear equations----------\n\n")

        for i in matrixOptions:
            print(i)
        print('\n')
        matrix_in = int(input("Choose equation Dimensions:"))
        if matrix_in == 1:
            matrix_grid_in = Matrixgrid.two_xtwo
        elif matrix_in == 2:
            matrix_grid_in = Matrixgrid.two_xthree
        elif matrix_in == 3:
            matrix_grid_in = Matrixgrid.three_xthree
        elif matrix_in == 4:
            matrix_grid_in = Matrixgrid.three_xfour
        elif matrix_in == 5:
            matrix_grid_in = Matrixgrid.five_xfive
        else:
            print("\n*************************************\n************INVALID "
                  "INPUT************\n*************************************\n")
            console_pauser()

    x1 = x2 = x3 = y1 = y2 = y3 = z1 = z2 = z3 = rightside1 = rightside2 = rightside3 = rightside4 = rightside5 = 0
    a1 = a2 = a3 = a4 = a5 = b1 = b2 = b3 = b4 = b5 = c1 = c2 = c3 = c4 = c5 = d1 = d2 = d3 = d4 = d5 = 0
    matrix = sy.randMatrix(1)
    if matrix_grid_in == Matrixgrid.two_xtwo:
        x1 = int(input("Input x1:"))
        rightside1 = int(input("Input right side of the first equation:"))
        x2 = int(input("Input x2:"))
        rightside2 = int(input("Input right side of the second equation:"))
        matrix = sy.Matrix([[x1, rightside1], [x2, rightside2]])
    elif matrix_grid_in == Matrixgrid.two_xthree:
        x1 = int(input("Input x1:"))
        y1 = int(input("Input y1:"))
        rightside1 = int(input("Input right side of the first equation:"))
        x2 = int(input("Input x2:"))
        y2 = int(input("Input y2:"))
        rightside2 = int(input("Input right side of the second equation:"))
        matrix = sy.Matrix([[x1, y1, rightside1], [x2, y2, rightside2]])
    elif matrix_grid_in == Matrixgrid.three_xthree:
        x1 = int(input("Input x1:"))
        y1 = int(input("Input y1:"))
        rightside1 = int(input("Input right side of the first equation:"))
        x2 = int(input("Input x2:"))
        y2 = int(input("Input y2:"))
        rightside2 = int(input("Input right side of the second equation:"))
        x3 = int(input("Input x3:"))
        y3 = int(input("Input y3:"))
        rightside3 = int(input("Input right side of the third equation:"))
        matrix = sy.Matrix([[x1, y1, rightside1], [x2, y2, rightside2], [x3, y3, rightside3]])
    elif matrix_grid_in == Matrixgrid.three_xfour:
        x1 = int(input("Input x1:"))
        y1 = int(input("Input y1:"))
        z1 = int(input("Input z1:"))
        rightside1 = int(input("Input right side of the first equation:"))
        x2 = int(input("Input x2:"))
        y2 = int(input("Input y2:"))
        z2 = int(input("Input z2:"))
        rightside2 = int(input("Input right side of the second equation:"))
        x3 = int(input("Input x3:"))
        y3 = int(input("Input y3:"))
        z3 = int(input("Input z3:"))
        rightside3 = int(input("Input right side of the third equation:"))
        matrix = sy.Matrix([[x1, y1, z1, rightside1], [x2, y2, z2, rightside2], [x3, y3, z3, rightside3]])
    elif matrix_grid_in == Matrixgrid.five_xfive:
        a1 = int(input("Input a1:"))
        b1 = int(input("Input b1:"))
        c1 = int(input("Input c1:"))
        d1 = int(input("Input d1:"))
        rightside1 = int(input("Input right side of the first equation:"))
        a2 = int(input("Input a2:"))
        b2 = int(input("Input b2:"))
        c2 = int(input("Input c2:"))
        d2 = int(input("Input d2:"))
        rightside2 = int(input("Input right side of the second equation:"))
        a3 = int(input("Input a3:"))
        b3 = int(input("Input b3:"))
        c3 = int(input("Input c3:"))
        d3 = int(input("Input d3:"))
        rightside3 = int(input("Input right side of the third equation:"))
        a4 = int(input("Input a4:"))
        b4 = int(input("Input b4:"))
        c4 = int(input("Input c4:"))
        d4 = int(input("Input d4:"))
        rightside4 = int(input("Input right side of the fourth equation:"))
        a5 = int(input("Input a5:"))
        b5 = int(input("Input b5:"))
        c5 = int(input("Input c5:"))
        d5 = int(input("Input d5:"))
        rightside5 = int(input("Input right side of the fifth equation:"))
        matrix = sy.Matrix([[a1, b1, c1, d1, rightside1], [a2, b2, c2, d2, rightside2],
                            [a3, b3, c3, d3, rightside3], [a4, b4, c4, d4, rightside4],
                            [a5, b5, c5, d5, rightside5]])

    return matrix
