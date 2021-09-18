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
import searchingAlgos as SEACA
import sortingAlgos as SORTA



from colored import fg
blueColor = fg('blue')
greenColor = fg('green')
redColor = fg('red')
yellowColor = fg('yellow')
whiteColor = fg('white')



def isSquareMatrixFunctionTest():
    print("\n\n")

    # is square matrix function test
    print(whiteColor + "Testing isSquareMatrix function")

    def isSquareMatrixTest(howMany):

        avgTime = 0
        error = 0
        errorList = []


        for i in range(howMany):
            n = random.randint(1 , 100)

            myList = []

            for i in range(n):
                tempList = []
                for j in range(n):
                    tempList.append(random.random())

                myList.append(tempList)

            start = time.time()
            result = MO.MatOperations.isSquareMatrix(myList)
            end = time.time()

            avgTime = avgTime + (end - start)

            if(result != True):
                error = error + 1

                errorList.append(myList)

        avgTime = avgTime / howMany

        return error , errorList , avgTime


    error , errorList , avgTime = isSquareMatrixTest(100)

    if(error == 0):
        print(blueColor + "avg time taken by isSquareMatrixTest function per matrix = {}".format(avgTime))
        print(greenColor + "square matrix test passed")
    else:
        print(redColor + "square matrix test failed")
        print(redColor + "error = {} / {}".format(error , 100))
        print(redColor + "error list = {}".format(errorList))
        






def determinantFunctionTest():

    print("\n\n")

    # testing determinant function 
    print(whiteColor + "Testing determinant function")



    def determinantTest(howMany):

        
        # external determinant code
        def getcofactor(m, i, j):
            return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]


        def determinantOfMatrix(mat):

            if(len(mat) == 2):
                value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
                return value

            Sum = 0

            for current_column in range(len(mat)):
                sign = (-1) ** (current_column)

                sub_det = determinantOfMatrix(getcofactor(mat, 0, current_column))

                Sum += (sign * mat[0][current_column] * sub_det)
            return Sum

        avgTime = 0
        error = 0
        errorList = []



        for k in range(howMany):

            n = random.randint(2 , 5)

            myList = []

            for i in range(n):
                tempList = []
                for j in range(n):
                    tempList.append(random.randint(0 , 100000))

                myList.append(tempList)

            result2 = determinantOfMatrix(myList)

            print(f"\ron {k} / {howMany} , test size = {n}" , end = "")


            start = time.time()
            result1 = MO.MatOperations.determinant(myList)
            end = time.time()


            avgTime = avgTime + (end - start)


            if(result1 != result2):

                error = error + 1

                errorList.append([myList , result1 , result2])

        avgTime = avgTime / howMany

        print()

        return error , errorList , avgTime





    error , errorList , avgTime = determinantTest(1000)

    if(error == 0):
        print(blueColor + "avg time taken by determinant function per matrix = {}".format(avgTime))
        print(greenColor + "determinant function test passed")
    else:
        print(redColor + "determinant function test failed")
        print(redColor + "error = {} / {}".format(error , 1000))
        print(redColor + "error list = {}".format(errorList))
        





















def transposeFuncTest():

    print("\n\n")

    # testing determinant function 
    print(whiteColor + "Testing transpose function")



    def transposeTest(howMany):

        
        # transpose using numpy
        def numpyTranspose(mat):
            return mat.transpose()

        avgTime = 0
        error = 0
        errorList = []


        for k in range(howMany):


            n = random.randint(1 , 100)

            myList = []

            for i in range(n):
                tempList = []
                for j in range(n):
                    tempList.append(random.randint(0 , 100000))

                myList.append(tempList)

            result2 = numpyTranspose(numpy.array(myList))

            print(f"\ron {k} / {howMany} , test size = {n}" , end = "")

            isNumpyArray = bool(random.randint(0,1))

            if(isNumpyArray):
                temp = numpy.array(myList)
                start = time.time()
                result1 = MO.MatOperations.transpose(temp)
                end = time.time()
            else:
                start = time.time()
                result1 = MO.MatOperations.transpose(myList)
                end = time.time()


            avgTime = avgTime + (end - start)


            if(not(numpy.array_equal(result1 , result2))):
                error = error + 1

                errorList.append([myList , result1 , result2])

        avgTime = avgTime / howMany

        print()

        return error , errorList , avgTime





    error , errorList , avgTime = transposeTest(1000)

    if(error == 0):
        print(blueColor + "avg time taken by transpose function per matrix = {}".format(avgTime))
        print(greenColor + "transpose function test passed")
    else:
        print(redColor + "transpose function test failed")
        print(redColor + "error = {} / {}".format(error , 1000))
        print(redColor + "error list = {}".format(errorList))
        



































