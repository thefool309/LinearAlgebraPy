import sympy as sy

def matrixFunctionality(matrix : sy.Matrix):
    user_in = 0
    menu_options = ["1 - transpose matrix", "2 - reduced row echelon form", "3 - row echelon form",
                    "4 - Solve Via Linear Equation", "5- nullspace of matrix",
                    "6 - Determinate of matrix", "else - exit"]
    while user_in < len(menu_options):
        sy.pprint(matrix)

        for i in menu_options:
            print(i)
        print('\n')
        user_in = int(input("Input a Selection:"))

        if user_in == 1:
            result = matrix.transpose()
            print(result)
        elif user_in == 2:
            result = matrix.rref()
            sy.pprint(result)
        elif user_in == 3:
            result = matrix.echelon_form()
            sy.pprint(result)
        elif user_in == 4:
            result = sy.linsolve(matrix)
            sy.pprint(result)
        elif user_in == 5:
            result = matrix.nullspace()
            sy.pprint(result)
        elif user_in == 6:
            result = matrix.det()
            sy.pprint(result)



