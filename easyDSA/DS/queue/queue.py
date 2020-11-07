from collections import deque


# main class to implement queue
class Queue:

    def __init__(self):
        self.queue = deque()
    
    # method to push data into queue
    def enqueue(self , *data):
        self.queue.append(list(data))

    # method to get the first element of queue
    def peek(self):
        try:
            return self.queue[0]
        except IndexError:
            return None

    # method to check whether the queue is empty or not
    def isEmpty(self):
        try:
            self.queue[0]
            return False
        except IndexError:
            return True

    # method to remove the first element from queue
    def dequeue(self):
        try:
            return self.queue.popleft()
        except IndexError:
            return None
    

if __name__ == "__main__":
    
    q = Queue()
    q.enqueue(1 , 2)
    q.enqueue(2 , 3)
    q.enqueue(3 , 4)
    q.enqueue(4 , 5)
    print(q.peek())
    print(q.isEmpty())
    print(q.dequeue())
    print(q.peek())
    print(q.isEmpty())
    print(q.dequeue())
    print(q.peek())
    print(q.isEmpty())
    print(q.dequeue())
    print(q.peek())
    print(q.isEmpty())
    print(q.dequeue())
    print(q.peek())
    print(q.isEmpty())
    print(q.dequeue())
    print(q.peek())
    print(q.isEmpty())
    print(q.dequeue())
