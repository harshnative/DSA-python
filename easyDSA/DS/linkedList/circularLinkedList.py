
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
            self.head = nextNode

        del node





        







def test():
    dll = CircularLinkedList()

    print("1")
    dll.insertAtEnd(1 , 'a')
    dll.traverseList()

    print("\n2")
    dll.insertAtEnd(2 , 'b')
    dll.traverseList()

    print("\n3")
    dll.insertAtEnd(3 , 'c')
    dll.traverseList()

    print("\n4")
    dll.insertAtEnd(4 , 'd')
    dll.traverseList()

    print("\n5")
    dll.insertAtFront(5 , 'e')
    dll.traverseList()

    print("\n6")
    dll.insertAtFront(6 , 'e')
    dll.traverseList()

    print("\n7")
    dll.insertAfterNode(dll.getNodeAtPos(3) , "hello" , 'e')
    dll.traverseList()

    print("\n8")
    dll.insertBeforeNode(dll.getNodeAtPos(7) , "bye" , 'e')
    dll.traverseList()

    print("\n9")
    print(dll.getNodeAtPos(12).data)
    dll.insertBeforeNode(dll.getNodeAtPos(12) , "tata" , 's')
    dll.traverseList()


    print("\nlist length = " , dll.getListLength())

    print("\nlist = " , dll.returnList())


if __name__ == "__main__":
    test()

