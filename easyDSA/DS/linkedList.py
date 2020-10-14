

# Node class
class Node:

    def __init__(self , *dataArgs):

        # data list
        self.data = list(*dataArgs)

        # next pointer 
        self.next = None






class SinglyLinkedList:

    def __init__(self):
        self.head = None

        # cache obj for last node
        self.lastNodeCache = None


    # function to insert a node at front
    def insertAtFront(self , *dataArgs):

        """Algo - 
        1. get a new node and add data
        2. make this new node point to head
        3. make the new node as head"""

        newNode = Node(dataArgs)

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

            while(last.next != None):

                # return the last node even if the list is circular to avoid infinite loop
                if(last.next == self.head):
                    break

                last = last.next

            # storing the last node in cache
            self.lastNodeCache = last

            return last


    # function to insert at end
    def insertAtEnd(self , *dataArgs , useCache = True):

        """Algo - 
        1. get a new node and add data
        2. if the linked list is empty then the new node will be head
        3. else get the last node
        4. make the last node point to new node"""

        newNode = Node(dataArgs)

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

        return last


    # function to insert a node after a provided node
    # raise error if the prev node is None else operation is not performed
    def insertAfterNode(self , prevNode , *dataArgs , raiseError = True):

        """Algo - 
        1. generate new node
        2. make the newNode point to next node of prev node
        3. make the prev node point to new node"""

        if(prevNode == None):
            if(raiseError):
                raise RuntimeError("prev node should not be None")
            else:
                return

        newNode = Node(dataArgs)

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


    # function to traverse the list
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












def test():
    sll = SinglyLinkedList()

    sll.insertAtEnd(1 , "a")
    sll.insertAtEnd(2 , "b")
    sll.insertAtEnd(3 , "c")
    sll.insertAtEnd(4 , "d")
    sll.insertAtEnd(5 , "e")
    sll.insertAtFront(0.5 , "f")

    print("first linked list = \n")
    sll.traverseList()

    sll1 = SinglyLinkedList()

    sll1.insertAtEnd(1)
    sll1.insertAtEnd(2)
    sll1.insertAtEnd(3)
    sll1.insertAfterNode(sll1.getNodeAtPos(2) , 2.5)
    sll1.insertAtEnd(4)
    sll1.insertAtEnd(5)
    sll1.insertAtFront(0.5 , "f")

    print("\nsecond linked list = \n")
    sll1.traverseList()

    print("\n second list form  2 to end\n")
    print(sll1.returnList(2))

    print("\n second list form  2 to 5\n")
    print(sll1.returnList(2 , 5))
    
if __name__ == "__main__":
    test()
    # pass
