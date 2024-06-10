import sympy as sy

def matrixFunctionality():
    userIn = 0
    menuOptions = ["1 - transpose matrix", "2 - reduced row echelon form", "3 - row echelon form" "4 - Solve Via Linear Equation", "5- nullspace of matrix", "else - exit"]
    while userIn < len(menuOptions):
        print("Enter the following positions of the two matrices")
        a1 = int(input("a1:"))
        a2 = int(input("a2:"))
        # a3 = int(input("a3:"))
        b1 = int(input("b1:"))
        b2 = int(input("b2:"))
        # b3 = int(input("b3:"))
        c1 = int(input("c1:"))
        c2 = int(input("c2:"))
        # c3 = int(input("c3:"))
        # d1 = int(input("d1:"))
        # d2 = int(input("d2:")) [a3, b3, c3]
        # d3 = int(input("d3:"))

        matrix1 = sy.Matrix([[a1, b1, c1], [a2, b2, c2], ])
        sy.pprint(matrix1)

        for i in menuOptions:
            print(i)
        print('\n')
        userIn = int(input("Input a Selection:"))

        if userIn == 1:
            result = "NOT DONE YET"
            print(result)
        elif userIn == 2:
            result = matrix1.rref()
            sy.pprint(result)
        elif userIn == 3:
            result = matrix1.echelon_form()
            sy.pprint(result)
        elif userIn == 4:
            result = sy.linsolve(matrix1)
            sy.pprint(result)
        elif userIn == 5:
            result = matrix1.nullspace()
            sy.pprint(result)


matrixFunctionality()