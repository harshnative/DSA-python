import random

import cProfile
import pstats   
import time


import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import matrixOperations as MO


from colored import fg
blueColor = fg('blue')
greenColor = fg('green')
redColor = fg('red')
yellowColor = fg('yellow')




# is square matrix function test
print("Testing is isSquareMatrix function")

def isSquareMatrixTest(howMany):
    for i in range(howMany):

        error = 0
        errorList = []

        n = random.randint(1 , 100)

        myList = []

        for i in range(n):
            tempList = []
            for j in range(n):
                tempList.append(random.random())

            myList.append(tempList)

        result = MO.MatOperations.isSquareMatrix(myList)

        if(result != True):
            error = error + 1

            errorList.append(myList)

    return error , errorList


start = time.time()
error , errorList = isSquareMatrixTest(100)
end = time.time()

if(error == 0):
    print(blueColor + "avg time taken by isSquareMatrixTest function per matrix = {}".format((end - start)/100))
    print(greenColor + "square matrix test passed")
else:
    print(redColor + "square matrix test failed")
    print(redColor + "error = {} / {}".format(error , 100))
    print(redColor + "error list = {}".format(errorList))
    

        