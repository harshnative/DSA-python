

# Node class
class Node:

    def __init__(self , *dataArgs):

        # data list
        self.data = [item for item in dataArgs]

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

        if(self.head == None):
            self.insertAtFront(dataArgs)
            return

        newNode = Node(dataArgs)

        # getting last node
        last = self.getLastNode(useCache)

        last.next = newNode

        self.lastNodeCache = newNode


    # function to return a node at pos
    # raiseError if the pos is not found else return None
    def returnNodeAtPos(self, pos , raiseError = False):

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
