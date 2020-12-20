import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from linkedList.circularLinkedList import CircularLinkedList
from linkedList.circularLinkedList_listType import CircularLinkedList as CircularLinkedList_listType


class Queue:
    def __init__(self):
        self.cll = CircularLinkedList()

    def enqueue(self , data):
        self.cll.insertAtEnd(data)
    
    def dequeue(self , returnNone = True):
        toReturn = self.cll.head

        # if the stack is empty then return None
        if(toReturn == None):
            if(returnNone):
                return None
            else:
                raise RuntimeError("dequeue from empty queue")

        self.cll.deleteNode(toReturn)

        return toReturn.data

    def isEmpty(self):
        toReturn = self.cll.head

        # if the last node is None then the stack is empty
        if(toReturn == None):
            return True
        else:
            return False

        
    def getFront(self , returnNone = True):
        toReturn = self.cll.head

        # if the stack is empty then return None
        if(toReturn == None):
            if(returnNone):
                return None
            else:
                raise RuntimeError("dequeue from empty queue")

        return toReturn.data


    # function to return data of the last element
    def getEnd(self , returnNone = True):
        toReturn = self.cll.getLastNode()

        # if the stack is empty then return None
        if(toReturn == None):
            if(returnNone):
                return None
            else:
                raise RuntimeError("pop on empty stack")

        # else return data
        return toReturn.data

class QueueListType:
    def __init__(self):
        self.cll = CircularLinkedList_listType()

    def enqueue(self , data):
        self.cll.insertAtEnd(data)
    
    def dequeue(self , returnNone = True):
        toReturn = self.cll.head

        # if the stack is empty then return None
        if(toReturn == None):
            if(returnNone):
                return None
            else:
                raise RuntimeError("dequeue from empty queue")

        self.cll.deleteNode(toReturn)

        return toReturn.data

    def isEmpty(self):
        toReturn = self.cll.head

        # if the last node is None then the stack is empty
        if(toReturn == None):
            return True
        else:
            return False

        
    def getFront(self , returnNone = True):
        toReturn = self.cll.head

        # if the stack is empty then return None
        if(toReturn == None):
            if(returnNone):
                return None
            else:
                raise RuntimeError("dequeue from empty queue")

        return toReturn.data

    # function to return data of the last element
    def getEnd(self , returnNone = True):
        toReturn = self.cll.getLastNode()

        # if the stack is empty then return None
        if(toReturn == None):
            if(returnNone):
                return None
            else:
                raise RuntimeError("pop on empty stack")

        # else return data
        return toReturn.data





if __name__ == "__main__":
    
    # q = Queue()
    q = QueueListType()
    # q.enqueue(1)
    # q.enqueue(2)
    # q.enqueue(3)
    # q.enqueue(4)


    q.enqueue([1 , 2])
    q.enqueue([3 , 4])
    q.enqueue([5 , 6])
    q.enqueue([7 , 8])



    print(q.getFront() , q.getEnd())
    print(q.isEmpty())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.isEmpty())
    print(q.getFront() , q.getEnd())




