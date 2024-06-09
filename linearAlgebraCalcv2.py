import VectorFunctionality
import MatrixFunctionality
userIn = 0
menuOptions = ["1 - Vector Operations", "2 - Matrix operations", "Else - Exit"]
while userIn < len(menuOptions):
    for i in menuOptions:
        print(i)
    print('\n')
    userIn = int(input("Choose an option:"))
    if userIn == 1:
        VectorFunctionality.vectorFunctionality()
    elif userIn == 2:
        result = "NOT DONE"
        print(result)
        MatrixFunctionality.matrixFunctionality()
    else:
        print("yeet")
        break
