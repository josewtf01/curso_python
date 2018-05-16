import math

print(math.sqrt(9),"\n")

print(math.sqrt(8),"\n")

import sympy

print(sympy.sqrt(3),"\n")

print(sympy.sqrt(8),"\n")

from sympy import symbols

x,y= symbols('x y')
expr = x + 2*y
print(expr,"\n")

expr = expr + 1
print(expr,"\n")

expr = expr - x
print(expr,"\n")

expr = x + 2*y
print(expr,"\n")

expr = x * expr
print(expr,"\n")

from sympy import expand,factor
expanded_expr = expand(expr)
print(expanded_expr,"\n")

print(factor(expanded_expr),"\n")
