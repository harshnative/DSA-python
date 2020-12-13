
# Node class
class Node:

    def __init__(self , data , next=None , prev=None):

        temp = []
        if(type(data) != type(temp)):
            raise RuntimeError("list argument is excepted as data")

        # data list
        self.data = list(data)

        # prev pointer
        self.prev = prev

        # next pointer 
        self.next = next


    

# main class of module
class DoublyLinkedList:


    def __init__(self):
        self.head = None

        self.lastNodeCache = None


    # function to return the head
    def returnHead(self):
        return self.head

    
    # set custom head to perform operations
    def setCustomHead(self , head , deletePrevList=True):
        if(deletePrevList):
            self.deleteEntireList()

        self.head = head


    
    # function to insert at front
    def insertAtFront(self, data):

        """algo - 
        1. insert the data , make the newNode.next = self.head
        2. newNode.prev = None
        3. if the head is not none then head.prev = newNode
        4. make the new Node as head"""

        newNode = Node(data)

        newNode.next = self.head
        newNode.prev = None

        if(self.head != None):
            self.head.prev = newNode

        self.head = newNode


    # function to insert a node after a node
    def insertAfterNode(self , prevNode , data):

        """Algo - 
        1. make new node
        2. newNode.next = prevNode.next
        3. prevNode.next = newNode
        4. newNode.prev = prevNode
        5. if the newNode.next is not None then prev of newNode.next is newNode"""

        if(prevNode == None):
            raise Exception("prevNode cannot be None")

        
        newNode = Node(data)

        newNode.next = prevNode.next
        prevNode.next = newNode

        newNode.prev = prevNode

        if(newNode.next != None):
            newNode.next.prev = newNode

        self.lastNodeCache = None


    def getLastNode(self, useCache = True):

        # using the cache
        if(useCache and (self.lastNodeCache != None)):
            try:
                dataIsPresent = self.lastNodeCache.data
                return self.lastNodeCache
            except AttributeError:
                pass
                
        
        last = self.head

        if(last == None):
            return None


        # getting the last node
        while(last.next != None):

            if(last.next == self.head):
                break

            last = last.next

        self.lastNodeCache = last

        return last

            



    # function to insert at end
    def insertAtEnd(self , data , useCache = True):

        """algo - 
        1. get the last node
        2. if the last node is none the insert at front
        3. insert the node after prev node = lastNode
        """

        lastNode = self.getLastNode(useCache)

        if(lastNode == None):
            self.insertAtFront(data)

        else:
            prevNode = lastNode
            newNode = Node(data)

            newNode.next = prevNode.next
            prevNode.next = newNode

            newNode.prev = prevNode

            self.lastNodeCache = newNode

    
    # function to insert a node before a node
    def insertBeforeNode(self , node , data):

        prevNode = node.prev

        if(prevNode == None):
            if(node != self.head):
                raise Exception("node.prev is none but node is not head")
            else:
                self.insertAtFront(data)
            
        else:
            self.insertAfterNode(prevNode , data)

    

    # function to traverse the list
    def traverseList(self , dataArgs_seperator = " , " , nodeSeperator = " -> " , justReturn = False , forNode_start="[ " , forNode_end = " ]"):

        last = self.head
        result = ""

        # till be reach list end
        while(last != None):

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

            # just to avoid infinite loop
            if(last == self.head):
                break

        # removing the lastly added nodeSeperator
        result = result[:(len(nodeSeperator) * -1)]

        if(justReturn):
            return result
        else:
            print(result)
            return result


    
    # function to return a node at pos
    # raiseError if the pos is not found else return None
    def getNodeAtPos(self, pos , raiseError = False):

        if(pos < 1):
            raise Exception("position cannot be less than 1")

        last = self.head
        found = False

        # traversing the list till be get a None node
        while(last != None):

            # if pos is found - break
            if(pos == 1):
                found = True
                break

            last = last.next

            pos -= 1

        if(not(found) and raiseError):
            raise RuntimeError("position could not be found")
        elif(not(found)):
            return None
            
        return last



    # function to delete a node
    def deleteNode(self , nodeToBeDeleted):

        if(self.head == None):
            raise Exception("list is empty")
    
        if(nodeToBeDeleted == None):
            raise Exception("node to be deleted cannot be None")
        
        # checking if the node to be deleted is head
        if(nodeToBeDeleted == self.head):
            self.head = nodeToBeDeleted.next
            self.head.prev = None
            return
        
        # checking if the node is last node
        if(nodeToBeDeleted.next == None):
            prevNode = nodeToBeDeleted.prev
            prevNode.next = None
            del nodeToBeDeleted
            return

        # else
        # prevNode.next = nextNode
        # nextNode.prev = prevNode
        nextNode = nodeToBeDeleted.next
        prevNode = nodeToBeDeleted.prev

        prevNode.next = nextNode
        nextNode.prev = prevNode

        del nodeToBeDeleted

    
    # function to delete node at pos
    def deleteNodeAtPos(self, pos):
        node = self.getNodeAtPos(pos , True)
        
        self.deleteNode(node)


     # function to reverse a linked list
    def reverseLinkedList(self):
        current = self.head
        prevNode = None
        
        while(current != None):

            # storing prev
            prevNode = current.prev

            # reversing the direction
            current.prev = current.next
            current.next = prevNode

            # moving to next element
            current = current.prev

            # just to avoid infinite loop
            if(current == self.head):
                break

        if(prevNode != None):
            self.head = prevNode.prev


    # function to return the list
    # from node and to node are also included
    def returnList(self , fromNode = 0 , toNode = "till end"):

        last = self.head

        # pos to keep track where we are in linked list
        pos = 0

        if(toNode == "till end"):
            toNode = None

        resultList = []

        # to check if we are in the range provided
        start = False

        # till be reach list end
        while(last != None):

            # if the pos becomes the from node then start will be become true , so the from node is also added
            if(pos == fromNode):
                start = True

            # adding data
            if(start):
                tempList = []

                for i in last.data:
                    tempList.append(i)

                resultList.append(tempList)
            
            # if the pos becomes the toNode Value else list will tarverse till last
            if((pos == toNode) and (toNode != None)):
                break

            last = last.next
            pos += 1

            # just to avoid infinite loop
            if(last == self.head):
                break

        return resultList


    # function to traverse the list and get its length
    def getListLength(self):

        last = self.head
        length = 0

        # till be reach list end
        while(last != None):

            length += 1
            last = last.next

            # just to avoid infinite loop
            if(last == self.head):
                break

        return length


    
    # method to delete the entire linked list
    # data and reference both are deleted
    def deleteEntireList(self):

        last = self.head

        while(last != None):

            nextNode = last.next

            del last.data
            del last.next
            del last.prev

            last = nextNode

        self.head = None

    
    # function to sort the linked list
    def sortLinkedList(self , listPos_reference = 0 , reverse = False):

        # conv the linked list to python normal list
        dataList = self.returnList()

        # sorting list
        dataList.sort(key = lambda x: x[listPos_reference])

        self.deleteEntireList()

        # making new sorted linked list
        for i in dataList:
            if(reverse):
                self.insertAtFront(i)
            else:
                self.insertAtEnd(i)


    # function to delete a node by matching the key - deletes the first occurence
    # if the keylist is passed then it will matched against the data list
    # if the key is passed then if the data list contains that key is checked 
    # if the startform is passed then traversing will start from their
    def deleteNodeAtKey(self , keyList = None , key = None , startForm = None):

        # for tracking wheather to delete a node or not
        delete = False

        # for traversing the list 
        last = self.head

        # if the start form is passed
        if(startForm != None):
            last = startForm


        # till be reach list end
        while(last != None):
            
            # if the key list is none then we check for the element in the data list
            if(keyList == None):
                
                # if the elment is found the we need to delete this node
                for i in last.data:
                    if(i == key):
                        delete = True
            
            # if the key list is passed then we have to match it to the list
            else:
                if(last.data == keyList):
                    delete = True

            # if the node is set to be deleted
            if(delete):
                if(last.next != None):
                    temp = last.next
                    self.deleteNode(last)
                    return temp
                else:
                    self.deleteNode(last)
                    return None

            
            last = last.next

            # just to avoid infinite loop
            if(last == self.head):
                break

        return None


    # function to delete all node containing the key
    # if the keylist is passed then it will matched against the data list
    # if the key is passed then if the data list contains that key is checked 
    def deleteAllNodeAtKey(self , keyList = None , key = None):

        status = True

        # till node will be none when we are just starting
        tillNode = None

        while(status):

            # node and prev node will be returned by the function 
            # if the none is returned that means no other key is left to delete
            tillNode = self.deleteNodeAtKey(keyList , key , tillNode)

            # break the loop when the till node is none
            if(tillNode == None):
                status = False


    def getNodeAtKey(self , keyList = None , key = None , startForm = None , allNode = True):

        # for tracking wheather to delete a node or not
        delete = False

        nodeList = []

        # for traversing the list 
        last = self.head

        # if the start form is passed
        if(startForm != None):
            last = startForm


        # till be reach list end
        while(last != None):
            
            # if the key list is none then we check for the element in the data list
            if(keyList == None):
                
                # if the elment is found the we need to delete this node
                for i in last.data:
                    if(i == key):
                        delete = True
            
            # if the key list is passed then we have to match it to the list
            else:
                if(last.data == keyList):
                    delete = True

            # if the node is set to be deleted
            if(delete):
                delete = False
                if(allNode):
                    nodeList.append(last)
                else:
                    return last

            
            last = last.next

            # just to avoid infinite loop
            if(last == self.head):
                break

        return nodeList



    # function to find out if the linked list
    def isCircular(self):

        # for traversing the list 
        last = self.head

        # till be reach list end
        while(last != None):
            
            last = last.next

            # just to avoid infinite loop
            if(last == self.head):
                return True

        return False


    # function to find out if the linked list
    def detectLoop(self):

        # for traversing the list 
        last = self.head

        # till be reach list end
        while(last != None):

            thisNode = last
            tempLen = 0

            # traversing the list till the end or the last is reached
            while(thisNode != None):

                thisNode = thisNode.next
                tempLen += 1

                if(thisNode  == last):
                    return tempLen
            
            last = last.next

        return False

    
    # function to delete all the duplicate elements in sorted list
    def delDuplicateShorted(self , entireData = True , specificPosInData = None):

        last = self.head

        # need to check as while loop starts form last.next
        if(last == None):
            return

        while(last.next != None):

            # if the data matches we delete the next node
            if(last.next.data == last.data):
                if(entireData):
                    self.deleteNodeAtKey(last.data , startForm=last.next)
                else:
                    self.deleteNodeAtKey(key=last.data[specificPosInData] , startForm=last.next)
            else:
                last = last.next


    # function to delete all the duplicate elements in unsorted list
    def delDuplicateUnShorted(self , entireData = True , specificPosInData = None):

        last = self.head

        # need to check as while loop starts form last.next
        if(last == None):
            return

        while(last.next != None):

            temp = last

            # second loop for checking the next elements in list with the last element
            while(temp.next != None):
                
                # if the data matches we delete the next node
                if(temp.next.data == last.data):
                    if(entireData):
                        self.deleteNodeAtKey(last.data , startForm=last.next)
                    else:
                        try:
                            self.deleteNodeAtKey(key=last.data[specificPosInData] , startForm=last.next)
                        except IndexError:
                            raise IndexError("list index out of range - keep in mind : position is considered like index here , starting form zero")
                else:
                    temp = temp.next

            last = last.next










