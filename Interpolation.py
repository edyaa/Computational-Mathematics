import numpy as np
import pylab
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

# Enter your values
x = np.array([])
y = np.array([])

x_lag = np.array([])
y_lag = np.array([])
r = 0


def product(val, n):
    """ Auxiliary generator for calculating the product of coordinate differences """
    mul = 1
    for i in range(n):
        if i: mul *= val - x[i - 1]
        yield mul


C = []

# calculate the coefficients
for n in range(len(x)):
    p = product(x[n], n + 1)
    C.append((y[n] - sum(C[k] * next(p) for k in range(n))) / next(p))


def f(v):
    """ The value of the polynomial at v """
    return sum(C[k] * p for k, p in enumerate(product(v, len(C))))


poly_lag = lagrange(x_lag, y_lag)
print(f'\nLagrange Interpolation Polynomial:\n\n {poly_lag}\n')
print(f'y = L2(r) = {poly_lag(r)}\n')
print('Newton Interpolation Polynomial:\n')
print()
print(f'Q(r) = {f(r)}')
print("coefficients: ")
for i in C:
    print(i)

xnew1 = np.linspace(np.min(x), np.max(x), 100)
ynew1 = [poly_lag(x) for x in xnew1]
pylab.subplot(1, 2, 1)
pylab.plot(xnew1, ynew1)
pylab.scatter(r, poly_lag(r), marker='*', s=60)
pylab.title('Lagrange Interpolation Polynomial')
pylab.grid(True)

xnew2 = np.linspace(np.min(x), np.max(x), 100)
ynew2 = [f(x) for x in xnew1]
pylab.subplot(1, 2, 2)
pylab.plot(xnew2, ynew2)
pylab.scatter(r, f(r), marker='*', s=60)
pylab.title('Newton Interpolation Polynomial')
pylab.grid(True)
pylab.show()

