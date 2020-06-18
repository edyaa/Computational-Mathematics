def function(_x):
    pass  # Enter your equation


print('View segment [a; b]')
a = int(input('Enter a: '))
b = int(input('Enter b: '))
e = 0.01
i = 0
x = (a + b) / 2
print('***********************************')
print(f'Start segment: [{a}, {b}]')

while (b-a)/2 > e:
    if function(a) * function(x) < 0:
        b = x
    else:
        a = x
    x = round((a + b) / 2, 5)
    i += 1

print(f'\nNumber of iterations: {i}')
print(f'Answer: {x} ± {round((b-a)/2, 4)}')
