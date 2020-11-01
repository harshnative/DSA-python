
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
class __CircularLinkedList:


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
        self.cll = __CircularLinkedList()

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
        self.cll.returnHead()










    


if __name__ == "__main__":
    stackObj = StackUsingArray()

    stackObj.push(1)
    stackObj.push(2)
    stackObj.push(3)
    stackObj.push(4)
    print(stackObj.pop())
    print(stackObj.pop())
    print(stackObj.pop())
    print(stackObj.pop())
    print(stackObj.pop())
    print(stackObj.returnList())