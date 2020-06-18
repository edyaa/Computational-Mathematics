def function(x):
    pass  # Enter your equation


print('View segment [a; b]')
a = int(input('Enter a: '))
b = int(input('Enter b: '))
e = 0.1

x0 = a if function(a) > function(b) else b
print('***********************************')
print(f'Start segment: [{a}, {b}]')
i = 0
x1 = function(x0)
eps = round(abs(x1 - x0), 4)
while eps > e:
    eps = round(abs(x1 - x0), 4)
    x0, x1 = x1, function(x1)
    i += 1

print(f'\nNumber of iterations: {i}')
print(f'Answer: {x0} ± {eps}')