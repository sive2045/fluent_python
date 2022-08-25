import numpy as np

def func(x):
    return x**4 - 14*(x**3) + 60*(x**2) - 70*x

epsilon = 0.000_01
a_k = 0
b_k = 2
dx = b_k - a_k
f = func(b_k)
iteration = 0

print('iter      a_k       b_k         d_x      f(b_k)')
print('----   ---------  --------   --------   --------')
print('{:3d}    {:.6f}   {:.6f}   {:.6f}   {:.6f}'.format(iteration, a_k, b_k, dx, f))

while(True):
    iteration += 1
    c_k = 0.5*(a_k + b_k)
    f_prime_c_k = 4*(c_k**3) - 42*(c_k**2) + 120*(c_k) - 70 # f'(k) at a_k
    
    if f_prime_c_k > 0:
        b_k = c_k
    elif f_prime_c_k < 0:
        a_k = c_k
    else:
        a_k = c_k
        b_k = c_k
    
    f = func(c_k)
    dx = b_k - a_k
    
    print('{:3d}    {:.6f}   {:.6f}   {:.6f}   {:.6f}'.format(iteration, a_k, b_k, dx, f))
    
    if dx <= epsilon: break

print('done!')