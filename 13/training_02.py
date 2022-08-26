import numpy as np
import matplotlib.pyplot as plt

x1_plot, x2_plot = np.meshgrid([np.arange(-0.5,5,0.1)], [np.arange(-0.5,2.5,0.1)])
fx_plot = (x1_plot-2)**2 + 2*(x2_plot-2)**2
plt.contour(x1_plot, x2_plot, fx_plot)
plt.xlabel('x0'); plt.ylabel('x1'); plt.colorbar(); plt.grid()

iter = 0 # iteration
tol = 1e-6 # tolerance level for gradient norms
x = [0,0] # initial poin (Starting point)
fx = (x[0]-2)**2 + 2*(x[1]-2)**2

Gf = np.array([2*(x[0]-2), 4*(x[1]-2)]) # Gradient at starting point
norm_Gf = np.linalg.norm(Gf)
H = np.array([[2, 0], [0, 4]]) # Hessian matrix at starting point
d_k = -np.linalg.inv(H) @ Gf # Searching direction at starting point

plt.plot(x[0], x[1] , 'r*')

print('iter      x_0       x_1       |Gf|         f(x)')
print('----   ---------  --------   --------    ---------')
print('{:3d}    {:>9.6f}   {:>8.6f}   {:>8.6f}   {:>8.6f}'.format(iter, x[0], x[1], norm_Gf, fx))

while(True):
    iter += 1
    ds = 0.0001
    s_range = np.arange(0,100,ds)
    x_next = np.array([x[0] + d_k[0]*s_range, x[1] + d_k[1]*s_range])
    fx_next = (x_next[0,:] - 2)**2 + 2*(x_next[1,:] - 2)**2
    
    idx = np.where(fx_next == min(fx_next))
    
    x_prev = x
    
    x = [x_next[0][idx], x_next[1][idx]]
    fx = fx_next[idx]
    Gf = np.array([2*(x[0]-2), 4*(x[1]-2)])
    norm_Gf = np.linalg.norm(Gf)
    H = np.array([[2, 0], [0, 4]])
    d_k = -np.linalg.inv(H) @ Gf


    plt.plot(x[0], x[1] , 'r*')
    plt.plot([x_prev[0], x[0]], [x_prev[1], x[1]], 'r-')
    
    print('{:3d}    {:>9.6f}   {:>8.6f}   {:>8.6f}   {:>8.6f}'.format(iter, float(x[0]), float(x[1]), norm_Gf, fx[0]))
    
    if norm_Gf <= tol: break

plt.show()
print('done!')