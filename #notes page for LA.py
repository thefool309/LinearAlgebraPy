#notes page for LA
import sympy as sy
from sympy.physics.vector import ReferenceFrame
from sympy import init_printing

#gather two LA vectors
first = int(input("please enter first int:"))
second = int(input("please enter second int:"))
third = int(input("please enter third int:"))
vList1 = [first, second, third] #store into lists just in case

fourth = int(input("Please enter the first int of the second vector:"))
fifth = int(input("Please enter the second int of the second vector:"))
sixth = int(input("Please enter the third int of the second vector:"))
vList2 = [fourth, fifth, sixth] #store into lists just in case
e = ReferenceFrame('e')
vVector1 = first*e.x + second*e.y + third*e.z
vVector2 = fourth*e.x + fifth*e.x + sixth*e.z

distanceVerticeResults = [fourth - first, fifth - second, sixth - third] #vector AB
c = sy.Array([distanceVerticeResults[0], distanceVerticeResults[1], distanceVerticeResults[2]])
v = distanceVerticeResults[0]*e.x + distanceVerticeResults[1]*e.y + distanceVerticeResults[2]*e.z
print("Formula Form:")
sy.pprint(v)
print("Brackets form:", c)
#magnitude with sympy
m = v.magnitude()
print("from sympy magnitude of v=", v, "is", m)
#normalize with sympy
print ("normalized with sympy:")
y = v.normalize()
sy.pprint(y)
userIn = 0
menuoptions = ["1 - Add Vectors", " 2 - Subtract vectors", "3 - Dot multiply vectors", "Else - Exit"]
while userIn != len(menuoptions):
    for i in menuoptions:
        print(i, "\n")
    userIn = int(input("Select a menu option:"))
    if userIn < 3:
        multipleForFirstVector = int(input("multiple for first vector (1 for none):"))
        multipleForSecondVector = int(input("multiple for Second vector (1 for none)"))
    if userIn == 1:
        result = [multipleForFirstVector*first + multipleForSecondVector*fourth, multipleForFirstVector*second + multipleForSecondVector*fifth, multipleForFirstVector*third + multipleForSecondVector*sixth]
        print("[", result[0], result[1], result[2], "]")
    elif userIn == 2:
        result = [multipleForFirstVector*first - multipleForSecondVector*fourth, multipleForFirstVector*second - multipleForSecondVector*fifth, multipleForFirstVector*third - multipleForSecondVector*sixth]
        print("[", result[0], result[1], result[2], "]")
    elif userIn == 3:
        import numpy as np
        a = np.array([first, second, third])
        b = np.array([fourth, fifth, sixth])
        result = np.dot(a, b)
        print(result)
    else:
        break

