import random

import cProfile
import pstats   
import time
import numpy


import sys
import os

from numpy.core.fromnumeric import transpose
from numpy.core.numeric import array_equal
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import matrixOperations as MO


from colored import fg
blueColor = fg('blue')
greenColor = fg('green')
redColor = fg('red')
yellowColor = fg('yellow')
whiteColor = fg('white')




# # is square matrix function test
# print(whiteColor + "Testing isSquareMatrix function")

# def isSquareMatrixTest(howMany):

#     avgTime = 0
#     error = 0
#     errorList = []


#     for i in range(howMany):
#         n = random.randint(1 , 100)

#         myList = []

#         for i in range(n):
#             tempList = []
#             for j in range(n):
#                 tempList.append(random.random())

#             myList.append(tempList)

#         start = time.time()
#         result = MO.MatOperations.isSquareMatrix(myList)
#         end = time.time()

#         avgTime = avgTime + (end - start)

#         if(result != True):
#             error = error + 1

#             errorList.append(myList)

#     avgTime = avgTime / howMany

#     return error , errorList , avgTime


# error , errorList , avgTime = isSquareMatrixTest(100)

# if(error == 0):
#     print(blueColor + "avg time taken by isSquareMatrixTest function per matrix = {}".format(avgTime))
#     print(greenColor + "square matrix test passed")
# else:
#     print(redColor + "square matrix test failed")
#     print(redColor + "error = {} / {}".format(error , 100))
#     print(redColor + "error list = {}".format(errorList))
    







# print("\n\n")

# # testing determinant function 
# print(whiteColor + "Testing determinant function")



# def determinantTest(howMany):

    
#     # external determinant code
#     def getcofactor(m, i, j):
#         return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]


#     def determinantOfMatrix(mat):

#         if(len(mat) == 2):
#             value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
#             return value

#         Sum = 0

#         for current_column in range(len(mat)):
#             sign = (-1) ** (current_column)

#             sub_det = determinantOfMatrix(getcofactor(mat, 0, current_column))

#             Sum += (sign * mat[0][current_column] * sub_det)
#         return Sum

#     avgTime = 0
#     error = 0
#     errorList = []



#     for k in range(howMany):

#         n = random.randint(2 , 5)

#         myList = []

#         for i in range(n):
#             tempList = []
#             for j in range(n):
#                 tempList.append(random.randint(0 , 100000))

#             myList.append(tempList)

#         result2 = determinantOfMatrix(myList)

#         print(f"\ron {k} / {howMany} , test size = {n}" , end = "")


#         start = time.time()
#         result1 = MO.MatOperations.determinant(myList)
#         end = time.time()


#         avgTime = avgTime + (end - start)


#         if(result1 != result2):

#             error = error + 1

#             errorList.append([myList , result1 , result2])

#     avgTime = avgTime / howMany

#     print()

#     return error , errorList , avgTime





# error , errorList , avgTime = determinantTest(1000)

# if(error == 0):
#     print(blueColor + "avg time taken by isSquareMatrixTest function per matrix = {}".format(avgTime))
#     print(greenColor + "determinant function test passed")
# else:
#     print(redColor + "determinant function test failed")
#     print(redColor + "error = {} / {}".format(error , 1000))
#     print(redColor + "error list = {}".format(errorList))
    























# print("\n\n")

# # testing determinant function 
# print(whiteColor + "Testing transpose function")



# def transposeTest(howMany):

    
#     # transpose using numpy
#     def numpyTranspose(mat):
#         return mat.transpose()

#     avgTime = 0
#     error = 0
#     errorList = []


#     for k in range(howMany):


#         n = random.randint(1 , 100)

#         myList = []

#         for i in range(n):
#             tempList = []
#             for j in range(n):
#                 tempList.append(random.randint(0 , 100000))

#             myList.append(tempList)

#         result2 = numpyTranspose(numpy.array(myList))

#         print(f"\ron {k} / {howMany} , test size = {n}" , end = "")

#         isNumpyArray = bool(random.randint(0,1))

#         if(isNumpyArray):
#             temp = numpy.array(myList)
#             start = time.time()
#             result1 = MO.MatOperations.transpose(temp)
#             end = time.time()
#         else:
#             start = time.time()
#             result1 = MO.MatOperations.transpose(myList)
#             end = time.time()


