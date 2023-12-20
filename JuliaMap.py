'''
Julia map
Written by Jonathan De Sousa
Date: 16-12-2023

f(z) -> z^2 + c
'''

import matplotlib.pyplot as plt
from methods import *

count_threshold     = 2.75*(10**1);
modulus_threshold   = 10**9;
complex_constant    = -0.101 + 0.956j

meshgrid = generate_complex_meshgrid(real_range=[-3,3], 
                            imaginary_range=[-3,3],
                            real_count=501,
                            imaginary_count=501)

count_matrix = generate_iteration_map(count_threshold,
                                      modulus_threshold,
                                      complex_constant,
                                      meshgrid)

plot_filled_contour_map(meshgrid,
                        count_matrix,
                        countour_levels=100,
                        color_map='seismic')