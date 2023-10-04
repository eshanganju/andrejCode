"""Code for micrograd"""

#imports
import math
import numpy as np
import matplotlib.pyplot as plt
from graphviz import Diagraph

# Function definitions

def f(x):
    return 3*x**2 - 4*x + 5

# Run

print(f(3.0))

xs = np.arange(-5,5,0.25)
ys = f(xs)
#plt.plot(xs,ys)
#plt.show()

h = 0.0001
x = 2/3
slope = ( f(x) - f(x+h) ) / h
print( 'slope: ' + str(slope) )


# Complex functions
# inputs
a = 2.0
b = -3.0
c = 10
d = a * b + c
print(d)

d1  = a * b + c
c += h
d2 = a * b + c

print('d1', d1)
print('d2', d2)
print('slope', (d2-d1)/h)


# Adding datastuctures
"""Value objects"""

class Value: 
    
    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self._prev = set(_children)
        self._op = _op

    def __repr__(self):
        return f"Value(data={self.data})"

    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), '+')
        return out

    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), '*')
        return out

a = Value(data = 2.0)
b = Value(data = -3.0)
c = Value(10.0)
d = a * b + c
print(a)
print(a + b)
print(d)
print(d._prev)
print(d._op)


