# import math    >>imports library
 #import only one function  from the  library _math
from math import sqrt
def q_e_solver(a,b,c):
    d=b**2-4*a*c
    if d<0:
        return None
    elif d==0:
        x=-b/(2*a)
        return x
    else:
        x1=(-b+sqrt(d))/(2*a)
        x2=(-b-sqrt(d))/(2*a)      
    
    return x1, x2

print (q_e_solver(2, 5, -3))



        


