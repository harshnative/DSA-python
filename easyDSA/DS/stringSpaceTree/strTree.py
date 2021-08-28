class Node:
    
    def __init__(self , data = None , parent = None , nextNodes = None):
        self.data = data

        if(nextNodes == None):
            self.nextNodes = []
        else:
            self.nextNodes = nextNodes

        self.parent = parent





class StringSpaceTree:


    def __init__(self):
        self.root = Node()

    def binarySearch(cls , iterator , elementToSearch):

        # init low , high acc to index so low is 0 and high is len - 1
        low = 0
        lenIterator = len(iterator) - 1
        high = lenIterator

        while(low <= high):

            # if the element is at low then simply return the low as its index number is low
            if(iterator[low].data == elementToSearch):
                return low
        
            # if the element is at high then simply return the high as its the element index
            if(iterator[high].data == elementToSearch):
                return high
            
            # mid will be low + as we need to find the mid element od rest array and adding low to actual mid will help in that
            mid = low + ((high - low)//2)


            # if the element is found at mid then return mid
            if(iterator[mid].data == elementToSearch):
                return mid
            
            # else if the element is in lower array then change the high
            if(iterator[mid].data > elementToSearch):
                high = mid - 1

            # else if the element is in upper array then change the low
            elif(iterator[mid].data < elementToSearch):
                low = mid + 1
            
        # if element is not found then return None
        return None


    def insertIntoTree(self , string):

        string = str(string)
        lenString = len(string)

        currentNode = self.root
        

        for i in range(lenString):

            charToInsert = string[i]
            foundExistingNode = False
            foundNode = None
                    
            result = self.binarySearch(currentNode.nextNodes , charToInsert)

            if(result != None):
                foundExistingNode = True
                foundNode = currentNode.nextNodes[result]



            if(foundExistingNode):
                currentNode = foundNode
            else:
                newNode = Node(charToInsert , parent=currentNode)

                currentNode.nextNodes.append(newNode)

                currentNode.nextNodes = sorted(currentNode.nextNodes , key=lambda x: x.data)
                
                currentNode = newNode


    def tempfunc(self , node):
        string = ""

        if(node == None):
            return ""

        if(node != None):
            string = string + node.data

        while(True):
            node = node.parent

            if((node == None) or (node.data == None)):
                break

            # print("node = " , node.data)
            string = string + node.data


        strList = list(string)
        strList.reverse()
        string = "".join(strList)

        return string
                        

    def traverse(self):

        nodesList = []
        traversed = False
        stringList = []

        def innerTraverse(currentNode):

            if(currentNode != None):

                nonlocal nodesList
                nonlocal traversed

                nextNode = currentNode.nextNodes

                lastNode = None

                for j in nextNode:
                    lastNode = j
                    traversed = True

                    innerTraverse(j)

                if(lastNode != None and traversed):
                    traversed = False
                    stringList.append(self.tempfunc(lastNode))

        innerTraverse(self.root)

        return stringList




    def searchInTree(self , string):

        string = str(string)
        lenString = len(string)

        currentNode = self.root

        found = 0

        for i in range(lenString):

            charToSearch = string[i]
            foundExistingNode = False
            foundNode = None

            result = self.binarySearch(currentNode.nextNodes , charToSearch)

            if(result != None):
                foundExistingNode = True
                foundNode = currentNode.nextNodes[result]


            if(foundExistingNode):
                currentNode = foundNode
                found = found + 1
            else:
                return False

            
        if(found == lenString):
            return True

    def deleteInTree(self , string):

        string = str(string)
        lenString = len(string)

        currentNode = self.root

        found = 0

        for i in range(lenString):

            charToSearch = string[i]
            foundExistingNode = False
            foundNode = None

            result = self.binarySearch(currentNode.nextNodes , charToSearch)

            if(result != None):
                foundExistingNode = True
                foundNode = currentNode.nextNodes[result]

            if(foundExistingNode):
                if(len(foundNode.nextNodes) <= 1):
                    currentNode.nextNodes.remove(foundNode)
                    nextNode = foundNode

                    toDelete = []

                    while(True):
                        try:
                            nextNode = nextNode.nextNodes[0]
                            toDelete.append(nextNode)
                        except IndexError:
                            break

                    for i in toDelete:
                        del i

                    del foundNode
                    return True
                else:
                    currentNode = foundNode
            else:
                return False

            
        return None

            



    



if __name__ == "__main__":


    # obj = StringSpaceTree()

    # obj.insertIntoTree("bear")
    # obj.insertIntoTree("bell")
    # obj.insertIntoTree("bid")
    # obj.insertIntoTree("bull")
    # obj.insertIntoTree("sell")
    # obj.insertIntoTree("stock")
    # obj.insertIntoTree("stop")

    # print(obj.searchInTree("bull"))

    # print(obj.traverse())

    # print(obj.deleteInTree("bull"))

    # print(obj.traverse())


    import string
    import random

    randomStringList = list(string.ascii_letters + string.digits + string.whitespace)
    randomStringList.extend(["!" , "@" , "#" , "$" , "%" , "^" , "&" , "*"])


    for i in range(1000):
        print(i)

        obj = StringSpaceTree()

        stringList = []

        for k in range(100):

            myString = ""

            for j in range(random.randint(10 , 100)):
                myString = myString + random.choice(randomStringList)

            obj.insertIntoTree(myString)

            if(myString not in stringList):
                stringList.append(myString)

        objList = obj.traverse()

        count = 0

        for i in stringList:
            for j in objList:
                if(i == j):
                    count = count + 1
        
        if(count != len(objList)):
            print("error" , stringList , objList)
            input()

        for i in stringList:
            obj.deleteInTree(i)

        if(len(obj.traverse()) != 0):
            print("error" , obj.traverse())
            input()











        