#         avgTime = avgTime + (end - start)


#         if(not(numpy.array_equal(result1 , result2))):
#             error = error + 1

#             errorList.append([myList , result1 , result2])

#     avgTime = avgTime / howMany

#     print()

#     return error , errorList , avgTime





# error , errorList , avgTime = transposeTest(1000)

# if(error == 0):
#     print(blueColor + "avg time taken by transpose function per matrix = {}".format(avgTime))
#     print(greenColor + "transpose function test passed")
# else:
#     print(redColor + "transpose function test failed")
#     print(redColor + "error = {} / {}".format(error , 1000))
#     print(redColor + "error list = {}".format(errorList))
    

























# print("\n\n")

# # testing mean of matrix function 
# print(whiteColor + "Testing mean of matrix function")



# def meanTest(howMany):

    
#     # transpose using numpy
#     def numpyMean(mat):
#         return mat.mean()

#     avgTime = 0
#     error = 0
#     errorList = []


#     for k in range(howMany):

#         n = random.randint(1 , 100)

#         myList = []

#         for i in range(n):
#             tempList = []
#             for j in range(n):
#                 tempList.append(random.randint(0 , 100000))

#             myList.append(tempList)

#         result2 = numpyMean(numpy.array(myList))

#         print(f"\ron {k} / {howMany} , test size = {n}" , end = "")

#         isNumpyArray = bool(random.randint(0,1))

#         if(isNumpyArray):
#             temp = numpy.array(myList)
#             start = time.time()
#             result1 = MO.MatOperations.meanOfMatrix(temp)
#             end = time.time()
#         else:
#             start = time.time()
#             result1 = MO.MatOperations.meanOfMatrix(myList)
#             end = time.time()


#         avgTime = avgTime + (end - start)


#         if(result1 != result2):
#             error = error + 1

#             errorList.append([myList , result1 , result2])

#     avgTime = avgTime / howMany

#     print()

#     return error , errorList , avgTime





# error , errorList , avgTime = meanTest(1000)

# if(error == 0):
#     print(blueColor + "avg time taken by meanOfMatrix function per matrix = {}".format(avgTime))
#     print(greenColor + "meanOfMatrix function test passed")
# else:
#     print(redColor + "meanOfMatrix function test failed")
#     print(redColor + "error = {} / {}".format(error , 1000))
#     print(redColor + "error list = {}".format(errorList))
    































print("\n\n")

# testing multiplyMatrix function 
print(whiteColor + "Testing multiplyMatrix function")



def multiplyTest(howMany):

    
    # transpose using numpy
    def numpymul(mat1 , mat2):
        return numpy.dot(mat1,mat2)

    avgTime = 0
    error = 0
    errorList = []


    for k in range(howMany):

        n = random.randint(1 , 100)
        m = random.randint(1 , 100)

        myList = []

        for i in range(m):
            tempList = []
            for j in range(n):
                tempList.append(random.randint(0 , 1000))

            myList.append(tempList)

        myList2 = []

        for i in range(n):
            tempList = []
            for j in range(m):
                tempList.append(random.randint(0 , 1000))

            myList2.append(tempList)

        result2 = numpymul(numpy.array(myList) , numpy.array(myList2))

        print(f"\ron {k} / {howMany} , test size = {m} by {n}" , end = "")

        start = time.time()
        result1 = MO.MatOperations.multiplyTwoMatrix(myList , myList2)
        end = time.time()


        avgTime = avgTime + (end - start)


        if(not(numpy.array_equal(result1 , result2))):
            error = error + 1

            errorList.append([myList , result1 , result2])

    avgTime = avgTime / howMany

    print()

    return error , errorList , avgTime





error , errorList , avgTime = multiplyTest(1000)

if(error == 0):
    print(blueColor + "avg time taken by multiplyMatrix function per matrix = {}".format(avgTime))
    print(greenColor + "multiplyMatrix function test passed")
else:
    print(redColor + "multiplyMatrix function test failed")
    print(redColor + "error = {} / {}".format(error , 1000))
    print(redColor + "error list = {}".format(errorList))
    