
# Node class
class Node:

    def __init__(self , data):

        temp = []
        if(type(data) != type(temp)):
            raise RuntimeError("list argument is excepted as data")

        # data list
        self.data = data

        # next pointer 
        self.next = None






class SinglyLinkedList:

    def __init__(self):
        self.head = None

        # cache obj for last node
        self.lastNodeCache = None

    # function to return the head
    def returnHead(self):
        return self.head


    # set custom head to perform operations
    def setCustomHead(self , head , deletePrevList=True):
        if(deletePrevList):
            self.deleteEntireList()

        self.head = head


    # function to insert a node at front
    def insertAtFront(self , data):

        """Algo - 
        1. get a new node and add data
        2. make this new node point to head
        3. make the new node as head"""

        newNode = Node(data)

        newNode.next = self.head

        self.head = newNode

    

    # function to get the last node
    def getLastNode(self, getForCache = True):

        # returning the last node from cache O(1)
        if((getForCache) and (self.lastNodeCache != None)):
            return self.lastNodeCache

        else:


            # traversing till last Node
            last = self.head

            if(last == None):
                return None

            while(last.next != None):

                # return the last node even if the list is circular to avoid infinite loop
                if(last.next == self.head):
                    break

                last = last.next

            # storing the last node in cache
            self.lastNodeCache = last

            return last


    # function to insert at end
    def insertAtEnd(self , data , useCache = True):

        """Algo - 
        1. get a new node and add data
        2. if the linked list is empty then the new node will be head
        3. else get the last node
        4. make the last node point to new node"""

        newNode = Node(data)

        if(self.head == None):
            newNode.next = self.head
            self.head = newNode
            return

        

        # getting last node
        last = self.getLastNode(useCache)

        last.next = newNode

        self.lastNodeCache = newNode


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


    # function to insert a node after a provided node
    def insertAfterNode(self , prevNode , data):

        """Algo - 
        1. generate new node
        2. make the newNode point to next node of prev node
        3. make the prev node point to new node"""

        if(prevNode == None):
                raise RuntimeError("prev node should not be None")

        newNode = Node(data)

        newNode.next = prevNode.next

        prevNode.next = newNode

        self.lastNodeCache = None


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

        
    # function to traverse the list
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

    

    
    # function to delete a node by matching the key - deletes the first occurence
    # if the keylist is passed then it will matched against the data list
    # if the key is passed then if the data list contains that key is checked 
    # if the startform is passed then traversing will start from their
    # start is a list type containing the node and the prev node -> [currentNode , prevNode]
    def deleteNodeAtKey(self , keyList = None , key = None , startForm = None):

        # for tracking the prev node
        prev = None

        # for tracking wheather to delete a node or not
        delete = False

        # for traversing the list 
        last = self.head

        # if the start form is passed
        if(startForm != None):
            last = startForm[0]
            prev = startForm[1]


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

                # if the node is head itself
                if(prev == None):
                    self.head = last.next
                    return [last.next , prev]
                
                else:
                    nextNode = last.next               
                    prev.next = nextNode
                    return [last.next , prev]


            prev = last
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




    # function to delete a node
    def deleteNode(self , node):

        # for keeping track of prev node
        prev = None

        last = self.head

        while(last != None):

            # if the pos is found
            if(last == node):

                if(prev == None):
                    self.head = last.next
                    del last
                    return
                
                else:
                    prev.next = last.next
                    del last
                    return

            prev = last
            last = last.next

            # just to avoid infinite loop
            if(last == self.head):
                break



    
    # fucntion for deleting the node at a certain position
    # position starts from 1 
    def deleteNodeAtPos(self , pos):

        if(pos < 1):
            raise Exception("position should not be less than 1 , head is at 1'st position")

        # for keeping track of prev node
        prev = None

        tempPos = 1

        last = self.head

        while(last != None):

            # if the pos is found
            if(pos == tempPos):

                # if the pos is head
                if(prev == None):
                    self.head = last.next


                prev.next = last.next

            prev = last
            last = last.next
            tempPos += 1


    # method to delete the entire linked list
    # data and reference both are deleted
    def deleteEntireList(self):

        last = self.head

        while(last != None):

            nextNode = last.next

            del last.data
            del last.next

            last = nextNode

        self.head = None



    # function to return the node containing certain key
    def getNodeAtKey(self , keyList = None , key = None , startForm = None):

        # for tracking wheather to return a node or not
        returnNode = False

        # for traversing the list 
        last = self.head

        # if the start form is passed
        if(startForm != None):
            last = startForm

        # till be reach list end
        while(last != None):
            
            # if the key list is none then we check for the element in the data list
            if(keyList == None):
                
                # if the elment is found the we need return this node
                for i in last.data:
                    if(i == key):
                        returnNode = True
            
            # if the key list is passed then we have to match it to the list
            else:
                if(last.data == keyList):
                    returnNode = True

            # if the node is set to be returned
            if(returnNode):
                return last

            last = last.next

            # just to avoid infinite loop
            if(last == self.head):
                break

        return None

        
    def getAllNodeAtKey(self , keyList = None , key = None , startForm = None):

        # for tracking wheather to return a node or not
        returnNode = False

        # for traversing the list 
        last = self.head

        # list of nodes to return
        nodeListToReturn = []

        # if the start form is passed
        if(startForm != None):
            last = startForm

        # till be reach list end
        while(last != None):
            
            # if the key list is none then we check for the element in the data list
            if(keyList == None):
                
                # if the elment is found the we need return this node
                for i in last.data:
                    if(i == key):
                        returnNode = True
            
            # if the key list is passed then we have to match it to the list
            else:
                if(last.data == keyList):
                    returnNode = True

            # if the node is set to be returned
            if(returnNode):
                returnNode = False
                nodeListToReturn.append(last)

            last = last.next

            # just to avoid infinite loop
            if(last == self.head):
                break

        return nodeListToReturn


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
                    self.deleteNodeAtKey(last.data , startForm=[last.next , last])
                try:
                    self.deleteNodeAtKey(key=last.data[specificPosInData] , startForm=last.next)
                except IndexError:
                    raise IndexError("list index out of range - keep in mind : position is considered like index here , starting form zero")
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
                        self.deleteNodeAtKey(last.data , startForm=[last.next , last])
                    else:
                        try:
                            self.deleteNodeAtKey(key=last.data[specificPosInData] , startForm=last.next)
                        except IndexError:
                            raise IndexError("list index out of range - keep in mind : position is considered like index here , starting form zero")
                else:
                    temp = temp.next

            last = last.next


    # function to reverse a linked list
    def reverseLinkedList(self):
        current = self.head
        prev = None
        next = None
        
        while(current != None):

            # storing next
            next = current.next

            # reversing the direction
            current.next = prev

            # moving to next element
            prev = current
            current = next

            # just to avoid infinite loop
            if(current == self.head):
                break


                    

            
            
            


    
            



                


















