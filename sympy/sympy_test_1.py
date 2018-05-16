from sympy import *

# x, y, z, t = symbols('x y z t')
#ponemos los simbolos antes de utilizar las funciones
x = symbols('x')

# init_printing(use_unicode=True)
# --------------------------------

# derivadas

# f(x) = sin(x)*e^(x)

expr = sin(x)*exp(x)
d_expr = diff(expr,x)
print(d_expr,"\n")

# integrales

# f(x) = e^(-x^2)
expr = exp(-x**2)
int_expr = integrate(expr,(x,-oo,oo))
print(int_expr,"\n")

# limites
expr = sin(x)/x
lim_expr = limit(expr,x,0)
print(lim_expr,"\n")

# calculo de raices

# f(x) = x^2 - 2
expr = x**2 - 2
roots_expr = solve(expr,x)
print(roots_expr,"\n")

# ecuaciones diferenciales

# y^´´ - y = e^t
t = symbols('t')
y = Function('y')
expr = dsolve( Eq( y(t).diff(t,t) - y(t), exp(t)), y(t) )
print(expr,"\n")

# eigenvalores de una matriz

# [ 1  2 ]
# [ 2  2 ]

expr = Matrix( [ [ 1 , 2 ] , [ 2 , 2 ] ] ).eigenvals()
print(expr,"\n")

# http://www.sympy.org/es/
