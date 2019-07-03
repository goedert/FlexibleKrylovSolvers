# Local dir
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path += '/'

# Add solver resources to the Python PATH
import sys
sys.path.append(dir_path + '../matrix/')
sys.path.append(dir_path + '../solver/')
sys.path.append(dir_path + '../aux/')

import numpy as np

from matrix import Matrix
from solver import Solver
from plotter import plotter

# This test computes/plots, for a matrix of fixed size, the
# behaviour of the residual vs the count of matrix-vector
# multiplications

def plot_resid_vs_matmuls():

    inverters = ["GMRES", "FGMRES"]
    #matrices = ["laplace", "laplace_2"]

    # Sizes for each matrix type
    #matrices = dict()
    #matrices['cz'] = [148, 308, 628, 1268, 2548, 5108]
    matrices = dict()
    matrices['cz'] = 148

    # Solver object - can be used for any matrix
    sol_params = dict()
    sol = Solver(sol_params)

    for mat_label in matrices:

        # Construct the matrix
        mat_params = dict()
        mat_params['fromSuiteSparse'] = True
        mat_params['whichMatrix'] = mat_label
        mat_size = matrices[mat_label]
        mat_params['dims'] = [mat_size,mat_size]
        M = Matrix(mat_params)

        # Build a rhs for this matrix
        matDims = M.getDims()
        b = np.ones(matDims[0])

        for inv in inverters:

            x,residuals,it_count,nr_matvec_muls = sol.solve(inv, M, b)

            filename = 'test002_' + inv + '_' + mat_label + '_' + str(mat_size) + '.png'
            plotter(residuals, nr_matvec_muls, "nr mat vec multipls", "residual", filename)
