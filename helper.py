#helper file
import math
from sympy import init_printing
def Norm(vector):
   result = math.sqrt(vector[0]^2 + vector[1]^2 + vector[2]^2)
   return result
def Dot(vector1, vector2):
   result = vector1[0]*vector2[0] + vector1[1]*vector2[1] + vector1[2]*vector2[2]
   return result
# def Angle(vector1, vector2):
#    dotProduct = Dot(vector1, vector2)
#    normVec1 = Norm(vector1)
#    normVec2 = Norm(vector2)
#    bottom = normVec1*normVec2
#    result = math.degrees(math.acos(dotProduct / bottom))
#    return result
