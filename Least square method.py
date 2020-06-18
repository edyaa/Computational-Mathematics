from pylab import *
import numpy as np

# Enter your values. Example:

x = np.array([3, 4, 5, 6, 7])
y = np.array([13.6, 12, 11.2, 10, 9.6])

A = np.array([[5, 25, 135], [25, 135, 775], [135, 775, 4659]])
b = np.array([56.4, 272, 1424.8])
print(np.linalg.solve(A, b))

m = vstack((x**2, x, ones(len(x)))).T
s = lstsq(m, y, rcond=1)[0]
x_ = linspace(2, 8, 101)
plot(x, y, 'D')
plot(x_, s[0]*x_**2+s[1]*x_+s[2], '-', lw=2)
print(f'c0 = {round(s[2], 4)} '
      f'\nc1 = {round(s[1], 4)} '
      f'\nc2 = {round(s[0], 4)}')
grid()
plt.show()
