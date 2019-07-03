import scipy.io as sio
import os

# TODO: imports

class Matrix:

    def __init__(self, params, A=None):

        # Default params
        #self.possibleMatrices = ['laplace', 'laplace_2']
        self.possibleMatrices = ['cz']
        self.isSparse = True
        self.isHermitian = False

        # Extract params from 'params'
        if ('fromSuiteSparse' not in params) or (params['fromSuiteSparse']==False):
            # Build from the input matrix A
            self.mat = A

        # else, import from SuiteSparse (if possible)
        else:

            if ('dims' not in params):
                raise Exception("Please specify the dimensions of your matrix.")

            self.dims = params['dims']

            if ('whichMatrix' not in params):
                raise Exception("Please specify the name of the matrix you would like to import from SuiteSparse.")

            self.whichMatrix = params['whichMatrix']

            if (params['whichMatrix'] not in self.possibleMatrices):
                raise Exception('The matrix requested is not currently available.')

            self.mat = self.importFromSuiteSparse()

            #print(self.mat.todense())


    # Imports the matrix from the SuiteSparse 'database'
    def importFromSuiteSparse(self):

        filename = os.path.dirname(os.path.realpath(__file__))
        filename += '/'
        filename += self.whichMatrix + '/' + self.whichMatrix + str(self.dims[0]) + '.mtx'
        M = sio.mmread(filename)

        return M


    def getDims(self):
        return self.mat.shape


    def getMat(self):
        return self.mat
