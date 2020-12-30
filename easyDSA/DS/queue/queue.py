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

        # if the queue is empty then return None
        if(toReturn == None):
            if(returnNone):
                return None
            else:
                raise RuntimeError("dequeue from empty queue")

        self.cll.deleteNode(toReturn)

        return toReturn.data

    def removeEnd(self , returnNone = True):
        toReturn = self.cll.getLastNode()

        # if the queue is empty then return None
        if(toReturn == None):
            if(returnNone):
                return None
            else:
                raise RuntimeError("dequeue from empty queue")

        self.cll.deleteNode(toReturn)

        return toReturn.data


    def isEmpty(self):
        toReturn = self.cll.head

        # if the last node is None then the queue is empty
        if(toReturn == None):
            return True
        else:
            return False

        
    def getFront(self , returnNone = True):
        toReturn = self.cll.head

        # if the queue is empty then return None
        if(toReturn == None):
            if(returnNone):
                return None
            else:
                raise RuntimeError("dequeue from empty queue")

        return toReturn.data


    # function to return data of the last element
    def getEnd(self , returnNone = True):
        toReturn = self.cll.getLastNode()

        # if the queue is empty then return None
        if(toReturn == None):
            if(returnNone):
                return None
            else:
                raise RuntimeError("pop on empty queue")

        # else return data
        return toReturn.data
    

    # function to return the head so that more operations can be performed
    def returnObj(self):
        return self.cll



class QueueListType:
    def __init__(self):
        self.cll = CircularLinkedList_listType()

    def enqueue(self , data):
        self.cll.insertAtEnd(data)
    
    def dequeue(self , returnNone = True):
        toReturn = self.cll.head

        # if the queue is empty then return None
        if(toReturn == None):
            if(returnNone):
                return None
            else:
                raise RuntimeError("dequeue from empty queue")

        self.cll.deleteNode(toReturn)

        return toReturn.data

    def removeEnd(self , returnNone = True):
        toReturn = self.cll.getLastNode()

        # if the queue is empty then return None
        if(toReturn == None):
            if(returnNone):
                return None
            else:
                raise RuntimeError("dequeue from empty queue")

        self.cll.deleteNode(toReturn)

        return toReturn.data

    def isEmpty(self):
        toReturn = self.cll.head

        # if the last node is None then the queue is empty
        if(toReturn == None):
            return True
        else:
            return False

        
    def getFront(self , returnNone = True):
        toReturn = self.cll.head

        # if the queue is empty then return None
        if(toReturn == None):
            if(returnNone):
                return None
            else:
                raise RuntimeError("dequeue from empty queue")

        return toReturn.data

    # function to return data of the last element
    def getEnd(self , returnNone = True):
        toReturn = self.cll.getLastNode()

        # if the queue is empty then return None
        if(toReturn == None):
            if(returnNone):
                return None
            else:
                raise RuntimeError("pop on empty queue")

        # else return data
        return toReturn.data


    # function to return the head so that more operations can be performed
    def returnObj(self):
        return self.cll



# class containing some pre build queue opeartion
class QueueOperations:

    # method for reversing a queue
    # accepts queue obj generated by above two classes
    @classmethod
    def reverseQueue(cls , queueObj):
        queueObj.cll.reverseLinkedList()
        

    # method to sort a queue
    @classmethod
    def sortQueue(cls , queueObj , reverse = False):

        # else it is converted to the list first 
        queue = []

        while(not(queueObj.isEmpty())):
            queue.append(queueObj.dequeue())

        queue.sort(reverse = (reverse))

        for i in queue:
            queueObj.enqueue(i)


    # method to sort a queue
    @classmethod
    def sortQueue_listType(cls , queueObj , listPos_reference = 0 , reverse = False):

        # else it is converted to the list first 
        queue = []

        while(not(queueObj.isEmpty())):
            queue.append(queueObj.dequeue())

        queue.sort(key = lambda x: x[listPos_reference] ,  reverse = (reverse))

        for i in queue:
            queueObj.enqueue(i)



    @classmethod
    def getLength(cls , queueObj):
        return queueObj.cll.getListLength()

    
    @classmethod
    def traverse(cls , queueObj , reverse = False , listType = False , nodeSeperator = " -> " , justReturn = False , forNode_start = "[ " , forNode_end = " ]"):
        
        dataArgs_seperator = " , "

        result = ""

        if(not(reverse)):
            last = queueObj.cll.head

            result = result + " ..Front.. "
            # till be reach list end
            while((last != None)):

                # adding the node starting string "[ "
                if(forNode_start != None):
                    result = result + forNode_start

                # adding the elements in last.data list seperated with dataArgs_seperator
                if(listType):
                    for i in last.data:
                        result = result + str(i) + dataArgs_seperator

                    # removing the lastly added dataArgs_seperator
                    result = result[:(len(dataArgs_seperator) * -1)]

                else:
                    result = result + str(last.data)
                

                # adding the node end string " ]"
                if(forNode_end != None):
                    result = result + forNode_end

                # adding the node seperator
                result = result + nodeSeperator

                last = last.next

                if(last == queueObj.cll.head):
                    break

            # removing the lastly added nodeSeperator
            result = result[:(len(nodeSeperator) * -1)]
            result = result + " ..End.. "



        else:
            tempNodeVar = queueObj.cll.getLastNode()
            last = queueObj.cll.getLastNode()

            result = result + " ..End.. "
            # till be reach list end
            while((last != None)):

                # adding the node starting string "[ "
                if(forNode_start != None):
                    result = result + forNode_start

                # adding the elements in last.data list seperated with dataArgs_seperator
                if(listType):
                    for i in last.data:
                        result = result + str(i) + dataArgs_seperator

                    # removing the lastly added dataArgs_seperator
                    result = result[:(len(dataArgs_seperator) * -1)]

                else:
                    result = result + str(last.data)
                

                # adding the node end string " ]"
                if(forNode_end != None):
                    result = result + forNode_end

                # adding the node seperator
                result = result + nodeSeperator

                last = last.prev

                if(last == tempNodeVar):
                    break

            # removing the lastly added nodeSeperator
            result = result[:(len(nodeSeperator) * -1)]
            result = result + " ..Front.. "

        if(justReturn):
            return result
        else:
            print(result)
            return result





if __name__ == "__main__":
    
    # q = Queue()
    q = QueueListType()
    # q.enqueue(1)
    # q.enqueue(2)
    # q.enqueue(3)
    # q.enqueue(4)


    q.enqueue([1 , 2])
    q.enqueue([3 , 4])
    q.enqueue([55 , 6])
    q.enqueue([7 , 8])


    QueueOperations.traverse(q)
    QueueOperations.sortQueue_listType(q)
    QueueOperations.traverse(q)
    print(q.getFront() , q.getEnd())
    print(q.isEmpty())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.isEmpty())
    print(q.getFront() , q.getEnd())




