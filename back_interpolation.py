import pylab
import numpy as np
from scipy.interpolate import lagrange

#  Enter your values
x = np.array([])
y = np.array([])
r = 0

print('*** 1 way ***\n\n Polynomial in х: \n')
print(lagrange(x, y)-r)
print(f'\nPolynomial roots y*=L2(x):  {np.roots(lagrange(x, y)-r)}')
print('\n*** 2 way ***\n\n Polynomial in y: \n')
print(lagrange(y, x))
print(f'\nRoot: {lagrange(y, x)(r)}')

x_new = np.linspace(1, np.max(x), 100)
y_new = [lagrange(x, y)(i) for i in x_new]
pylab.subplot(1, 2, 1)
pylab.plot(x_new, y_new)
pylab.scatter(np.roots(lagrange(x, y)-r), [r, r], marker='*')
pylab.title('1 way')
pylab.grid(True)

y_new = np.linspace(5, 30, 100)
x_new = [lagrange(y, x)(i) for i in y_new]
pylab.subplot(1, 2, 2)
pylab.plot(y_new, x_new)
pylab.scatter(r, lagrange(y, x)(r), marker='*', s=60)
pylab.title('2 way')
pylab.grid(True)
pylab.show()
