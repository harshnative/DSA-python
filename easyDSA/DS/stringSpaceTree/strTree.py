# node object class
class Node:
    
    def __init__(self , data = None , parent = None , nextNodes = None):
        
        # to store data
        self.data = data

        # list to store reference to the child nodes
        if(nextNodes == None):
            self.nextNodes = []
        else:
            self.nextNodes = nextNodes

        # to store reference to parent node 
        self.parent = parent





# main class
class StringSpaceTree:

    # constructor
    # root node will be None always
    def __init__(self):
        self.root = Node()


    # algo to perform a binary search
    def binarySearch(cls , iterator , elementToSearch):

        # init low , high acc to index so low is 0 and high is len - 1
        low = 0
        lenIterator = len(iterator) - 1
        high = lenIterator

        while(low <= high):

            # modified algo , using .data attribute to extract the data from iterator of nodes and compare 

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


    # function to insert a string into string
    # returns True if the string is successfully inserted
    # returns None if the string was already present
    # returns False otherwise
    def insertIntoTree(self , string):

        string = str(string)
        lenString = len(string)

        currentNode = self.root
        count = 0
        
        # returnList the string
        # starting with the root
        for i in range(lenString):

            charToInsert = string[i]
            foundExistingNode = False
            foundNode = None
            
            # check if the current char of string is already a child of current node
            result = self.binarySearch(currentNode.nextNodes , charToInsert)

            # if yes
            # then assign values
            if(result != None):
                foundExistingNode = True
                foundNode = currentNode.nextNodes[result]

            if(foundExistingNode):
                currentNode = foundNode
                count = count + 1
            
            # else make a new node and insert that into current nodes nextNodes list
            else:
                newNode = Node(charToInsert , parent=currentNode)

                currentNode.nextNodes.append(newNode)

                # keeping the list sorted so that we can perform binary search
                currentNode.nextNodes = sorted(currentNode.nextNodes , key=lambda x: x.data)
                
                currentNode = newNode

        # if the count is less then a new node must be inserted
        # means the string was ot already present
        if(count < lenString):
            return True

        # if the count is equal then the string was already present
        elif(count == lenString):
            return None
        else:
            return False

    

    # function to traceback the path to root and convert the path to string
    def traceBackToRoot(self , node):
        string = ""

        # if the node is none return empty string
        if(node == None):
            return ""

        # add the node data to list 
        if(node != None):
            string = string + node.data


        while(True):
            # find the nodes parent
            node = node.parent

            # exist loop if None
            if((node == None) or (node.data == None)):
                break

            # else data nodes parent data to string
            string = string + node.data


        # reversing the path [last -> root] to [root -> last]
        strList = list(string)
        strList.reverse()
        string = "".join(strList)

        return string
                        

    # function to traverse the tree and return list
    def returnList(self):

        nodesList = []
        traversed = False
        stringList = []

        # inner recursion function
        def innerTraverse(currentNode):

            if(currentNode != None):

                nonlocal nodesList
                nonlocal traversed

                nextNode = currentNode.nextNodes

                lastNode = None

                # call the function recursively for next node
                for j in nextNode:
                    lastNode = j
                    traversed = True

                    innerTraverse(j)

                # if the j loop is not runned then don't call traceBack function
                # if we don't do this then this function will also be runned recursively
                if(lastNode != None and traversed):
                    traversed = False
                    stringList.append(self.traceBackToRoot(lastNode))

        innerTraverse(self.root)

        return stringList



    # function to search a string in tree
    # returns True if found
    # else return False
    def searchInTree(self , string):

        string = str(string)
        lenString = len(string)

        currentNode = self.root

        found = 0

        # start with current node and first char
        for i in range(lenString):

            charToSearch = string[i]
            foundExistingNode = False
            foundNode = None

            # find whether the childs of current node as the current char
            result = self.binarySearch(currentNode.nextNodes , charToSearch)

            # if found assign values
            if(result != None):
                foundExistingNode = True
                foundNode = currentNode.nextNodes[result]

            # if found make current node = found node and increase found count
            if(foundExistingNode):
                currentNode = foundNode
                found = found + 1
            else:
                return False

        # if the found count is equal to lenString then return True
        if(found == lenString):
            return True


    # function to delete a string in Tree
    # returns True if the node is deleted
    # retuns False if the node is not present
    # else returns None
    def deleteInTree(self , string):

        string = str(string)
        lenString = len(string)

        currentNode = self.root

        found = 0

        # start with current node and first char
        for i in range(lenString):

            charToSearch = string[i]
            foundExistingNode = False
            foundNode = None

            # find whether the childs of current node as the current char
            result = self.binarySearch(currentNode.nextNodes , charToSearch)

            # if found assign values
            if(result != None):
                foundExistingNode = True
                foundNode = currentNode.nextNodes[result]

            if(foundExistingNode):

                # if the foundNode does not have more than 1 child then we need to delete this node as well as child of it
                if(len(foundNode.nextNodes) <= 1):

                    # remove this node from the parents nextNodes List
                    currentNode.nextNodes.remove(foundNode)

                    # find the next child
                    nextNode = foundNode

                    toDelete = []
                
                    # add all childs to a list
                    while(True):
                        if(len(nextNode.nextNodes) != 0):
                            nextNode = nextNode.nextNodes[0]
                            toDelete.append(nextNode)
                        else:
                            break
                        
                    # delete all child
                    for i in toDelete:
                        del i

                    # delete the node itself
                    del foundNode
                    return True
                else:
                    currentNode = foundNode
            else:
                return False

            
        return None

            



    


# just for testing
if __name__ == "__main__":


    obj = StringSpaceTree()

    print(obj.insertIntoTree("bear"))
    print(obj.insertIntoTree("bell"))
    print(obj.insertIntoTree("bid"))
    print(obj.insertIntoTree("bull"))
    print(obj.insertIntoTree("sell"))
    print(obj.insertIntoTree("stock"))
    print(obj.insertIntoTree("stop"))
    print(obj.insertIntoTree("stop"))

    print(obj.searchInTree("bull"))

    print(obj.returnList())

    print(obj.deleteInTree("bull"))

    print(obj.returnList())


    # import string
    # import random

    # randomStringList = list(string.ascii_letters + string.digits + string.whitespace)
    # randomStringList.extend(["!" , "@" , "#" , "$" , "%" , "^" , "&" , "*"])


    # for i in range(1000):
    #     print(i)

    #     obj = StringSpaceTree()

    #     stringList = []

    #     for k in range(100):

    #         myString = ""

    #         for j in range(random.randint(10 , 100)):
    #             myString = myString + random.choice(randomStringList)

    #         obj.insertIntoTree(myString)

    #         if(myString not in stringList):
    #             stringList.append(myString)

    #     objList = obj.returnList()

    #     count = 0

    #     for i in stringList:
    #         for j in objList:
    #             if(i == j):
    #                 count = count + 1
        
    #     if(count != len(objList)):
    #         print("error" , stringList , objList)
    #         input()

    #     for i in stringList:
    #         obj.deleteInTree(i)

    #     if(len(obj.returnList()) != 0):
    #         print("error" , obj.returnList())
    #         input()











        

