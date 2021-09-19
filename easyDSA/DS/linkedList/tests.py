import random

import cProfile
import pstats   
import time
import numpy
import copy


import sys
import os

from colored import fg
blueColor = fg('blue')
greenColor = fg('green')
redColor = fg('red')
yellowColor = fg('yellow')
whiteColor = fg('white')


import singlyLinkedList


def singlyLinkedListTest():
    print("\n\n")

    # singlyLinked list test
    print(whiteColor + "Testing singly linked list class")


    def testThing(howMany):

        errorList = []
        error = 0

        for k in range(howMany):
            print(f"\ron {k} / {howMany}" , end = "")

            sll = singlyLinkedList.SinglyLinkedList()

            myList = []

            # generating a list
            for _ in range(1000):
                choice = random.randint(0 , 2)
                toInsert = random.randint(0 , 100)

                if(choice == 0):
                    sll.insertAtEnd(toInsert)
                    myList.append(toInsert)
                elif(choice == 1):
                    sll.insertAtFront(toInsert)
                    myList.insert(0 , toInsert)
                elif(choice == 2):
                    if(len(myList) != 0):
                        pos = random.randint(0 , len(myList)-1)
                        prevNode = sll.getNodeAtPos(pos , raiseError=True)
                        sll.insertAfterNode(prevNode , toInsert)
                        myList.insert(pos+1 , toInsert)
                

            sslList = sll.returnList()
            if(sslList != myList):
                error = error + 1
                errorList.append(["insertion error" , sslList , myList]) 

            # shuffle myList and perform deletion test
            random.shuffle(myList)

            couldNotDelete = []

            for i in myList:
                result = sll.deleteNodeAtKey(i)
                if(result == None):
                    couldNotDelete.append(i)

            if(sll.getListLength() != 0):
                error = error + 1
                errorList.append(["deletion error" , sll.returnList() , couldNotDelete])


            # regenerate the list
            sll = singlyLinkedList.SinglyLinkedList()

            myList = []

            # generating a list
            for _ in range(1000):
                choice = random.randint(0 , 2)
                toInsert = random.randint(0 , 100)

                if(choice == 0):
                    sll.insertAtEnd(toInsert)
                    myList.append(toInsert)
                elif(choice == 1):
                    sll.insertAtFront(toInsert)
                    myList.insert(0 , toInsert)
                elif(choice == 2):
                    if(len(myList) != 0):
                        pos = random.randint(0 , len(myList)-1)
                        prevNode = sll.getNodeAtPos(pos , raiseError=True)
                        sll.insertAfterNode(prevNode , toInsert)
                        myList.insert(pos+1 , toInsert) 


            # remove duplicate elements test

            sll.delDuplicateUnShorted()

            myList = list(set(myList))

            if(sorted(sll.returnList()) != sorted(myList)):
                error = error + 1
                errorList.append(["remove duplicate elements error" , sll.returnList() , myList])


            # is circular test
            if(sll.isCircular()):
                error = error + 1
                errorList.append(["isCircular error" , sll.returnList()])


            

            # generating list again
            # regenerate the list
            sll = singlyLinkedList.SinglyLinkedList()

            myList = []

            # generating a list
            for _ in range(1000):
                choice = random.randint(0 , 2)
                toInsert = random.randint(0 , 100)

                if(choice == 0):
                    sll.insertAtEnd(toInsert)
                    myList.append(toInsert)
                elif(choice == 1):
                    sll.insertAtFront(toInsert)
                    myList.insert(0 , toInsert)
                elif(choice == 2):
                    if(len(myList) != 0):
                        pos = random.randint(0 , len(myList)-1)
                        prevNode = sll.getNodeAtPos(pos , raiseError=True)
                        sll.insertAfterNode(prevNode , toInsert)
                        myList.insert(pos+1 , toInsert)

            # delete element at pos test
            for _ in range(10):
                randomElement = random.choice(myList)

                randomElementPos = myList.index(randomElement)

                sll.deleteNodeAtPos(randomElementPos)
                myList.pop(randomElementPos)

            sslList = sll.returnList()
            if(sslList != myList):
                error = error + 1
                errorList.append(["deletion at pos error" , sslList , myList])


            # get all node at key test
            randomElement = random.choice(myList)
            randomElementCount = myList.count(randomElement)

            nodesAtRandomElement = sll.getAllNodeAtKey(randomElement)

            if(randomElementCount != len(nodesAtRandomElement)):
                error = error + 1
                errorList.append(["get all node at key error" , sll.returnList() , myList , randomElementCount , len(nodesAtRandomElement)])

            
            # reverse list test
            sll.reverseLinkedList()

            sllList = sll.returnList()

            myList.reverse()

            if(myList != sllList):
                error = error + 1
                errorList.append(["reverse list error" , sllList , myList , len(sllList) , len(myList)])




        return error , errorList
    
            


    error , errorList = testThing(100)

    print()

    if(error == 0):
        print(greenColor + "singlyLinkedListTest function test passed")
    else:
        print(redColor + "singlyLinkedListTest function test failed")
        print(redColor + "error = {} / {}".format(error , 1000))
        print(redColor + "error list = {}".format(errorList))



                



if __name__ == "__main__":

    testsDict = {
        1 : singlyLinkedListTest , 
        # 2 : determinantFunctionTest , 
        # 3 : transposeFuncTest , 
        # 4 : meanFunctionTest , 
        # 5 : multiplyFunctionTest ,
        # 6 : sortingTester ,
        # 7 : binarySearchIterativeFuncTest ,
        # 8 : binarySearchRecursiveFuncTest ,
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




