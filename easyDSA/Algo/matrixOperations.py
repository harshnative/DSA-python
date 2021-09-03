import numpy
import copy
from math import pow
class MatOperations:

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
    def determinant(cls , matrix):

        isNumpyArray = type(matrix) == numpy.ndarray

        n = len(matrix)

        # conforming if it is a square matrix
        result = cls.isSquareMatrix(matrix)

        # if not a square matrix , raise error
        if(result == False):
            raise ValueError("{} is not a square matrix".format(matrix))

        # return just number if the matrix only has 1 element
        if(n == 1):
            return matrix[0][0]

        # return the determinant of 2 by 2 matrix
        if(n == 2):
            determinant2by2 = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
            return determinant2by2

        finalDeterminant = 0

        # calculate the determinant
        # determinant is submission of aij (-1^(j) * determinant of new matrix)
        # here the new matrix is matrix excluding ith row , jth col 
        for i in range(n):
            
            # if the array is numpy type
            if(isNumpyArray):
                newMatrix = matrix

                # excluding the row
                newMatrix = numpy.delete(newMatrix, (0), axis=0)

                # excluding the col
                newMatrix = numpy.delete(newMatrix, (i), axis=1)
            
            # if the array is list type
            else:
                newMatrix = copy.deepcopy(matrix)

                # excluding the row
                newMatrix.pop(0)

                # excluding the col
                [j.pop(i) for j in newMatrix]

            
            finalDeterminant = finalDeterminant + ((matrix[0][i] * cls.determinant(newMatrix)) * int(pow(-1 , i)))


        return finalDeterminant


if __name__ == "__main__":

    matrix1 = [[1,4,2,3] , [0,1,4,4] , [-1,0,1,0] , [2,0,4,1]]
    matrix2 = [[1,2,3] , [4,7,8] , [145,14,5]]

    array = numpy.array(matrix2)

    print(MatOperations.determinant(matrix1))