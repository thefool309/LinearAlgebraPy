# notes page for LA
import sympy as sy
import numpy as np
from sympy.physics.vector import ReferenceFrame
from sympy import init_printing
import math

menuoptions = ["1 - Add Vectors", "2 - Subtract vectors", "3 - Dot product of vectors", "4 - Angle Between Vectors",
               "5 - Normalize Vec1", "6 - Normalize Vec2", "7 - Cross Product",
               "8 - Calculate distance between Vectors", "Else - Exit"]
userIn = 0
while userIn < len(menuoptions):
    # gather two LA vectors
    first = int(input("please enter first int:"))
    second = int(input("please enter second int:"))
    third = int(input("please enter third int:"))
    vList1 = [first, second, third]  # store into lists just in case
    npVector1 = np.array([first, second, third])
    norm1 = np.linalg.norm(npVector1)
    print(norm1)

    fourth = int(input("Please enter the first int of the second vector:"))
    fifth = int(input("Please enter the second int of the second vector:"))
    sixth = int(input("Please enter the third int of the second vector:"))
    vList2 = [fourth, fifth, sixth]  # store into lists just in case
    npVector2 = np.array([fourth, fifth, sixth])
    norm2 = np.linalg.norm(npVector2)
    print(norm2)

    for i in menuoptions:  # print menu options
        print(i)
    print('\n')

    userIn = int(input("Select a menu option:"))
    #check userIn
    if userIn < 3:
        multipleForFirstVector = int(input("multiple for first vector (1 for none):"))
        multipleForSecondVector = int(input("multiple for Second vector (1 for none)"))
    if userIn == 1:
        result = [multipleForFirstVector * first + multipleForSecondVector * fourth,
                  multipleForFirstVector * second + multipleForSecondVector * fifth,
                  multipleForFirstVector * third + multipleForSecondVector * sixth]
        print("[", result[0], result[1], result[2], "]")
    elif userIn == 2:
        result = [multipleForFirstVector * first - multipleForSecondVector * fourth,
                  multipleForFirstVector * second - multipleForSecondVector * fifth,
                  multipleForFirstVector * third - multipleForSecondVector * sixth]
        print("[", result[0], result[1], result[2], "]")
    elif userIn == 3:
        result = np.dot(npVector1, npVector2) / norm1 * norm2
        print(result)
    elif userIn == 4:
        result = math.degrees(np.arccos(np.dot(npVector1, npVector2) / (norm1 * norm2)))
        print(result)
    elif userIn == 5:
        result = vVector1.normalize()
        sy.pprint(result)
    elif userIn == 6:
        result = vVector2.normalize()
        sy.pprint(result)
    elif userIn == 7:
        result = np.cross(npVector1, npVector2)
        print(result)
    elif userIn == 8:
        e = ReferenceFrame('e')
        vVector1 = first * e.x + second * e.y + third * e.z
        vVector2 = fourth * e.x + fifth * e.x + sixth * e.z
        # vector distance between these two
        distanceVerticeResults = [fourth - first, fifth - second, sixth - third]  #vector AB
        c = sy.Array([distanceVerticeResults[0], distanceVerticeResults[1], distanceVerticeResults[2]])
        v = distanceVerticeResults[0] * e.x + distanceVerticeResults[1] * e.y + distanceVerticeResults[2] * e.z
        print("Distance between Vectors Formula Form:")
        sy.pprint(v)
        print("Distance between Vectors Brackets form:", c)
        # magnitude with sympy
        m = v.magnitude()
        print("magnitude of distance between vectors", v, "is", m)
        # normalize with sympy
        print("normalized:")
        y = v.normalize()
        sy.pprint(y)
        userIn = 0
    else:
        break
