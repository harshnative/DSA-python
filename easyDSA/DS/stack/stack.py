import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from linkedList.circularLinkedList import CircularLinkedList
from linkedList.circularLinkedList_listType import CircularLinkedList as CircularLinkedList_listType


# list implementation of stack
class StackUsingArray:
    
    def __init__(self):
        self.stack = []

    # function to push a data into stack
    def push(self , *data):
        self.stack.append(list(data))

    # function to pop a data into stack
    def pop(self , raiseError = False):
        try:
            return self.stack.pop()
        except IndexError:
            if(raiseError):
                raise RuntimeError("stack is empty , cannot pop")
            else:
                return None

    # function to return the data of last element
    def peek(self):
        try:
            return self.stack[-1]
        except IndexError:
            return None

    # function check if the stack is empty or not 
    def isEmpty(self):

        # if the stack is not empty then pop does not raise exception
        try:
            temp = self.stack.pop()
            self.stack.append(temp)
            return False
        except IndexError:
            return True 

    # function to get the entire stack
    def returnList(self):
        return self.stack




# circular linked list implementation of stack
# circular doubly linked list is chosen because insertion and deletion is O(1)
class StackUsingLinkedList:
    
    def __init__(self):
        self.cll = CircularLinkedList()

    # every new element will be inserted at end of linked list
    def push(self , data):
        self.cll.insertAtEnd(data)


    # function to remove the last element
    def pop(self , returnNone = True):
        toReturn = self.cll.getLastNode()

        # if the stack is empty then return None
        if(toReturn == None):
            if(returnNone):
                return None
            else:
                raise RuntimeError("pop on empty stack")

        self.cll.deleteNode(toReturn)

        # else return data
        return toReturn.data

    # function to return data of the last element
    def peek(self , returnNone = True):
        toReturn = self.cll.getLastNode()

        # if the stack is empty then return None
        if(toReturn == None):
            if(returnNone):
                return None
            else:
                raise RuntimeError("pop on empty stack")

        # else return data
        return toReturn.data

    # function to check if the stack is empty or not
    def isEmpty(self):
        toReturn = self.cll.getLastNode()

        # if the last node is None then the stack is empty
        if(toReturn == None):
            return True
        else:
            return False

    # function to return the head so that more operations can be performed
    def returnHead(self):
        return self.cll.returnHead()




# circular linked list implementation of stack
# circular doubly linked list is chosen because insertion and deletion is O(1)
# this version of the stack is used for having a python list as a single stack element
class StackUsingLinkedList_listType:
    
    def __init__(self):
        self.cll = CircularLinkedList_listType()

    # every new element will be inserted at end of linked list
    def push(self , data):
        self.cll.insertAtEnd(data)


    # function to remove the last element
    def pop(self , returnNone = True):
        toReturn = self.cll.getLastNode()

        # if the stack is empty then return None
        if(toReturn == None):
            if(returnNone):
                return None
            else:
                raise RuntimeError("pop on empty stack")

        self.cll.deleteNode(toReturn)

        # else return data
        return toReturn.data

    # function to return data of the last element
    def peek(self , returnNone = True):
        toReturn = self.cll.getLastNode()

        # if the stack is empty then return None
        if(toReturn == None):
            if(returnNone):
                return None
            else:
                raise RuntimeError("pop on empty stack")

        # else return data
        return toReturn.data

    # function to check if the stack is empty or not
    def isEmpty(self):
        toReturn = self.cll.getLastNode()

        # if the last node is None then the stack is empty
        if(toReturn == None):
            return True
        else:
            return False

    # function to return the head so that more operations can be performed
    def returnHead(self):
        return self.cll.returnHead()