def test():
    sll = SinglyLinkedList()

    sll.insertAtEnd([1 , "a"])
    sll.insertAtEnd([2 , "b"])
    sll.insertAtEnd([3 , "c"])
    sll.insertAtEnd([4 , "d"])
    sll.insertAtEnd([5 , "e"])
    sll.insertAtFront([0.5 , "f"])

    print("first linked list = \n")
    sll.traverseList()

    sll1 = SinglyLinkedList()

    sll1.insertAtEnd([1])
    sll1.insertAtEnd([2])
    sll1.insertAtEnd([3])
    sll1.insertAfterNode(sll1.getNodeAtPos(2) , [2.5])
    sll1.insertAtEnd([4])
    sll1.insertAtEnd([5])
    sll1.insertAtFront([0.5 , "f"])

    print("\nsecond linked list = \n")
    sll1.traverseList()

    print("\n second list form  2 to end\n")
    print(sll1.returnList(2))

    print("\n second list form  2 to 5\n")
    print(sll1.returnList(2 , 5))

    print("\n deleting [0.5 , f] from list\n")
    sll1.deleteNodeAtKey(keyList=[0.5 , "f"])
    sll1.traverseList()

    print("\n List after adding [0.6 , 'h']\n")
    sll1.insertAtFront([0.6 , "h"])
    sll1.traverseList()

    print("\n deleting node containing 0.6  from list\n")
    sll1.deleteNodeAtKey(key=0.6)
    sll1.traverseList()

    print("\n List after adding 2 at front\n")
    sll1.insertAtFront([2])
    sll1.traverseList()

    print("\n List after adding 3 2's at end\n")
    sll1.insertAtEnd([2])
    sll1.insertAtEnd([2])
    sll1.insertAtEnd([2])
    sll1.traverseList()

    print("\n List after adding 3 2's at front\n")
    sll1.insertAtFront([2])
    sll1.insertAtFront([2])
    sll1.insertAtFront([2])
    sll1.traverseList()

    print("\n List after adding 3 2's at after 2.5\n")
    pos = sll1.getNodeAtPos(7)
    sll1.insertAfterNode(pos , [2])
    sll1.insertAfterNode(pos , [2])
    sll1.insertAfterNode(pos , [2])
    sll1.traverseList()

    print("\n after removing all duplicate elements")
    sll1.delDuplicateUnShorted()
    sll1.traverseList()


    print("\n After sorting\n")
    sll1.sortLinkedList(reverse=True)
    sll1.traverseList()

    # print("\n after removing all duplicate elements")
    # sll1.delDuplicateShorted()
    # sll1.traverseList()



    

    # print("\n deleting node containing all 2  from list\n")
    # sll1.deleteAllNodeAtKey(key=2)
    # sll1.traverseList()

    # print("\n deleting node containing 2.5  from list\n")
    # sll1.deleteNodeAtKey(key=2.5)
    # sll1.traverseList()

    # print("\n deleting node at 2nd pos from list\n")
    # sll1.deleteNodeAtPos(2)
    # sll1.traverseList()

    # print("\n After adding 6 to front\n")
    # sll1.insertAtFront(6)
    # sll1.traverseList()

    # print("\n After sorting \n")
    # sll1.sortLinkedList()
    # sll1.traverseList()

    # print("\n After sorting in reverse\n")
    # sll1.sortLinkedList(reverse=True)
    # sll1.traverseList()

    # print("\n deleting entire list\n")
    # sll1.deleteEntireList()
    # sll1.traverseList()

    
if __name__ == "__main__":
    test()
    # pass
