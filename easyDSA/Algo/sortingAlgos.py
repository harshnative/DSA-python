import random
import time
import os

# main class containing all the algorithms
class SortingAlgo:


    # method to implement the counting sort
    @classmethod
    def countingSort(cls , iterator):

        """
        Algo - 
        1. If no element , quit
        2. find the minimum element in array
        3. find the maximum element in array
        4. find range of array as range = max - min + 1 (as range of 10 - 20 is 11 numbers)
        5. generate a temp array of size range and init every element to 0
        6. similarly generate a output array 

        7. traverse the array and add 1 to pos = array[i] - min in temp array
        8. now traverse the temp array and add element = i + min to output array total of tempArray[i] times
        """

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

    


    # method to implement the insertion sort
    @classmethod
    def insertionSort(cls , iterator):

        """
        Algo -
        1. divide the array into sorted array and unsorted array
        2. slowly traverse the unsorted array , and insert the element into sorted array
        3. increase the sorted array size by 1 each time
        """

        # function to insert a element in sorted array
        def insertIntoSortedArray(end , iteratorPass , element):

            """
            Algo - 
            1. traverse in opposite direction
            2. if the current arr[i] in greator than element then swap those two element 
            """

            # looping in backward direction from end element - index till the array is sorted to 0 with step = -1
            for i in range(end , -1 , -1):

                # if the arr[i] > element then we need to shift arr[i] to i+1 and insert the element at i
                # till the arr[i] <= element
                if(iteratorPass[i] > element):

                    # shift the arr[i] to i + 1
                    # and as at arr[i+1] is element then simple swap i to i+1 
                    iteratorPass[i] , iteratorPass[i+1] = iteratorPass[i+1] , iteratorPass[i]
                else:
                    break
            
        
        # at first only array at index 0 will be sorted to init end = 0 
        end = 0
        lenIterator = len(iterator)
        

        for i in range(1 , lenIterator):

            # element at i will be inserted into 0 to i-1
            insertIntoSortedArray(end , iterator , iterator[i])
            end += 1

        return iterator




    
    # method to implement the bubble sort
    @classmethod
    def bubbleSort(cls , iterator):

        """
        Algo - 
        1. run double loop , first from 0 to len
        2. inner from 0 to len - i as after i all elements are already sorted
        3. swap if arr[j] > arr[j+1]
        4. take a swap var to indicate whether the swapping as occur in inner loop or not, if not break outer loop
        """

        lenIterator = len(iterator)

        # outer loop to run inner loop total of length of iterator times 
        for i in range(lenIterator):

            swap = False

            # running a loop until end of arr is reached
            # we minus i each time as slowly arr at last will be sorted containing only larger element , so no need to go their
            for j in range(lenIterator-i-1):

                # if arr[j] is greator than arr[j+1] the swap both
                if(iterator[j] > iterator[j+1]):
                    iterator[j] , iterator[j+1] = iterator[j+1] , iterator[j]
                    swap = True
            
            # if no swap is done it means arr is already sorted out then simply break
            if(not(swap)):
                break

        return iterator


    

    # maethod to implement the selection sort
    @classmethod
    def selectionSort(cls , iterator):

        """
        Algo - 
        1. take a pos = 0
        2. find the smallest element in arr and swap(arr[i] , arr[pos])
        3. increase pos by 1
        """

        lenIterator = len(iterator)

        # traversing the array
        for i in range(lenIterator):

            # let the smallest element be arr[i] as before i , all elements are sorted
            smallest = iterator[i]

            # position of the smallest element
            pos = i

            # traversing the array from i+1 to end to find the smallest element
            for j in range(i+1 , lenIterator):
                if(iterator[j] < smallest):

                    # if smallest element is found , update smallest and its position 
                    smallest = iterator[j]
                    pos = j

            # swap the element at pos with arr[i] to insert the smallest element
            iterator[i] , iterator[pos] = iterator[pos] , iterator[i]

        return iterator

    


    # method to implement the merge sort algo
    @classmethod
    def mergeSort(cls , iterator):

        # if the length of the iterator <= 1 then it is already sorted
        if(len(iterator) <= 1):
            return iterator

        """
        Algo - 
        1. divide the array into left and right and recursively call on both left and right
        2. merging - 
        i , j , k = 0
        a) if left[i] < right[j] then iterator[k] = left[i] and i++
        b) else iterator[k] = right[j] and j++
        c) k++
        d) repeat above three till (i < len(left)) and (j < len(right))
        e) add rest of elements in both i and j to iterator[k] doing k++
        """
        

        def performMergeSort(iterator):
        
            # exit condition for recursive call
            if(len(iterator) > 1):

                # dividing the array
                midPoint = len(iterator)//2

                left = iterator[:midPoint]
                right = iterator[midPoint:]

                # recursively calling both left and rigth
                performMergeSort(left)
                performMergeSort(right)

                i = j = k = 0

                # comparing the left and right element one by one and adding it to iterator[k]
                while((i < len(left)) and (j < len(right))):
                    if(left[i] < right[j]):
                        iterator[k] = left[i]
                        i = i + 1

                    else:
                        iterator[k] = right[j]
                        j = j + 1

                    k = k + 1 

                # adding rest of elements in left array
                while(i < len(left)):
                    iterator[k] = left[i]
                    i += 1
                    k += 1
                
                # adding rest of elements in right array
                while(j < len(right)):
                    iterator[k] = right[j]
                    j += 1
                    k += 1
                
        # calling the inner function to perform merge sort
        performMergeSort(iterator)
        
        # returning the sorted iterator
        return iterator




    # method to perform quick sort
    # if pivot element is 0 then element at low will be used as pivot
    # if pivot element is 1 then element at high will be used as pivot
    @classmethod
    def quickSort(cls , iterator , pivotElement = 0):
        
        # if the iterator as only 1 element then it is already sorted
        if(len(iterator) <= 1):
            return iterator


        # function to place the pivot at right position so that all the elements on left side of pivot are smaller and on right side are greator          
        def helperHigh(iterator , low , high):

            # taking pivot as last element in iterator
            pivot = iterator[high]

            # as we are taking last element as pivot so we take i as -1 to were array starts
            i = low - 1

            # traversing the array passed
            for j in range(low,high):
                if(iterator[j] <= pivot):
                    i = i + 1
                    iterator[i] , iterator[j] = iterator[j] , iterator[i]

            # placing the pivot
            iterator[i+1] , iterator[high] = iterator[high] , iterator[i+1]
            
            # returning pivot index
            return i+1

        
        # function to place the pivot at right position so that all the elements on left side of pivot are smaller and on right side are greator          
        def helperLow(iterator , low , high):

            i = low+1
            j = high

            # selecting the pivot
            pivot = iterator[low]

            # looping till j becomes greator than i
            while(i<=j):
                # if the A[i] is less than pivot simply increament i until it is not
                while(iterator[i]<pivot and i<high):
                    i = i+1

                # if A[j] is greator than pivot simply decreament j until it is not
                while(iterator[j]>pivot):
                    j = j-1
                
                # if i < j and above condition it not meat , then swap A[i] , A[j]
                if(i<j):
                    iterator[i],iterator[j] = iterator[j],iterator[i]
                    i = i+1
                    j = j-1
                
                # else increament i 
                else:
                    i = i+1

            # in the end swap the pivot at j value to place it at rigth position
            iterator[low] , iterator[j] = iterator[j] , iterator[low]

            return j


        if(pivotElement == 0):
            helperFunction = helperLow
        else:
            helperFunction = helperHigh 

        
        # function to implement in recursion
        def performQuickSort(iterator , low , high):
            if(low < high):

                # dividing the array from pivot
                pi = helperFunction(iterator , low , high)

                # applying quick sort on divided arrays along pivot
                performQuickSort(iterator , low , pi-1)
                performQuickSort(iterator , pi+1 , high)


        performQuickSort(iterator , 0 , len(iterator)-1)
    
        return iterator




























            














if __name__ == "__main__":
    # arr = [5,7,6,9,4,8,1,2,3]
    # print(SortingAlgo.quickSort(arr))
            
            

        
        

        
        

         