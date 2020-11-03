
# Node class
class Node:

    def __init__(self , *dataArgs , next=None , prev=None):

        # data list
        self.data = list(*dataArgs)

        # prev pointer
        self.prev = prev

        # next pointer 
        self.next = next



# min version of circular class of the easyDSA module to implement stack
class CircularLinkedList:


    def __init__(self):
        self.head = None

        self.lastNodeCache = None


    # function to return the head
    def returnHead(self):
        return self.head


    # function to insert in a empty list
    def insertInEmpty(self , *dataArgs):
        if(self.head != None):
            raise Exception("only insert in empty list")

        newNode = Node(dataArgs)

        self.head = newNode

        # making it pointing to himself
        self.head.next = self.head
        self.head.prev = self.head



    # function to get the last node 
    def getLastNode(self):
        if(self.head == None):
            return None
        return self.head.prev

            
    # function to insert at end
    def insertAtEnd(self , *dataArgs):

        # if the list if initially empty 
        if(self.head == None):
            self.insertInEmpty(*dataArgs)
            return

        lastNode = self.getLastNode()

        newNode = Node(dataArgs)
    
        # new node will point to head
        newNode.next = self.head

        # new node prev will point to lastNode
        newNode.prev = lastNode

        # last node will point to new node
        lastNode.next = newNode

        # head prev will point to new node
        self.head.prev = newNode

    

     # function to delete a node
    def deleteNode(self, node):

        # if the list is empty 
        if(self.head == None):
            return

        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

        if(node == self.head):
            if(nextNode == self.head):
                self.head = None
            else:
                self.head = nextNode

        del node

    def reverseLinkedList(self):

        if (self.head == None): 
            return

        current = self.head
       
        while(current != None):
            nextNode = current.next
            prevNode = current.prev

            current.prev = nextNode
            current.next = prevNode

            current = nextNode

            if(current == self.head):
                break

        temp = self.head

        self.deleteNodeAtPos(1)

        self.insertAtEnd(*temp.data)


    # function to traverse the list
    def getListLength(self):

        last = self.head
        
        length = 0

        # till be reach list end
        while((last != None)):

            last = last.next

            length = length + 1

            if(last == self.head):
                break

        return length

    
    # function to traverse the list
    def traverseList(self , dataArgs_seperator = " , " , nodeSeperator = " -> " , justReturn = False , forNode_start="[ " , forNode_end = " ]"):

        last = self.head
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

            if(last == self.head):
                break

        # removing the lastly added nodeSeperator
        result = result[:(len(nodeSeperator) * -1)]

        if(justReturn):
            return result
        else:
            print(result)
            return result





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
    def push(self , *data):
        self.cll.insertAtEnd(*data)


    # function to remove the last element
    def pop(self):
        toReturn = self.cll.getLastNode()

        # if the stack is empty then return None
        if(toReturn == None):
            return None

        self.cll.deleteNode(self.cll.getLastNode())

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

        stack = []

        # getting stack elements
        while(not(stackObj.isEmpty())):
            stack.append(stackObj.pop())
        
        # adding them back
        for i in stack:
            stackObj.push(*i)


    # method of reversing the stack using no extra space
    # stack must be implemented using doubly circular linked list
    @classmethod
    def reverseStack_onlyForCDLL(cls , cdllObj):
        cdllObj.reverseLinkedList()

    # method to sort a stack
    @classmethod
    def sortStack(cls , stackObj , listPos_reference = 0 , reverse = False):

        # else it is converted to the list first 
        stack = []

        while(not(stackObj.isEmpty())):
            stack.append(stackObj.pop())

        stack.sort(key = lambda x: x[listPos_reference] ,  reverse = not(reverse))

        for i in stack:
            stackObj.push(*i)

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
    stackObj = StackUsingLinkedList()

    stackObj.push(1)
    # stackObj.push(2)
    # stackObj.push(33)
    # stackObj.push(4)
    print(stackOperations.getLength(stackObj))
    print(stackOperations.quickTraverse(stackObj=stackObj , asAdded=False))
    print(stackObj.pop())
    print(stackObj.pop())
    print(stackObj.pop())
    print(stackObj.pop())
    print(stackObj.pop())
