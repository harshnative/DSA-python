
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
class DoublyLinkedList:


    def __init__(self):
        self.head = None

        self.lastNodeCache = None


    
    # function to insert at front
    def insertAtFront(self, *dataArgs):

        """algo - 
        1. insert the data , make the newNode.next = self.head
        2. newNode.prev = None
        3. if the head is not none then head.prev = newNode
        4. make the new Node as head"""

        newNode = Node(dataArgs)

        newNode.next = self.head
        newNode.prev = None

        if(self.head != None):
            self.head.prev = newNode

        self.head = newNode


    # function to insert a node after a node
    def insertAfterNode(self , prevNode , *dataArgs):

        """Algo - 
        1. make new node
        2. newNode.next = prevNode.next
        3. prevNode.next = newNode
        4. newNode.prev = prevNode
        5. if the newNode.next is not None then prev of newNode.next is newNode"""

        if(prevNode == None):
            raise Exception("prevNode cannot be None")

        
        newNode = Node(dataArgs)

        newNode.next = prevNode.next
        prevNode.next = newNode

        newNode.prev = prevNode

        if(newNode.next != None):
            newNode.next.prev = newNode

        self.lastNodeCache = None


    def getLastNode(self, useCache = True):

        # using the cache
        if(useCache and (self.lastNodeCache != None)):
            return self.lastNodeCache

        else:
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
    def insertAtEnd(self , *dataArgs , useCache = True):

        """algo - 
        1. get the last node
        2. if the last node is none the insert at front
        3. insert the node after prev node = lastNode
        """

        lastNode = self.getLastNode(useCache)

        if(lastNode == None):
            self.insertAtFront(*dataArgs)

        else:
            prevNode = lastNode
            newNode = Node(dataArgs)

            newNode.next = prevNode.next
            prevNode.next = newNode

            newNode.prev = prevNode

            self.lastNodeCache = newNode

    
    # function to insert a node before a node
    def insertBeforeNode(self , node , *dataArgs):

        prevNode = node.prev

        if(prevNode == None):
            if(node != self.head):
                raise Exception("node.prev is none but node is not head")
            else:
                self.insertAtFront(*dataArgs)
            
        else:
            self.insertAfterNode(prevNode , *dataArgs)

    

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









def test():
    dll = DoublyLinkedList()
    dll.insertAtEnd(1 , 'a' , useCache= True)
    dll.insertAtEnd(2 , 'b' , useCache= True)
    dll.insertAtEnd(3 , 'c', useCache= True)
    dll.insertAtEnd(4 , 'd' , useCache= True)
    dll.insertAtFront(5 , 'e')
    dll.insertAtFront(6 , 'e')
    dll.insertAfterNode(dll.getNodeAtPos(3) , "hello" , 'e')
    dll.insertBeforeNode(dll.getNodeAtPos(7) , "hello" , 'e')
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



if __name__ == "__main__":
    test()



            

        






