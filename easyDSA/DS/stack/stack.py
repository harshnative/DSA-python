import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from linkedList.circularLinkedList import CircularLinkedList
from linkedList.circularLinkedList_listType import CircularLinkedList as CircularLinkedList_listType




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
    def returnObj(self):
        return self.cll




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
    def returnObj(self):
        return self.cll





# class containing some pre build stack opeartion
class StackOperations:

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

        stack.sort(reverse = not(reverse))

        for i in stack:
            stackObj.push(i)


    # method to sort a stack
    @classmethod
    def sortStack_listType(cls , stackObj , listPos_reference = 0 , reverse = False):

        # else it is converted to the list first 
        stack = []

        while(not(stackObj.isEmpty())):
            stack.append(stackObj.pop())

        stack.sort(key = lambda x: x[listPos_reference] ,  reverse = not(reverse))

        for i in stack:
            stackObj.push(i)



    @classmethod
    def getLength(cls , stackObj):
        return stackObj.cll.getListLength()

    
    @classmethod
    def traverse(cls , stackObj , reverse = False , listType = False , nodeSeperator = " -> " , justReturn = False , forNode_start = "[ " , forNode_end = " ]"):
        
        dataArgs_seperator = " , "

        result = ""

        if(reverse):
            last = stackObj.cll.head

            result = result + " ..Bottom.. "
            # till be reach list end
            while((last != None)):

                # adding the node starting string "[ "
                if(forNode_start != None):
                    result = result + forNode_start

                # adding the elements in last.data list seperated with dataArgs_seperator
                if(listType):
                    for i in last.data:
                        result = result + str(i) + dataArgs_seperator

                    # removing the lastly added dataArgs_seperator
                    result = result[:(len(dataArgs_seperator) * -1)]

                else:
                    result = result + str(last.data)
                

                # adding the node end string " ]"
                if(forNode_end != None):
                    result = result + forNode_end

                # adding the node seperator
                result = result + nodeSeperator

                last = last.next

                if(last == stackObj.cll.head):
                    break

            # removing the lastly added nodeSeperator
            result = result[:(len(nodeSeperator) * -1)]
            result = result + " ..Top.. "



        else:
            tempNodeVar = stackObj.cll.getLastNode()
            last = stackObj.cll.getLastNode()

            result = result + " ..Top.. "
            # till be reach list end
            while((last != None)):

                # adding the node starting string "[ "
                if(forNode_start != None):
                    result = result + forNode_start

                # adding the elements in last.data list seperated with dataArgs_seperator
                if(listType):
                    for i in last.data:
                        result = result + str(i) + dataArgs_seperator

                    # removing the lastly added dataArgs_seperator
                    result = result[:(len(dataArgs_seperator) * -1)]

                else:
                    result = result + str(last.data)
                

                # adding the node end string " ]"
                if(forNode_end != None):
                    result = result + forNode_end

                # adding the node seperator
                result = result + nodeSeperator

                last = last.prev

                if(last == tempNodeVar):
                    break

            # removing the lastly added nodeSeperator
            result = result[:(len(nodeSeperator) * -1)]
            result = result + " ..Bottom.. "

        if(justReturn):
            return result
        else:
            print(result)
            return result








        

        

        




    
        








    


if __name__ == "__main__":
    stackObj = StackUsingLinkedList_listType()
    # stackObj = StackUsingLinkedList()

    stackObj.push([1 , 11])
    stackObj.push([2 , 22])
    stackObj.push([33 , 333])
    stackObj.push([4 , 44])



    # stackObj.push(1)
    # stackObj.push(2)
    # stackObj.push(33)
    # stackObj.push(4)




    stackOperations.sortStack(stackObj , reverse=True)
    print("stack length = " , stackOperations.getLength(stackObj))
    stackOperations.traverse(stackObj , listType = True , reverse=False)
    print(stackObj.pop())
    print(stackObj.pop())
    print(stackObj.pop())
    print(stackObj.pop())
    print(stackObj.pop())
