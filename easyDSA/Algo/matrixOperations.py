import numpy
import copy
from math import pow

from numpy.lib.function_base import place
from numpy.linalg.linalg import _raise_linalgerror_eigenvalues_nonconvergence


class MatOperations:

    cacheDeterminantMEM = []

    # function to determine is the matrix is square that is n * n dimenional type
    @classmethod
    def isSquareMatrix(cls , matrix):

        n = len(matrix)

        # empty matrix is not a square matrix
        if(n == 0):
            return False

        # if every row has exactly n cols then it is a square matrix
        for i in range(n):
            m = len(matrix[i])

            if(n != m):
                return False

        return True


    # function to find the determinant of a matrix
    # accepts a list or a numpy array
    @classmethod
    def determinant(cls , matrix , cache = True , numpyOnly = False , roundedTo = 0 , limit = 5):

        def removeIandJinMat(matrix , i , j , numpyArray = False):

            if(numpyArray):
                matrix = numpy.delete(matrix, (i), axis=0)
                matrix = numpy.delete(matrix, (j), axis=1)
                return matrix

            else:
                # removing ith row and jth col
                return [row[: j] + row[j+1:] for row in (matrix[: i] + matrix[i+1:])]



        n = len(matrix)

        if(n < 1):
            raise ValueError("Empty matrix passed")

        
        # if the n is greator than 10 use the numpy determinant function
        if((n > limit) or numpyOnly):
            isNumpyArray = type(matrix) == numpy.ndarray

            if(isNumpyArray):
                return round(numpy.linalg.det(matrix) , roundedTo) 

            else:
                matrix = numpy.array(matrix)
                return round(numpy.linalg.det(matrix) , roundedTo) 

            


        # conforming if it is a square matrix
        result = cls.isSquareMatrix(matrix)

        # if not a square matrix , raise error
        if(result == False):
            raise ValueError("{} is not a square matrix".format(matrix))

        # return just number if the matrix only has 1 element
        if(n == 1):
            return round(matrix[0][0] , roundedTo)

        # return the determinant of 2 by 2 matrix
        if(n == 2):
            determinant2by2 = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
            return round(determinant2by2 , roundedTo) 


        isNumpyArray = type(matrix) == numpy.ndarray

        # if the result is in cache return it
        if(cache):
            for i in cls.cacheDeterminantMEM:

                if(type(i[0]) == numpy.ndarray or isNumpyArray):
                    if(numpy.array_equal(i[0] , matrix)):
                        return i[1]

                elif(i[0] == matrix):
                    return i[1]


        if(n > 2):

            finalDeterminant = 0

            # calculate the determinant
            # determinant is submission of aij (-1^(j) * determinant of new matrix)
            # here the new matrix is matrix excluding ith row , jth col 


            for i in range(n):

                subMat = removeIandJinMat(matrix , 0 , i , isNumpyArray)
    
                finalDeterminant = finalDeterminant + ((matrix[0][i] * cls.determinant(subMat)) * int(pow(-1 , i)))

            if(cache):
                cls.cacheDeterminantMEM.append([matrix , finalDeterminant])

            return round(finalDeterminant , roundedTo) 



    # function to find the cofactor matrix for the adjoint matrix
    # Aij = (-1)ij det(Mij)
    @classmethod
    def cofactorMatrix_adjoint(cls , matrix , cache = True):

        def removeIandJinMat(matrix , i , j , numpyArray = False):

            if(numpyArray):
                matrix = numpy.delete(matrix, (i), axis=0)
                matrix = numpy.delete(matrix, (j), axis=1)
                return matrix

            else:
                # removing ith row and jth col
                return [row[: j] + row[j+1:] for row in (matrix[: i] + matrix[i+1:])]


        # if the matrix is of numpy array type
        isNumpyArray = type(matrix) == numpy.ndarray

        result = []
        n = len(matrix)

        for i in range(n):

            tempList = []

            for j in range(len(matrix[i])):

                subMat = removeIandJinMat(matrix , i , j , isNumpyArray)
                

                # calculating Aij
                deter = cls.determinant(subMat , cache)

                if(int(deter) != 0):
                    Aij = int(pow(-1 , i+j)) * deter
                else:
                    Aij = deter



                # adding to list
                tempList.append(Aij)
            
            result.append(tempList)

        # if the numpy array is passed then the result will also be returned in the form of numpy array
        if(isNumpyArray):
            result = numpy.array(result)

        return result



    # function to find the transpose of a matrix
    @classmethod
    def transpose(cls , matrix):


        # if the matrix is of numpy array type
        isNumpyArray = type(matrix) == numpy.ndarray

        # if it is of numpy type , simply apply the transpose function
        if(isNumpyArray):
            newMatrix = matrix.transpose()

        # else apply transpose to a list
        else:
            n = len(matrix)

            try:
                m = len(matrix[0])
            except IndexError:
                raise ValueError("Matrix is empty")

            newMatrix = [] 

            # generate a dummy list of m by n dimension instead of n by m
            for i in range(m):
                newMatrix.append([0 for _ in range(n)])

            # assign the value
            for i in range(n):
                for j in range(m):
                    newMatrix[j][i] = matrix[i][j]
            
        return newMatrix



    
    # function to find the adjoint of a matrix
    @classmethod
    def adjointMatrix(cls , matrix , cache = True):

        cofactorMatrix = cls.cofactorMatrix_adjoint(matrix , cache)

        cofactorMatrix_transpose = cls.transpose(cofactorMatrix)

        return cofactorMatrix_transpose

    
    # function to find the inverse of a matrix
    @classmethod
    def inverseMatrix(cls , matrix , cache = True):


        # confirm it is a square matrix
        result = cls.isSquareMatrix(matrix)

        if(result == False):
            raise ValueError("{} is not a square matrix".format(matrix))


        # find the adjoint matrix
        adjointMatrix = cls.adjointMatrix(matrix , cache)

        n = len(adjointMatrix)

        # find determinant , should not be 0
        determinant = cls.determinant(matrix , cache)

        if(determinant == 0):
            raise ValueError("{} , determinant of this matrix is zero".format(matrix))

        # divide the determinant from each value in matrix
        for i in range(n):
            for j in range(len(adjointMatrix[i])):
                adjointMatrix[i][j] = adjointMatrix[i][j] / determinant

                # makes -0 = 0
                if(int(adjointMatrix[i][j]) == 0):
                    adjointMatrix[i][j] = abs(adjointMatrix[i][j])
        return adjointMatrix


    # function to find the mean of the matrix
    # mean = submission of all elements / total number of elements
    @classmethod
    def meanOfMatrix(cls , matrix):

        # if the matrix is of numpy array type
        isNumpyArray = type(matrix) == numpy.ndarray

        # use numpy mean method to find the mean of a numpy array type matrix
        if(isNumpyArray):
            return matrix.mean()
        
        submission = 0
        count = 0

        # iterate through rows
        for i in range(len(matrix)):

            # iterate through cols
            for j in range(len(matrix[i])):

                submission = submission + matrix[i][j]
                count = count + 1
            
        mean = submission / count

        return mean

        

    # function to find the covariance btw two matrixes
    @classmethod
    def covariance(cls , x , y):
        submission = 0

        lenX = len(x)

        if(lenX != len(y)):
            raise ValueError("x and y are not equal in length where x = {} , y = {}".format(x,y))

        for i in range(lenX):
            if(len(x[i]) != len(y[i])):
                raise ValueError("x and y are not equal in length where x = {} , y = {}".format(x,y))


        xMean = cls.meanOfMatrix(x)
        yMean = cls.meanOfMatrix(y)

        elementCount = 0

        for i in range(lenX):
            for j in range(len(x[i])):
                elementCount = elementCount + 1
                submission = submission + ((x[i][j] - xMean) * (y[i][j] - yMean))

        return submission / (elementCount - 1)


    # function to make a covariance matrix
    @classmethod
    def covarianceMatrix(cls , x , y):

        """
        [[cov(X , X) , cov(X , Y)] , 
         [cov(Y , X) , cov(Y , Y)] ]
        """

        isNumpyArray = ((type(x) == numpy.ndarray) or (type(y) == numpy.ndarray))

        covarianceXY = cls.covariance(x,y)

        result = [[cls.covariance(x,x) , covarianceXY] , [covarianceXY , cls.covariance(y,y)]]

        if(isNumpyArray):
            return numpy.array(result)
        else:
            return result


    # function to reshape a matrix into m by n size with the extra spaces begin filled with the placeholder
    @classmethod
    def reshapeMatrix(cls , matrix , m , n , placeholder = 0):

        resultMat = []
        lenMatrix = len(matrix)

        for i in range(m):
            tempList = []

            if(i < lenMatrix):
                lenI = len(matrix[i])

                for j in range(n):
                    
                    if(j < lenI):
                        tempList.append(matrix[i][j])
                    else:
                        tempList.append(placeholder)

            else:
                tempList = [placeholder for _ in range(n)]

            resultMat.append(tempList)

        isNumpyArray = type(matrix) == numpy.ndarray

        if(isNumpyArray):
            return numpy.array(resultMat)
        else:
            return resultMat



    # function to add two matrixes
    @classmethod
    def addTwoMatrix(cls , x , y):

        resultMat = []

        lenX = len(x)
        lenY = len(y)
        
        m = max(lenX , lenY)

        n = 0

        for i in x:
            lenI = len(i)
            if(lenI > n):
                n = lenI

        for i in y:
            lenI = len(i)
            if(lenI > n):
                n = lenI

        x = cls.reshapeMatrix(x , m , n)
        y = cls.reshapeMatrix(y , m , n)

        resultMat = []

        for i,j in zip(x,y):
            tempList = []
            for k,l in zip(i,j):
                tempList.append(k + l)
            resultMat.append(tempList)

        isNumpyArray = ((type(x) == numpy.ndarray) or (type(y) == numpy.ndarray))

        if(isNumpyArray):
            return numpy.array(resultMat)
        else:
            return resultMat


    # function to sub two matrixes
    # x - y
    @classmethod
    def subtractTwoMatrix(cls , x , y):

        resultMat = []

        lenX = len(x)
        lenY = len(y)
        
        m = max(lenX , lenY)

        n = 0

        for i in x:
            lenI = len(i)
            if(lenI > n):
                n = lenI

        for i in y:
            lenI = len(i)
            if(lenI > n):
                n = lenI

        x = cls.reshapeMatrix(x , m , n)
        y = cls.reshapeMatrix(y , m , n)

        resultMat = []

        for i,j in zip(x,y):
            tempList = []
            for k,l in zip(i,j):
                tempList.append(k - l)
            resultMat.append(tempList)

        isNumpyArray = ((type(x) == numpy.ndarray) or (type(y) == numpy.ndarray))

        if(isNumpyArray):
            return numpy.array(resultMat)
        else:
            return resultMat



    # function to multiply two matrixes
    @classmethod
    def multiplyTwoMatrix(cls , x , y):

        # if the matrix is of numpy array type
        isNumpyArray = ((type(x) == numpy.ndarray) or (type(y) == numpy.ndarray))

        # use numpy mean method to find the mean of a numpy array type matrix
        if(isNumpyArray):
            return numpy.dot(x,y)

        y = cls.transpose(y)

        m = len(x)
        n = len(y)

        result = []

        for i in range(m):
            tempList = []
            for j in range(n):
                submission = 0

                for k,l in zip(x[i] , y[j]):
                    submission = submission + (k*l)

                tempList.append(submission)

            result.append(tempList)

        return result


                



        



        