def test():
    dll = DoublyLinkedList()
    dll.insertAtEnd([1 , 'a' ], useCache= True)
    dll.insertAtEnd([2 , 'b' ], useCache= True)
    dll.insertAtEnd([3 , 'c' ], useCache= True)
    dll.insertAtEnd([4 , 'd' ], useCache= True)
    dll.insertAtFront([5 , 'e'])
    dll.insertAtFront([6 , 'e'])
    dll.insertAfterNode(dll.getNodeAtPos(3) , ["hello" , 'e'])
    dll.insertBeforeNode(dll.getNodeAtPos(7) , ["hello" , 'e'])
    dll.traverseList()

    dll.deleteNode(dll.getNodeAtPos(1))
    print("\nafter deleting head")
    dll.traverseList()

    dll.deleteNode(dll.getNodeAtPos(7))
    print("\nafter deleting tail")
    dll.traverseList()

    dll.deleteNode(dll.getNodeAtPos(3))
    print("\nafter deleting node at pos = 3")
    dll.traverseList()


    dll.reverseLinkedList()
    print("\nafter reversing = ")
    dll.traverseList()

    dll.deleteNodeAtPos(1)
    print("\nafter deleting head = ")
    dll.traverseList()


    dll.sortLinkedList()
    print("\nafter sorting = ")
    dll.traverseList()

    dll.sortLinkedList(reverse=True)
    print("\nafter sorting reverse ")
    dll.traverseList()

    dll.insertAtFront([1 , 'a'])
    print("\nafter inserting [1,a]  at start")
    dll.traverseList()

    dll.insertAtEnd([1 , 'a'])
    dll.insertAtEnd([1 , 'a'])
    dll.insertAtEnd([1 , 'a'])
    print("\nafter inserting [1,a]  at end")
    dll.traverseList()

    dll.delDuplicateUnShorted()
    print("\nafter dup delete = ")
    dll.traverseList()




if __name__ == "__main__":
    test()



            

        






