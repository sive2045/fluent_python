import numpy as np
import matplotlib.pyplot as plt

x1_plot, x2_plot = np.meshgrid([np.arange(-1,5,0.1)], [np.arange(-1,5,0.1)])
fx_plot = 4*(x1_plot**2) -4*(x1_plot*x2_plot) + 2*(x2_plot**2)
plt.contour(x1_plot, x2_plot, fx_plot)
plt.xlabel('x0'); plt.ylabel('x1'); plt.colorbar(); plt.grid()

iter = 0 # iteration
tol = 1e-6 # tolerance level for gradient norms
x = [2,3] # initial poin (Starting point)
fx = 4*x[0]**2 - 4*x[0]*x[1] + 2*x[1]**2

Gf = np.array([8*x[0] - 4*x[1], 4*x[1] - 4*x[0]]) # Gradient at starting point
norm_Gf = np.linalg.norm(Gf)

plt.plot(x[0], x[1] , 'r*')

print('iter      x_0       x_1       |Gf|         f(x)')
print('----   ---------  --------   --------    ---------')
print('{:3d}    {:>9.6f}   {:>8.6f}   {:>8.6f}   {:>8.6f}'.format(iter, x[0], x[1], norm_Gf, fx))

while(True):
    iter += 1
    ds = 0.0001
    s_range = np.arange(0,100,ds)
    x_next = np.array([x[0] - Gf[0]*s_range, x[1] - Gf[1]*s_range])
    fx_next = 4*x_next[0,:]**2 -4*x_next[0,:]*x_next[1,:] + 2*x_next[1,:]**2
    
    idx = np.where(fx_next == min(fx_next))
    
    x_prev = x
    
    x = [x_next[0][idx], x_next[1][idx]]
    fx = fx_next[idx]
    Gf = [8*x[0] - 4*x[1], 4*x[1] - 4*x[0]]
    norm_Gf = np.linalg.norm(Gf)
    
    plt.plot(x[0], x[1] , 'r*')
    plt.plot([x_prev[0], x[0]], [x_prev[1], x[1]], 'r-')
    
    print('{:3d}    {:>9.6f}   {:>8.6f}   {:>8.6f}   {:>8.6f}'.format(iter, float(x[0]), float(x[1]), norm_Gf, fx[0]))
    
    if norm_Gf <= tol: break

plt.show()
print('done!')