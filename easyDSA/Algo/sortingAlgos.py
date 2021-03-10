import random
import time 


# main class containing all the algorithms
class SortingAlgo:


    # method to implement the counting sort
    @classmethod
    def countingSort(cls , iterator):

        # if their is no element in the iterator then simply return the iterator
        if(len(iterator) == 0):
            return iterator

        lenIterator = len(iterator)

        # finding the largest and smallest number in iterator
        largest = max(iterator)
        smallest = min(iterator)

        # range of the element will be max - min + 1
        rangeIterator = largest - smallest + 1

        # generating a arr for size rangeIterator and init to zero to each element
        tempArr = [0 for _ in range(rangeIterator)]

        # generating arr for output of size of the lenght of iterator
        outputArr = [0 for _ in range(lenIterator)] 

        # adding +1 to pos = iterator[i] - smallest
        # this will make sure that negative numbers are also handled
        for i in range(lenIterator):
            tempArr[iterator[i]-smallest] += 1
        
        
        # now iterating the tempArr
        # i + smallest will be added to output arr, total of tempArr[i] times
        # k is the var to keep track of output arr position
        k = 0

        for i in range(len(tempArr)):
            for _ in range(tempArr[i]):
                outputArr[k] = i + smallest
                k += 1

                if(k > lenIterator):
                    raise Exception("array overflow")

        return outputArr









# function to test the sorting algo's
def testSorting(minElement = -10000 , maxElement = 10000 , arrSize = 10000 , repeat = 10000 , onlyInt = True):
    
    # arrSize should be less than 10
    if(arrSize < 10):
        print("array size cannot be less than 10")
        return

    arr = []

    # generating a array with random number of size arrSize
    for _ in range(arrSize):
        toAppend = 0
        if(onlyInt):
            toAppend = random.randint(minElement , maxElement)
        else:
            toAppend = random.uniform(float(minElement) , float(maxElement))

        arr.append(toAppend)
    
    print("generated array of length = {}\n".format(str(len(arr))))


    
    # sorting the array using algo 
    begin = time.time() 
    sortedArr = SortingAlgo.countingSort(arr)
    end = time.time() 
    print(f"Total runtime of the program is {end - begin}") 

    lenSortedArr = len(sortedArr)

    failed = False

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

    # print result
    if(failed):
        print("\n\ntest failed ..\n")
    else:
        print("\n\ntest pass successfull\n")









if __name__ == "__main__":
    testSorting(arrSize=1000000)
            
            

        
        

        
        

         