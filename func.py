exec("print('hello world')")
from math import sqrt
scope = dict()
exec("sqrt=1", scope)
print(sqrt(4))
print(scope['sqrt'])
print(scope.keys())

print(eval(input("Enter an arithmetic expression:")))

scope = {}
scope['x'] = 2
scope['y'] = 3
print(eval('x*y', scope))


scope = dict()
exec('x=2', scope)
print(eval('x*x', scope))