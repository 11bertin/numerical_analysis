from sympy import *

f = symbols('f', cls=Function)

x = symbols('x')

eq = Eq(f(x).diff(x,1)+f(x)+f(x)**2, 0)

print(dsolve(eq, f(x)))

C1 = symbols('C1')

eqr = -C1/(C1 - exp(x))

eqr1 = eqr.subs(x, 0)

print(solveset(eqr1 - 1, C1))

eqr2 = eqr.subs(C1, 1/2)