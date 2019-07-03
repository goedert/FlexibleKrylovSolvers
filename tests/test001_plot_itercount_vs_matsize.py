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

# This test computes/plots the iteration count vs matrix size,
# to test how present 'critical slowing down' is

def plot_itercount_vs_matsize():

    inverters = ["GMRES", "FGMRES"]
    #matrices = ["laplace", "laplace_2"]

    # Sizes for each matrix type
    matrices = dict()
    matrices['cz'] = [148, 308, 628, 1268, 2548, 5108]

    # Solver object - can be used for any matrix
    sol_params = dict()
    sol = Solver(sol_params)

    for inv in inverters:

      for mat_label in matrices:

          it_counts = list()
          matsizes = list()

          for mat_size in matrices[mat_label]:

              # Construct the matrix
              mat_params = dict()
              mat_params['fromSuiteSparse'] = True
              mat_params['whichMatrix'] = mat_label
              mat_params['dims'] = [mat_size,mat_size]
              M = Matrix(mat_params)

              # Build a rhs for this matrix
              #b = np.
              matDims = M.getDims()
              b = np.ones(matDims[0])

              x,residuals,it_count,nr_matvec_muls = sol.solve(inv, M, b)
              it_counts.append(it_count)
              matsizes.append(mat_size)

          filename = 'test001_' + inv + '_' + mat_label + '.png'
          plotter(it_counts, matsizes, "matrix size", "iteration count", filename)
