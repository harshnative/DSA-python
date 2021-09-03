class MatOperations:

    @classmethod
    def isSquareMatrix(cls , matrix):

        n = len(matrix)

        if(n == 0):
            return False

        for i in range(n):
            m = len(matrix[i])

            if(n != m):
                return False

        return True

    # function to find the determinant of a matrix
    @classmethod
    def determinant(cls , matrix):

        lenMatrix = len(matrix)

        if(lenMatrix <= 0):
            raise ValueError("Matrix has no elements , could not determinant of empty matrix")

        if(lenMatrix == 1):
            return matrix[0][0]




if __name__ == "__main__":

    matrix1 = [[1,4,2,3] , [0,1,4,4] , [-1,0,1,0] , [2,0,4,1]]

    print(MatOperations.isSquareMatrix(matrix1))