def meanFunctionTest():
    print("\n\n")

    # testing mean of matrix function 
    print(whiteColor + "Testing mean of matrix function")



    def meanTest(howMany):

        
        # transpose using numpy
        def numpyMean(mat):
            return mat.mean()

        avgTime = 0
        error = 0
        errorList = []


        for k in range(howMany):

            n = random.randint(1 , 100)

            myList = []

            for i in range(n):
                tempList = []
                for j in range(n):
                    tempList.append(random.randint(0 , 100000))

                myList.append(tempList)

            result2 = numpyMean(numpy.array(myList))

            print(f"\ron {k} / {howMany} , test size = {n}" , end = "")

            isNumpyArray = bool(random.randint(0,1))

            if(isNumpyArray):
                temp = numpy.array(myList)
                start = time.time()
                result1 = MO.MatOperations.meanOfMatrix(temp)
                end = time.time()
            else:
                start = time.time()
                result1 = MO.MatOperations.meanOfMatrix(myList)
                end = time.time()


            avgTime = avgTime + (end - start)


            if(result1 != result2):
                error = error + 1

                errorList.append([myList , result1 , result2])

        avgTime = avgTime / howMany

        print()

        return error , errorList , avgTime





    error , errorList , avgTime = meanTest(1000)

    if(error == 0):
        print(blueColor + "avg time taken by meanOfMatrix function per matrix = {}".format(avgTime))
        print(greenColor + "meanOfMatrix function test passed")
    else:
        print(redColor + "meanOfMatrix function test failed")
        print(redColor + "error = {} / {}".format(error , 1000))
        print(redColor + "error list = {}".format(errorList))
        






























def multiplyFunctionTest():
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
        


























def sortingTester():


    # function to test the sorting algo's
    def testSorting(sortingAlgo , minElement = -10000 , maxElement = 10000 , arrSize = 10000 , repeat = 1000 , onlyInt = True):

        print("\n\n")
        print(whiteColor + "Testing {} function".format(sortingAlgo.__name__))

        failedNo = 0
        avgTime = 0

        for count in range(repeat):
            failed = False

            print(f"\ron {count} / {repeat}" , end = "")
            
            arr = []

            # generating a array with random numbers of size arrSize
            for _ in range(arrSize):
                toAppend = 0
                if(onlyInt):
                    toAppend = random.randint(minElement , maxElement)
                else:
                    toAppend = random.uniform(float(minElement) , float(maxElement))

                arr.append(toAppend)
            

            
            # sorting the array using algo 
            begin = time.time() 

            if(SORTA.SortingAlgo.quickSort == sortingAlgo):
                pivot = random.randint(0 , len(arr) - 1)
                sortedArr = sortingAlgo(arr , pivotElement = pivot)
            else:
                sortedArr = sortingAlgo(arr)

            end = time.time() 

            avgTime = avgTime + (end - begin)

            lenSortedArr = len(sortedArr)

            # if the i is found to be greator than i+1 then algo as failed
            for i in range(lenSortedArr-1):
                if(sortedArr[i] <= sortedArr[i+1]):
                    pass
                else:
                    failed = True
            
            # if another smallest number is found then algo as failed as in sorted array the smallest number will be at index 0
            smallest = sortedArr[0]
            for i in sortedArr:
                if(smallest > i):
                    failed = True

            # if the another largest number is found then algo is failed
            largest = sortedArr[-1]
            for i in sortedArr:
                if(largest < i):
                    failed = True
            
            # comparing result to python inbuilt sorter
            if(sorted(arr) != sortedArr):
                failed = True



            # print result
            if(failed):
                failedNo = failedNo + 1

        avgTime  = avgTime / repeat
        print()

        if(failedNo == 0):
            print(blueColor + "avg time taken by {} function per array = {}".format(sortingAlgo.__name__ , avgTime))
            print(greenColor + "{} function test passed".format(sortingAlgo.__name__))
        else:
            print(redColor + "{} function test failed".format(sortingAlgo.__name__))
            print(redColor + "error = {} / {}".format(failedNo , repeat))


    sortingAlgoList = [SORTA.SortingAlgo.insertionSort , SORTA.SortingAlgo.bubbleSort ,SORTA.SortingAlgo.selectionSort , SORTA.SortingAlgo.mergeSort , SORTA.SortingAlgo.quickSort]

    testSorting(SORTA.SortingAlgo.countingSort)

    for i in sortingAlgoList:
        testSorting(i , onlyInt=False)
























