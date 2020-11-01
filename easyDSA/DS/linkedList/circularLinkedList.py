
# Node class
class Node:

    def __init__(self , *dataArgs , next=None , prev=None):

        # data list
        self.data = list(*dataArgs)

        # prev pointer
        self.prev = prev

        # next pointer 
        self.next = next



# main class of module
class CircularLinkedList:


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

    # function to insert in a empty list
    def insertInEmpty(self , *dataArgs):
        if(self.head != None):
            raise Exception("only insert in empty list")

        newNode = Node(dataArgs)

        self.head = newNode

        # making it pointing to himself
        self.head.next = self.head
        self.head.prev = self.head



    # function to insert at front
    def insertAtFront(self, *dataArgs):

        # if the list if initially empty 
        if(self.head == None):
            self.insertInEmpty(*dataArgs)
            return

        # getting new node
        newNode = Node(dataArgs)
    
        lastNode = self.getLastNode()
        
        # new node will point to current head
        newNode.next = self.head

        # current head prev will point to new node
        self.head.prev = newNode

        # newNode prev will point to last 
        newNode.prev = lastNode

        # last node will point to new node
        lastNode.next = newNode

        # hence head will be new node
        self.head = newNode


    # function to insert a node after a node
    def insertAfterNode(self , prevNode , *dataArgs):
        
        # if the list if initially empty 
        if(self.head == None):
            self.insertInEmpty(*dataArgs)
            return
        

        # if the prev node is tail
        if(prevNode == self.getLastNode()):
            self.insertAtEnd(*dataArgs)
            return 

        newNode = Node(dataArgs)

        newNode.next = prevNode.next
        newNode.prev = prevNode

        prevNode.next.prev = newNode

        prevNode.next = newNode


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

    
    
    # function to insert a node before a node
    def insertBeforeNode(self , node , *dataArgs):

        self.insertAfterNode(node.prev , *dataArgs)

    

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


    # function to return a node at pos
    # raiseError if the pos is not found else return None
    def getNodeAtPos(self, pos , raiseError = False , continueLoop = True):

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

            if((last.next == self.head) and not(continueLoop)):
                break

        if(not(found) and raiseError):
            raise RuntimeError("position could not be found")
        elif(not(found)):
            return None

        return last



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


    # function to delete node at pos
    def deleteNodeAtPos(self, pos):
        node = self.getNodeAtPos(pos , True)
        
        self.deleteNode(node)

    
    # method to delete the entire linked list
    # data and reference both are deleted
    def deleteEntireList(self):

        last = self.head

        temp = self.head

        while(last != None):

            nextNode = last.next

            del last.data
            del last.next
            del last.prev

            last = nextNode

            if(nextNode == temp):
                del temp
                break

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
                self.insertAtFront(*i)
            else:
                self.insertAtEnd(*i)


    # function to delete a node by matching the key - deletes the first occurence
    # if the keylist is passed then it will matched against the data list
    # if the key is passed then if the data list contains that key is checked 
    # if the startform is passed then traversing will start from their
    def deleteNodeAtKey(self , keyList = None , key = None , startForm = None):

        # for tracking wheather to delete a node or not
        delete = False

        # for traversing the list 
        last = self.head

        temp = self.head

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
                self.deleteNode(last)
                temp = self.head
                return last.next

            last = last.next

            # just to avoid infinite loop
            if(last == temp):
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



     # function to delete all the duplicate elements in sorted list
    def delDuplicateShorted(self , entireData = True , specificPosInData = None):

        last = self.head

        # need to check as while loop starts form last.next
        if(last == None):
            return

        while((last.next != None) and (last.next != self.head)):

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

        while((last.next != None) and (last.next != self.head)):

            temp = last

            # second loop for checking the next elements in list with the last element
            while((temp.next != None) and (temp.next != self.head)):
                
                # if the data matches we delete the next node
                if(temp.next.data == last.data):
                    if(entireData):
                        self.deleteNodeAtKey(last.data , startForm=last.next)
                    else:
                        self.deleteNodeAtKey(key=last.data[specificPosInData] , startForm=last.next)
                else:
                    temp = temp.next

            last = last.next


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




        







def test():
    cll = CircularLinkedList()

    print("1")
    cll.insertAtEnd(1 , 'a')
    cll.traverseList()

    print("\n2")
    cll.insertAtEnd(2 , 'b')
    cll.traverseList()

    print("\n3")
    cll.insertAtEnd(3 , 'c')
    cll.traverseList()

    print("\n4")
    cll.insertAtEnd(4 , 'd')
    cll.traverseList()

    print("\n5")
    cll.insertAtFront(5 , 'e')
    cll.traverseList()

    print("\n6")
    cll.insertAtFront(6 , 'e')
    cll.traverseList()

    # print("\n7")
    # cll.insertAfterNode(cll.getNodeAtPos(3) , "hello" , 'e')
    # cll.traverseList()

    # print("\n8")
    # cll.insertBeforeNode(cll.getNodeAtPos(7) , "bye" , 'e')
    # cll.traverseList()

    # print("\n9")
    # cll.insertBeforeNode(cll.getNodeAtPos(12) , "tata" , 's')
    # cll.traverseList()

    # print("\n10")
    # cll.insertBeforeNode(cll.getNodeAtPos(12) , "tata" , 's')
    # cll.traverseList()

    # print("\n11")
    # cll.insertAtFront("tata" , 's')
    # cll.traverseList()

    # print("\n12")
    # cll.insertAtEnd("tata" , 's')
    # cll.traverseList()

    # print("\n13")
    # cll.deleteEntireList()
    # cll.traverseList()

    
    


    print("\n14")
    cll.insertAtFront(1 , 'a')
    cll.traverseList()


    print("\n15")
    cll.insertAtEnd(1 , 'a')
    cll.traverseList()

    print("\n15")
    cll.insertAfterNode( cll.getNodeAtPos(4) ,  1 , 'a')
    cll.traverseList()

    # print("\n13")
    # print(cll.sortLinkedList())
    # cll.traverseList()

    print("\n15")
    cll.delDuplicateUnShorted()
    cll.traverseList()



    


if __name__ == "__main__":
    test()

