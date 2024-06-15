import scipy as sp
import sympy as sy
import numpy as np
from enum import Enum
import MatrixFunctionality

class Matrixgrid(Enum):
    two_xthree = 1
    three_xthree = 2
    three_xfour = 3
    five_xfive = 4


userIn = 0
matrixIn = 0
matrix_grid_in = Matrixgrid.two_xthree
menuOptions = ["1 - Solve a System of Linear equations", "2 - Perform Operations on this matrix", "Else - Exit"]
matrixOptions = ["1- 2 equations 2 vars x 3 numbies per equation",
                 "2- 3 equations 2 vars x 3 numbies per equation",
                 "3- 3 equations 3 vars x 4 numbies per equation",
                 "4- 5 equations 4 vars x 5 numbies per equation"]

def console_pauser():
    print("Press any key to continue...")
    input()


while matrixIn > 4 or matrixIn < 1:
    print("----------Please Choose a setup for your system of linear equations----------\n\n")

    for i in matrixOptions:
        print(i)
    print('\n')
    matrixIn = int(input("Choose equation Dimensions:"))
    if matrixIn == 1:
        matrix_grid_in = Matrixgrid.two_xthree
    elif matrixIn == 2:
        matrix_grid_in = Matrixgrid.three_xthree
    elif matrixIn == 3:
        matrix_grid_in = Matrixgrid.three_xfour
    elif matrixIn == 4:
        matrix_grid_in = Matrixgrid.five_xfive
    else:
        print("\n*************************************\n************INVALID "
              "INPUT************\n*************************************\n")
        console_pauser()

x1 = x2 = x3 = y1 = y2 = y3 = z1 = z2 = z3 = rightside1 = rightside2 = rightside3 = rightside4 = rightside5 = 0
a1 = a2 = a3 = a4 = a5 = b1 = b2 = b3 = b4 = b5 = c1 = c2 = c3 = c4 = c5 = d1 = d2 = d3 = d4 = d5 = 0
matrix = sy.randMatrix(1)
while len(menuOptions) > userIn > -1:
    if matrix_grid_in == Matrixgrid.two_xthree: # input matrix of the equations numbers
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
    for i in menuOptions:
        print(i)
    print('\n')
    userIn = int(input("Enter a Menu Option:"))
    if userIn == 1:
        a, b, c, d, x, y, z = sy.symbols("a,b,c,d,x,y,z")
        if matrix_grid_in == Matrixgrid.two_xthree:
            ans = sy.solve([x1*x + y1*y + rightside1, x2*x + y2*y + rightside2])
            sy.pprint(ans)
            console_pauser()
        elif matrix_grid_in == Matrixgrid.three_xthree:
            ans = sy.solve([x1 * x + y1 * y + rightside1, x2 * x + y2 * y + rightside2, x3 * x + y3 * y + rightside3])
            sy.pprint(ans)
            console_pauser()
        elif matrix_grid_in == Matrixgrid.three_xfour:
            ans = sy.solve([x1 * x + y1 * y + z1 * z + rightside1, x2 * x + y2 * y + z2 * z +  rightside2, x3 * x + y3 * y + z3 * z +  rightside3])
            sy.pprint(ans)
            console_pauser()
        elif matrix_grid_in == Matrixgrid.five_xfive:
            ans = sy.solve([a1*a + b1*b + c1*c + d1*d + rightside1, a2*a + b2*b + c2*c + d2*d + rightside2, a3*a + b3*b + c3*c + d3*d + rightside3, a4*a + b4*b + c4*c + d4*d + rightside4, a5*a + b5*b + c5*c + d5*d + rightside5])
            sy.pprint(ans)
            console_pauser()
    elif userIn == 2:
        MatrixFunctionality.matrixFunctionality(matrix)
