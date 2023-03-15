from sympy import *
from sympy.printing.latex import latex

# Define some mathematical expressions
x, y, z = symbols('x y z')
expr1 = x**2 + y**2 + z**2
expr2 = 1/x + 1/y + 1/z

# Print LaTeX code for the expressions
print("Expression 1: " + latex(2))
print("Expression 2: " + latex(expr2))
