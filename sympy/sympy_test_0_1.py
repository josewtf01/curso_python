from sympy import *

x,y,z = symbols('x y z')

#init_printing(use_unicode=True)

# derivadas
D_cos = diff(cos(x),x)
print("D^1 cos(x) = ",D_cos, "\n")

D_1 = diff(exp(x**2),x)
print("D^1 exp(x**2) = ",D_1,"\n")

D_4 = diff(x**4,x,x,x)
#D_4 = diff(x**4,x,3)
print("D^3 x^4 = ",D_4,"\n")

expr = exp(x*y*z)
#d_7 = diff(expr,x,y,y,z,z,z,z)
d_7 = diff(expr,x,y,2,z,4)
print(d_7,"\n")
print(factor(d_7),"\n")
