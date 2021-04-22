import math
from sklearn.metrics.pairwise import laplacian_kernel
import numpy as np

# return an array K of size (N, N), depth d_max, first fix_dep layers fixed
def kernel_value(X, gamma=None): 
    return laplacian_kernel(X, gamma=gamma)