# class containing some pre build stack opeartion
class stackOperations:

    # method for reversing a stack
    # accepts stack obj generated by above two classes
    @classmethod
    def reverseStack(cls , stackObj):
        stackObj.cll.reverseLinkedList()
        

    # method to sort a stack
    @classmethod
    def sortStack(cls , stackObj , reverse = False):

        # else it is converted to the list first 
        stack = []

        while(not(stackObj.isEmpty())):
            stack.append(stackObj.pop())

        stack.sort(reverse = reverse)

        for i in stack:
            stackObj.push(i)


    # method to sort a stack
    @classmethod
    def sortStack_listType(cls , stackObj , listPos_reference = 0 , reverse = False):

        # else it is converted to the list first 
        stack = []

        while(not(stackObj.isEmpty())):
            stack.append(stackObj.pop())

        stack.sort(key = lambda x: x[listPos_reference] ,  reverse = reverse)

        for i in stack:
            stackObj.push(i)



    @classmethod
    def getLength(cls , stackObj):

        # if the stack is pre in simple list form
        if(type(stackObj) == type(StackUsingArray())):
            return len(stackObj.returnList())

        else:
            last = stackObj.returnHead()
        
            length = 0

            # till be reach list end
            while((last != None)):

                last = last.next

                length = length + 1

                if(last == stackObj.returnHead()):
                    break

            return length

    
    @classmethod
    def traverse(cls , stackObj , asAdded = False ,  dataArgs_seperator = " , " , nodeSeperator = " -> " , justReturn = False , forNode_start="[ " , forNode_end = " ]" , noPop = False):

        stack = []

        # getting stack elements
        while(not(stackObj.isEmpty())):
            stack.append(stackObj.pop())
        
        result = ""
        tempStack = []

        # elements will be added back if noPop is required
        if(noPop):
            
            # as while added back the stack will get reversed so we are pre reversing to null the upcomming effect
            tempStack = stack[::-1]

            for i in tempStack:
                stackObj.push(*i)

        # if the priting as to be done in the same direction in which the stack elements were added
        # then we need to reverse the stack
        if(asAdded and noPop):
            stack = tempStack

        elif(asAdded):
            stack = stack[::-1]

        # adding the result
        for i in stack:

            result = result + forNode_start
            
            for j in i:
                result = result + str(j) + dataArgs_seperator

            result = result[:len(dataArgs_seperator) * -1]

            result = result + forNode_end

            result = result + nodeSeperator

        result = result[:len(nodeSeperator) * -1]

        if(justReturn):
            return result
        else:
            print(result)
            return result

    

    @classmethod
    def quickTraverse(cls , stackObj , asAdded = False ,  dataArgs_seperator = " , " , nodeSeperator = " -> " , justReturn = False , forNode_start="[ " , forNode_end = " ]"):

        # if the stack is pre in simple list form
        if(type(stackObj) == type(StackUsingArray())):
            stack = stackObj.returnList()
        
            result = ""

            # if not as added then we need to print in reverse
            if(not(asAdded)):

                # adding the result
                for i in stack[::-1]:

                    result = result + forNode_start
                    
                    for j in i:
                        result = result + str(j) + dataArgs_seperator

                    result = result[:len(dataArgs_seperator) * -1]

                    result = result + forNode_end

                    result = result + nodeSeperator

                result = result[:len(nodeSeperator) * -1]

            # else simply print
            else:

                # adding the result
                for i in stack:

                    result = result + forNode_start
                    
                    for j in i:
                        result = result + str(j) + dataArgs_seperator

                    result = result[:len(dataArgs_seperator) * -1]

                    result = result + forNode_end

                    result = result + nodeSeperator

                result = result[:len(nodeSeperator) * -1]

            if(justReturn):
                return result
            else:
                print(result)
                return result

        # else if the stack was in circular linked list form
        else:

            # if not as added then we need to print in reverse
            if(not(asAdded)):

                # traversing doubly cicular linked list in reverse direction
                last = stackObj.returnHead().prev
                result = ""

                
                # till be reach list end
                while((last != None)):

                    # adding the node starting string "[ "
                    if(forNode_start != None):
                        result = result + forNode_start

                    # adding the elements in last.data list seperated with dataArgs_seperator
                    for i in last.data:
                        result = result + str(i) + dataArgs_seperator

                    # removing the lastly added dataArgs_seperator
                    result = result[:(len(dataArgs_seperator) * -1)]

                    # adding the node end string " ]"
                    if(forNode_end != None):
                        result = result + forNode_end

                    # adding the node seperator
                    result = result + nodeSeperator

                    last = last.prev

                    # if we reach the last node
                    if(last == stackObj.returnHead().prev):
                        break

                # removing the lastly added nodeSeperator
                result = result[:(len(nodeSeperator) * -1)]

                if(justReturn):
                    return result
                else:
                    print(result)
                    return result

            # else simply traversing the linked list
            else:
                last = stackObj.returnHead()
                result = ""
                
                # till be reach list end
                while((last != None)):

                    # adding the node starting string "[ "
                    if(forNode_start != None):
                        result = result + forNode_start

                    # adding the elements in last.data list seperated with dataArgs_seperator
                    for i in last.data:
                        result = result + str(i) + dataArgs_seperator

                    # removing the lastly added dataArgs_seperator
                    result = result[:(len(dataArgs_seperator) * -1)]

                    # adding the node end string " ]"
                    if(forNode_end != None):
                        result = result + forNode_end

                    # adding the node seperator
                    result = result + nodeSeperator

                    last = last.next

                    if(last == stackObj.returnHead()):
                        break

                # removing the lastly added nodeSeperator
                result = result[:(len(nodeSeperator) * -1)]

                if(justReturn):
                    return result
                else:
                    print(result)
                    return result







        

        

        




    
        








    


if __name__ == "__main__":
    stackObj = StackUsingLinkedList_listType()
    # stackObj = StackUsingLinkedList()

    stackObj.push([1])
    stackObj.push([2])
    stackObj.push([33])
    stackObj.push([4])



    # stackObj.push(1)
    # stackObj.push(2)
    # stackObj.push(33)
    # stackObj.push(4)




    stackOperations.sortStack_listType(stackObj)

    print(stackObj.pop())
    print(stackObj.pop())
    print(stackObj.pop())
    print(stackObj.pop())
    print(stackObj.pop())
