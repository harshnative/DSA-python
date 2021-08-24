# class to init a new node
class Node:
    def __init__(self , data , left=None , right=None , parent=None , frequency = 1):
        self.left = left
        self.right = right
        self.data = data
        self.parent = parent
        self.frequency = frequency



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

                # else it needs to be insert on right
                elif(data > currentNode.data):
                    prevNode = currentNode
                    currentNode = currentNode.right

                
                # if the data is already in table , increase the frequency
                else:
                    currentNode.frequency = currentNode.frequency + 1
                    return False

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

            return True



    # function to do the inoder traversal
    def inOrderTraversal(self , seperator = " , "):
        currentRoot = self.root
        result = ""

        # inner recursive function
        def traverse(currentNode):
            nonlocal result

            # we need to print in this way
            """left , root , right"""
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
            """root , left , right"""
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
            """left , right , root"""
            if(currentNode != None):

                traverse(currentNode.left)

                traverse(currentNode.right)

                result = result + str(currentNode.data) + seperator


        traverse(currentRoot)

        # remove the last seperator
        result = result[:len(seperator) * -1]

        return result


    
    # function to delete a node
    def deleteNode_data(self , data , deleteAll = True , method = "inorder_predecessor"):

        toDelete = None

        # inner recursive function
        def traverse(currentNode):

            nonlocal toDelete

            if(currentNode != None):
                
                if(currentNode.data == data):
                    toDelete = currentNode
                    return
                else:
                    traverse(currentNode.left)
                    if(toDelete == None):
                        traverse(currentNode.right)

        traverse(currentNode = self.root)

        if(toDelete == None):
            return None

        if((toDelete.left == None) and (toDelete.right == None)):
            parent = toDelete.parent

            if(parent.left == toDelete):
                parent.left = None
            else:
                parent.right = None

            del toDelete

        elif((toDelete.left == None) or (toDelete.right == None)):
            parent = toDelete.parent

            if(parent.left == toDelete):
                if(toDelete.left != None):
                    parent.left = toDelete.left
                else:
                    parent.left = toDelete.right

            else:
                if(toDelete.left != None):
                    parent.right = toDelete.left
                else:
                    parent.right = toDelete.right

            del toDelete

        else:

            if(method == "inorder_predecessor"):
                largest = None

                currentNode = self.root.left

                while(currentNode.right != None):

                    largest = currentNode
                    currentNode = currentNode.right

                currentNodeData = currentNode.data

                currentNodeParent = currentNode.parent

                currentNodeParent.right = None

                toDelete.data = currentNodeData

                del currentNode

            else:
                smallest = None

                currentNode = self.root.right

                while(currentNode.left != None):

                    largest = currentNode
                    currentNode = currentNode.left

                currentNodeData = currentNode.data

                currentNodeParent = currentNode.parent

                currentNodeParent.left = None

                toDelete.data = currentNodeData

                del currentNode







            



# for testing purpose only
if __name__ == "__main__":

    obj = BinaryTree()

    obj.insertIntoTree(11)
    obj.insertIntoTree(6)
    obj.insertIntoTree(4)
    obj.insertIntoTree(5)
    obj.insertIntoTree(9)
    obj.insertIntoTree(10)
    obj.insertIntoTree(20)
    obj.insertIntoTree(17)
    obj.insertIntoTree(42)
    obj.insertIntoTree(30)
    obj.insertIntoTree(50)







    print(obj.inOrderTraversal())
    print(obj.preOrderTraversal())
    print(obj.postOrderTraversal())

    obj.deleteNode_data(11 , method="inorder_successor")

    print()

    print(obj.inOrderTraversal())
    print(obj.preOrderTraversal())
    print(obj.postOrderTraversal())

