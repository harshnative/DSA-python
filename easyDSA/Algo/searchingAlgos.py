class SearchingAlgo:

    # method to implement the binary search (iterative method)
    # this function return the index number at which the element is found
    # returns None if the element is not found
    @classmethod
    def binarySearch(cls , iterator , elementToSearch):

        # init low , high acc to index so low is 0 and high is len - 1
        low = 0
        lenIterator = len(iterator) - 1
        high = lenIterator

        while(low <= high):

            # if the element is at low then simply return the low as its index number is low
            if(iterator[low] == elementToSearch):
                return low
        
            # if the element is at high then simply return the high as its the element index
            if(iterator[high] == elementToSearch):
                return high
            
            # mid will be low + as we need to find the mid element od rest array and adding low to actual mid will help in that
            mid = low + ((high - low)//2)


            # if the element is found at mid then return mid
            if(iterator[mid] == elementToSearch):
                return mid
            
            # else if the element is in lower array then change the high
            if(iterator[mid] > elementToSearch):
                high = mid - 1

            # else if the element is in upper array then change the low
            elif(iterator[mid] < elementToSearch):
                low = mid + 1
            
        # if element is not found then return None
        return None

    
    # method to implement the binary search in recursion method
    # this function return the index number at which the element is found
    # returns None if the element is not found
    @classmethod
    def binarySearch_usingRecursion(cls , iterator , elementToSearch):

        low = 0
        lenIterator = len(iterator) - 1
        high = lenIterator

        # secondary function to handle the recursion
        def main(iterator , low , high , elementToSearch):
            if(low <= high):

                # if the element is at low then simply return the low as its index number is low
                if(iterator[low] == elementToSearch):
                    return low
            
                # if the element is at high then simply return the high as its the element index
                if(iterator[high] == elementToSearch):
                    return high

            
                # mid will be low + as we need to find the mid element od rest array and adding low to actual mid will help in that
                mid = low + ((high - low)//2)

                # if the element is found at mid then return mid
                if(iterator[mid] == elementToSearch):
                    return mid

                # else if the element is in lower array then change the high
                if(iterator[mid] > elementToSearch):
                    high = mid - 1
                    return main(iterator , low , high , elementToSearch)

                # else if the element is in upper array then change the low
                elif(iterator[mid] < elementToSearch):
                    low = mid + 1
                    return main(iterator , low , high , elementToSearch)

            else:
                return None
        
        # return  the result from the second function
        result = main(iterator , low , high , elementToSearch)

        return result




if __name__ == "__main__":
    arr = ['a' , 'b' , 'c' , 'd' , 'e' , 'f']
    print(SearchingAlgo.binarySearch_usingRecursion(arr , 'e'))