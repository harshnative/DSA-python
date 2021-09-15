import numpy
import copy
from math import pow


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

        # if the matrix is of numpy array type
        isNumpyArray = type(matrix) == numpy.ndarray

        result = []
        n = len(matrix)

        for i in range(n):

            tempList = []

            for j in range(len(matrix[i])):

                # if the array is numpy type
                if(isNumpyArray):
                    newMatrix = matrix

                    # excluding the row
                    newMatrix = numpy.delete(newMatrix, (i), axis=0)

                    # excluding the col
                    newMatrix = numpy.delete(newMatrix, (j), axis=1)
                
                # if the array is list type
                else:
                    newMatrix = copy.deepcopy(matrix)

                    # excluding the row
                    newMatrix.pop(i)

                    # excluding the col
                    [k.pop(j) for k in newMatrix]

                # calculating Aij
                Aij = int(pow(-1 , i+j)) * cls.determinant(newMatrix , cache)

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
            for j in range(len(matrix[i])):
                adjointMatrix[i][j] = adjointMatrix[i][j] / determinant

        return adjointMatrix



    @classmethod
    def meanOfMatrix(cls , matrix):

        # if the matrix is of numpy array type
        isNumpyArray = type(matrix) == numpy.ndarray

        if(isNumpyArray):
            return matrix.mean()
        
        submission = 0
        count = 0

        for i in range(len(matrix)):
            for j in range(len(i)):
                submission = submission + matrix[i][j]
                count = count + 1
            
        mean = submission / count

        return mean

        


    @classmethod
    def covariance(cls , x , y):
        submission = 0

        lenX = len(x)

        if(lenX != len(y)):
            raise RuntimeError("x and y are not equal in length where x = {} , y = {}".format(x,y))

        for i in range(lenX):
            submission = submission + ((x))


    
    @classmethod
    def covarianceMatrix(cls , x , y):

        """
        [[cov(X , X) , cov(X , Y)] , 
         [cov(Y , X) , cov(Y , Y)] ]
        """



        

        
def numpyDeterminant(matrix):
    a = numpy.array(matrix) 
    return numpy.linalg.det(a)


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


    print(MatOperations.determinant(matrix1))
    print('{0:.20f}'.format(MatOperations.determinant(array1)))
    print(round(numpy.linalg.det(array1)))
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