if __name__ == "__main__":

    matrix1 = [[1,4,2,3] , [0,1,4,4] , [-1,0,1,0] , [2,0,4,1]]
    matrix1 = [[39236, 66782, 62717, 67851], [94943, 60210, 33571, 64054], [54493, 90443, 16758, 30514], [75354, 37653, 45644, 94705]]
    matrix2 = [[1,2,3] , [4,7,8] , [145,14,5]]
    matrix3 = [[1,-1,2] , [4,0,6] , [0,1,-1]]
    matrix4 = [[1,-1] , [4,0] , [0,1]]
    matrix5 = [[3,0,2] , [2,0,-2] , [0,1,1]]

    array1 = numpy.array([[85302., 48074., 69284., 89482., 49353.],
       [31905., 32238., 36901., 98817., 94439.],
       [66635., 25787., 70228., 46234., 60768.],
       [42672., 74636., 16335., 49230., 42135.],
       [19544., 90848., 82063., 31646., 93367.]])
    array2 = numpy.array(matrix2)
    array3 = numpy.array(matrix3)
    array4 = numpy.array(matrix4)
    array5 = numpy.array(matrix5)


    # print(MatOperations.determinant(matrix1))
    # print('{0:.20f}'.format(MatOperations.determinant(array1)))
    # print(round(numpy.linalg.det(array1)))
    # print(MatOperations.determinant(matrix2))
    # print(MatOperations.determinant(matrix1))
    # print(MatOperations.cacheDeterminantMEM)

    # print(MatOperations.cofactorMatrix_adjoint(array3))

    # print(MatOperations.transpose(matrix3))
    # print(MatOperations.transpose(array3))
    # print(MatOperations.transpose(matrix4))
    # print(MatOperations.transpose(array4))

    # print(MatOperations.adjointMatrix(array3))

    # print(MatOperations.inverseMatrix(matrix5))


    # matrixCov1 = [[4,8,13,7] , [4,8,13,7]]
    # matrixCov2 = [[11,4,5,14] , [4,8,13,7]]

    # print(MatOperations.covarianceMatrix(matrixCov1 , matrixCov2))

    # print(numpy.cov(matrixCov1, matrixCov2))







    matrix1 = [[1,4,2,3] , [0,1,4,4] , [-1,0,1,0] , [2,0,4,1]]
    matrix2 = [[1,4,2,3] , [0,1,4,4] , [-1,0,1,0,4]]
    # print(MatOperations.reshapeMatrix(matrix1 , 10 , 10))
    print(MatOperations.addTwoMatrix(matrix1 , matrix2))


    # matrix1 = [[1,2,3] , [4,5,6]]
    # matrix2 = [[7,8] , [9,10] , [11,12]]
    # print(MatOperations.multiplyTwoMatrix(matrix1  , matrix2))

