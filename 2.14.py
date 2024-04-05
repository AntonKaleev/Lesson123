import sympy

t = sympy.symbols('t')
y = sympy.Function('y')

equation = sympy.Eq(y(t).diff(t), y(t)+t)
print(equation)
solution = sympy.dsolve(equation)
C1=sympy.solve(solution.subs(t,0).subs(y(0),2),'C1')[0]#Подставляем условия
z=solution.subs('C1',C1,t=1)
z=z.subs(t,1)

print(z)

