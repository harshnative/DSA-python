# class to init a new node
class Node:
    def __init__(self , data , left=None , right=None , parent=None):
        self.left = left
        self.right = right
        self.data = data
        self.parent = parent



# main class
class BinaryTree:

    # constructor
    def __init__(self , rootData = None):

        if(rootData != None):
            self.root = Node(rootData)
        else:
            self.root = None

    # function to insert a node into tree
    def insertIntoTree(self , data):

        # if the tree is empty init root
        if(self.root == None):
            self.root = Node(data)

        else:
            currentNode = self.root
            prevNode = None
            
            # get the location were we want to insert the new node
            while(True):

                # if the data is small the it needs to be insert on left
                if(data < currentNode.data):
                    prevNode = currentNode
                    currentNode = currentNode.left

                # else it needs to be insert on rigth
                else:
                    prevNode = currentNode
                    currentNode = currentNode.right

                # if the currentNode becomes None , that is we want to insert the node here
                if(currentNode == None):
                    break

            # init new node
            newNode = Node(data , parent=prevNode)

            # insert the new node on left or right accordingly
            if(data < prevNode.data):
                prevNode.left = newNode
            else:
                prevNode.right = newNode



    # function to do the inoder traversal
    def inOrderTraversal(self , seperator = " , "):
        currentRoot = self.root
        result = ""

        # inner recursive function
        def traverse(currentNode):
            nonlocal result

            # we need to print in this way
            """left , root , rigth"""
            if(currentNode != None):
                traverse(currentNode.left)
                
                result = result + str(currentNode.data) + seperator

                traverse(currentNode.right)

        traverse(currentRoot)

        # remove the last seperator
        result = result[:len(seperator) * -1]

        return result


    
    # function to do the inoder traversal
    def preOrderTraversal(self , seperator = " , "):
        currentRoot = self.root
        result = ""

        # inner recursive function
        def traverse(currentNode):
            nonlocal result

            # we need to print in this way
            """root , left , rigth"""
            if(currentNode != None):
                
                result = result + str(currentNode.data) + seperator

                traverse(currentNode.left)

                traverse(currentNode.right)

        traverse(currentRoot)

        # remove the last seperator
        result = result[:len(seperator) * -1]

        return result

    
    # function to do the inoder traversal
    def postOrderTraversal(self , seperator = " , "):
        currentRoot = self.root
        result = ""

        # inner recursive function
        def traverse(currentNode):
            nonlocal result

            # we need to print in this way
            """left , rigth , root"""
            if(currentNode != None):

                traverse(currentNode.left)

                traverse(currentNode.right)

                result = result + str(currentNode.data) + seperator


        traverse(currentRoot)

        # remove the last seperator
        result = result[:len(seperator) * -1]

        return result

            



# for testing purpose only
if __name__ == "__main__":

    obj = BinaryTree(20)

    obj.insertIntoTree(10)
    obj.insertIntoTree(12)

    obj.insertIntoTree(30)
    obj.insertIntoTree(25)
    obj.insertIntoTree(22)

    obj.insertIntoTree(40)
    obj.insertIntoTree(35)
    obj.insertIntoTree(45)

    print(obj.inOrderTraversal())
    print(obj.preOrderTraversal())
    print(obj.postOrderTraversal())

