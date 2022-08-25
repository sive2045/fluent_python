import numpy as np

def func(x):
    return x**4 - 14*(x**3) + 60*(x**2) - 70*x

epsilon = 0.000_01
x = 0
iteration = 0
dx = 1
f = func(x)

print('iter       x          d_x        f(x)')
print('----   ---------    --------   --------')
print('{:3d}    {:.6f}     {:.6f}   {:.6f}'.format(iteration, x, dx, f))

while(True):
    iteration += 1
    
    f_prime = 4*(x**3) - 42*(x**2) + 120*x - 70 # f'(x) at x_k
    f_double_prime = 12*(x**2) - 84*x + 120 # f''(x) at x_k
    
    x_new = x - (f_prime / f_double_prime)
    
    dx = np.abs(x_new - x)
    x = x_new
    
    f = func(x)
    print('{:3d}    {:.6f}     {:.6f}   {:.6f}'.format(iteration, x, dx, f))
    
    if dx <= epsilon: break

print('done!')