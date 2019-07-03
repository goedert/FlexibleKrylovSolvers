import numpy as np
from scipy.sparse.linalg import gmres

class Solver:

    def __init__(self, params):
        pass


    # Based on the attributes of A, the solver will chose the best solution scheme
    # This method returns:
    #                             -- the solution
    #                             -- an np array with the norm of the residual over the iterations
    #                             -- iteration count
    #                             -- the amount of matrix x vector multiplications
    def solve(self, whichSolver, A, b, x0=None):

        if whichSolver=="GMRES":
            output = self.GMRES(A, b, x0)

        elif whichSolver=="FGMRES":
            output = self.FGMRES(A, b, x0)

        elif whichSolver=="GCR":
            output = self.GCR(A, b, x0)

        elif whichSolver=="GMRESR":
            output = self.GMRESR(A, b, x0)

        else:
            raise Exception("The requested inverter is not currently implemented.")

        return output

    # Solvers factory
    # ---------------

    # GMRES (re-started)
    def GMRES(self, A, b, x0):
        print("GMRES is under construction...")

        dims = A.getDims()
        x = np.zeros(dims[0])

        return (x, [1,2,3], 5, [1,2,3])


    # GMRESR
    def GMRESR(self, A, b, x0):
        print("GMRESR is under construction...")

        dims = A.getDims()
        x = np.zeros(dims[0])

        return (x, [1,2,3], 5, [1,2,3])


    # Flexible GMRES
    def FGMRES(self, A, b, x0):
        print("FGMRES is under construction...")

        dims = A.getDims()
        x = np.zeros(dims[0])

        return (x, [1,2,3], 5, [1,2,3])


    # GCR
    def GCR(self, A, b, x0):
        print("GCR is under construction...")

        dims = A.getDims()
        x = np.zeros(dims[0])

        return (x, [1,2,3], 5, [1,2,3])
