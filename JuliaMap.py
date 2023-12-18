'''
Julia map
Written by Jonathan De Sousa
Date: 16-12-2023
'''

import numpy as np
import matplotlib.pyplot as plt

# Julia set 1: c = -0.101 + 0.956i

# Discretise Re and Im parts of complex plane
Re = np.linspace(start=-3, stop=3, num=501)
Im = np.linspace(start=-3, stop=3, num=501)

# Mesh complex plane
X, Y = np.meshgrid(Re,Im)
Z = X + 1j*Y

# Set parameters
max_iter   = 2.75*(10**1); #max interations - used as convergence criteria
max_mod    = 10**6; #max modulus of z - used as divergence criteria
julia_iter = np.ones(np.shape(Z))*max_iter
c          = -0.101 + 0.956j

for u in range(np.shape(X)[0]):
    for v in range(np.shape(Y)[1]):
        
        Z_0 = Z[u][v]; #set as constant so that no need to constantly call C(u,v)
        count = 0
        
        while count < max_iter:
            z_n = Z_0**2 + c
            if abs(z_n) > max_mod:
                julia_iter[u][v] = count
                break
            
            Z_0 = z_n
            count = count + 1

# Plot Julia set
plt.contourf(np.real(Z), np.imag(Z), julia_iter, 100);
# [~,h1] = contourf(real(Z),imag(Z),julia_iter,100);
# set(h1,'LineColor','none')
# colormap(flipud(ColorMap))
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
# plt.title(sprintf('Julia Map, c = %.3f + %.3fi',real(c),imag(c)),'FontSize',15)
plt.gca().set_aspect('equal')
plt.show()