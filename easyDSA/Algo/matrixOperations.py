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
    def determinant(cls , matrix , cache = True):


        # if the result is in cache return it
        if(cache):
            for i in cls.cacheDeterminantMEM:
                if(i[0] == matrix):
                    return i[1]

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

        if(cache):
            cls.cacheDeterminantMEM.append([matrix , finalDeterminant])

        return finalDeterminant



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
        
                


if __name__ == "__main__":

    matrix1 = [[1,4,2,3] , [0,1,4,4] , [-1,0,1,0] , [2,0,4,1]]
    matrix2 = [[1,2,3] , [4,7,8] , [145,14,5]]
    matrix3 = [[1,-1,2] , [4,0,6] , [0,1,-1]]
    matrix4 = [[1,-1] , [4,0] , [0,1]]

    array2 = numpy.array(matrix2)
    array3 = numpy.array(matrix3)
    array4 = numpy.array(matrix4)

    # print(MatOperations.determinant(matrix1))
    # print(MatOperations.determinant(matrix2))
    # print(MatOperations.determinant(matrix1))
    # print(MatOperations.cacheDeterminantMEM)

    print(MatOperations.cofactorMatrix_adjoint(array3))

    # print(MatOperations.transpose(matrix3))
    # print(MatOperations.transpose(array3))
    # print(MatOperations.transpose(matrix4))
    # print(MatOperations.transpose(array4))

    print(MatOperations.adjointMatrix(array3))



