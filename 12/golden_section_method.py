import numpy as np

def func(x):
    return x**4 - 14*(x**3) + 60*(x**2) - 70*x

epsilon = 0.000_01
step_size = (3 - np.sqrt(5))/2
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
   
    hat_a_k = a_k + step_size*(b_k - a_k)
    hat_b_k = b_k - step_size*(b_k - a_k)
   
    f_a_k = func(a_k)
    f_b_k = func(b_k)
   
    f_hat_a_k = func(hat_a_k)
    f_hat_b_k = func(hat_b_k)
    
    if f_hat_a_k < f_hat_b_k:
       if f_a_k > f_hat_a_k:
           b_k = hat_b_k
       else:
           b_k = hat_a_k
    elif f_hat_a_k > f_hat_b_k:
        if f_hat_b_k < f_b_k:
            a_k = hat_a_k
        else:
            a_k = hat_b_k
    else:
        a_k = hat_a_k
        b_k = hat_b_k
    
    f = func(b_k)
    dx = b_k - a_k
    
    print('{:3d}    {:.6f}   {:.6f}   {:.6f}   {:.6f}'.format(iteration, a_k, b_k, dx, f))
    
    if dx <= epsilon: break

print('done!')