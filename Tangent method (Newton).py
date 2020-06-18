def function(x):
    pass  # return your func


def function_diff_1(x):
    pass  # return your func


def function_diff_2(x):
    pass  # return your func


def solve(x):
    return round((x - function(x)/function_diff_1(x)), 5)


print('View segment [a; b]')
a = int(input('Enter a: '))
b = int(input('Enter b: '))
e = 0.01

x0 = a if function(a) * function_diff_2(a) > 0 else b
print('***********************************')
print(f'Start segment: [{a}, {b}]')
i = 0
x1 = solve(x0)
eps = round(abs(x1 - x0), 4)
while eps > e:
    eps = round(abs(x1 - x0), 4)
    x0, x1 = x1, solve(x1)
    i += 1

print(f'\nNumber of iterations: {i}')
print(f'Answer: {x0} ± {eps}')