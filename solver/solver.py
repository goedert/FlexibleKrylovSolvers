import numpy as np
from scipy.sparse.linalg import gmres

class Solver:

    def __init__(self, params):
        pass


    # This method returns:
    #                     -- the solution
    #                     -- an np array with the norm of the residual over the iterations
    #                     -- iteration count
    #                     -- the amount of matrix x vector multiplications
    def solve(self, whichSolver, A, b, tol, extraParams, x0=None):

        self.itersCounter = 0
        self.matMulsCounter = 0

        if whichSolver=="GMRES":
            if ('restartLength' not in extraParams):
                raise Exception("Must specify re-start length when calling GMRES.")
            output = self.GMRES(A, b, tol, extraParams['restartLength'], x0)

        elif whichSolver=="FGMRES":
            output = self.FGMRES(A, b, tol, x0)

        elif whichSolver=="GCR":
            output = self.GCR(A, b, tol, x0)

        elif whichSolver=="GMRESR":
            output = self.GMRESR(A, b, tol, x0)

        else:
            raise Exception("The requested inverter is not currently implemented.")

        return output

    # Solvers factory
    # ---------------

    # GMRES (re-started)
    def GMRES(self, A, b, tol, restartLength, x0):
        # TODO: remove this line
        print("GMRES is under construction...")

        residuals = list()
        matMuls = list()

        # Re-naming of 'restartLength', for readability
        m = restartLength

        # Dimension of the problem
        matDims = b.shape[0]

        if x0==None:
            x0 = np.zeros(matDims)

        #relNormOfRes = r0Norm/r0Norm
        relNormOfRes = 1.0

        #np.append(a, z, axis=1)

        while relNormOfRes>tol:

            # Empty matrix of size matDims x restartLength, for the
            # storage of the orthonormal vectors produced by Arnoldi
            V = np.empty([matDims,m])

            # Hesselnberg matrix
            h = np.zeros([m+1,m])

            # Initial residual
            r0 = b - A.dot(x0)
            r0Norm = np.linalg.norm(r0)

            # Initial vector for the construction of V: the residual
            V[:,0] = r0 / r0Norm

            # beta * e1, in reduced dim
            b = np.zeros(m+1)
            b[0] = r0Norm

            # Counter for the outer loop
            self.itersCounter += 1

            luckyBreak = 0
            tolReached = 0

            for k in range(restartLength):

                # w = A * V[k], i.e. A times the k-th column of V
                w = A.dot(V[:,k])

                #r = b - A.dot(x0)

                # Orthogonalization procedure
                for j in range(k+1):
                    h[j,k] = np.dot(V[:,j], w)
                    w -= h[j,k] * V[:,j]
                h[k+1,k] = np.linalg.norm(w)

                # If we haven't reached the last iteration
                if k<(m-1): V[:,(k+1)] = w / h[k+1,k]

                # If lucky break
                if h[k+1,k]==0:
                    luckyBreak=1
                    break
                else:
                    partialResult = np.linalg.lstsq(h, b)[0]
                    partialResult = np.dot(V[:,:k].transpose(), partialResult)
                    x = x0 + partialResult

                    r = b - A.dot(x)
                    eps = np.linalg.norm(x) / r0Norm
                    residuals.append(eps)

                    if eps < tol:
                        tolReached = 1
                        break

            if luckyBreak==1:

                partialResult = np.linalg.lstsq(h, b)[0]
                partialResult = np.dot(V[:,:k].transpose(), partialResult)
                x = x0 + partialResult

                r = b - A.dot(x)
                eps = np.linalg.norm(r) / r0Norm
                residuals.append(eps)

                if eps < tol:
                    tolReached = 1
                    break

            # Exit the outer loop in case of tolerance reached
            if tolReached == 1: break

            # If tolerance hasn't been reached, then set x0 and re-start
            x0 = np.copy(x)

            # FIXME
            matMuls.append(1)

        #dims = A.getDims()
        #x = np.zeros(dims[0])

        return (x, residuals, self.itersCounter, matMuls)


    # GMRESR
    def GMRESR(self, A, b, tol, x0):
        print("GMRESR is under construction...")

        dims = A.getDims()
        x = np.zeros(dims[0])

        return (x, [1,2,3], 5, [1,2,3])


    # Flexible GMRES
    def FGMRES(self, A, b, tol, x0):
        print("FGMRES is under construction...")

        dims = A.getDims()
        x = np.zeros(dims[0])

        return (x, [1,2,3], 5, [1,2,3])


    # GCR
    def GCR(self, A, b, tol, x0):
        print("GCR is under construction...")

        dims = A.getDims()
        x = np.zeros(dims[0])

        return (x, [1,2,3], 5, [1,2,3])