def binarySearchIterativeFuncTest():

    print("\n\n")

    # testing binary search iterative function 
    print(whiteColor + "Testing binary search iterative function")



    def binary_search_iterativeTest(howMany):

        
        # transpose using numpy
        def normalLinearSearch(iterator , toSearch):
            for i,j in enumerate(iterator):
                if(j == toSearch):
                    return i
            return None

        avgTime = 0
        error = 0
        errorList = []


        for k in range(howMany):


            n = random.randint(1 , 10000)

            myList = []

            for i in range(n):
                if(i not in myList):
                    myList.append(random.randint(0 , 100000000))

            myList = sorted(myList)

            randomElementFromList = random.choice(myList)

            result2 = normalLinearSearch(myList , randomElementFromList)

            print(f"\ron {k} / {howMany}" , end = "")

            start = time.time()
            result1 = SEACA.SearchingAlgo.binarySearch(myList , randomElementFromList)
            end = time.time()


            avgTime = avgTime + (end - start)


            if(result1 != result2):
                error = error + 1

                errorList.append([myList , randomElementFromList , result1 , result2])

        avgTime = avgTime / howMany

        print()

        return error , errorList , avgTime





    error , errorList , avgTime = binary_search_iterativeTest(1000)

    if(error == 0):
        print(blueColor + "avg binary_search_iterativeTest function per array = {}".format(avgTime))
        print(greenColor + "binary_search_iterativeTest function test passed")
    else:
        print(redColor + "binary_search_iterativeTest function test failed")
        print(redColor + "error = {} / {}".format(error , 1000))
        print(redColor + "error list = {}".format(errorList))
       































def binarySearchRecursiveFuncTest():

    print("\n\n")

    # testing binary search recursive function 
    print(whiteColor + "Testing binary search recursive function")



    def binary_search_recursiveTest(howMany):

        
        # transpose using numpy
        def normalLinearSearch(iterator , toSearch):
            for i,j in enumerate(iterator):
                if(j == toSearch):
                    return i
            return None

        avgTime = 0
        error = 0
        errorList = []


        for k in range(howMany):


            n = random.randint(1 , 10000)

            myList = []

            for i in range(n):
                if(i not in myList):
                    myList.append(random.randint(0 , 100000000))

            myList = sorted(myList)

            randomElementFromList = random.choice(myList)

            result2 = normalLinearSearch(myList , randomElementFromList)

            print(f"\ron {k} / {howMany}" , end = "")

            start = time.time()
            result1 = SEACA.SearchingAlgo.binarySearch_usingRecursion(myList , randomElementFromList)
            end = time.time()


            avgTime = avgTime + (end - start)


            if(result1 != result2):
                error = error + 1

                errorList.append([myList , randomElementFromList , result1 , result2])

        avgTime = avgTime / howMany

        print()

        return error , errorList , avgTime





    error , errorList , avgTime = binary_search_recursiveTest(1000)

    if(error == 0):
        print(blueColor + "avg binary_search_recursiveTest function per array = {}".format(avgTime))
        print(greenColor + "binary_search_recursiveTest function test passed")
    else:
        print(redColor + "binary_search_recursiveTest function test failed")
        print(redColor + "error = {} / {}".format(error , 1000))
        print(redColor + "error list = {}".format(errorList))
       































if __name__ == "__main__":

    testsDict = {
        1 : isSquareMatrixFunctionTest , 
        2 : determinantFunctionTest , 
        3 : transposeFuncTest , 
        4 : meanFunctionTest , 
        5 : multiplyFunctionTest ,
        6 : sortingTester ,
        7 : binarySearchIterativeFuncTest ,
        8 : binarySearchRecursiveFuncTest ,
    }

    print("Select space seperated choices from below or 0 for all")

    for i,j in testsDict.items():
        print("{}: {}".format(i , j.__name__))

    inputted = input("Enter your choices here : ")

    if(inputted.strip() == "0"):
        for i,j in testsDict.items():
            j()
    else:
        inputtedList = [int(i) for i in inputted.split()]
        for i,j in testsDict.items():
            if(i in inputtedList):
                j()
