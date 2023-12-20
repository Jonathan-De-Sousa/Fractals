import numpy as np
import matplotlib.pyplot as plt


def generate_complex_meshgrid(real_range, 
                              imaginary_range, 
                              real_count, 
                              imaginary_count):
    Re = np.linspace(start=real_range[0], stop=real_range[1], num=real_count)
    Im = np.linspace(start=imaginary_range[0], stop=imaginary_range[1], num=real_count)

    X, Y = np.meshgrid(Re,Im)
    Z = X + 1j*Y

    return Z


def generate_iteration_map(count_threshold,
                           modulus_threshold,
                           complex_constant,
                           meshgrid):
    
    count_matrix = np.ones(np.shape(meshgrid))*count_threshold

    for real in range(np.shape(meshgrid)[0]):
        for imaginary in range(np.shape(meshgrid)[1]):
            
            Z_0 = meshgrid[real][imaginary]
            count = 0
            
            while count < count_threshold:
                z_n = Z_0**2 + complex_constant
                if abs(z_n) > modulus_threshold:
                    count_matrix[real][imaginary] = count
                    break
                
                Z_0 = z_n
                count = count + 1

    return count_matrix


def plot_filled_contour_map(meshgrid, count_matrix, countour_levels, color_map):
    plt.contourf(np.real(meshgrid), np.imag(meshgrid), count_matrix, levels=countour_levels)
    plt.set_cmap(color_map)
    plt.gca().set_aspect('equal')
    plt.show()
    
