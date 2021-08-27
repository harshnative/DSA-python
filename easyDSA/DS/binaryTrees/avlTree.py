# class to init a new node
class Node:
    def __init__(self , data , left=None , right=None , parent=None , frequency = 1):
        self.left = left
        self.right = right
        self.data = data
        self.parent = parent
        self.frequency = frequency



# main class
class AVLTree:

    # constructor
    def __init__(self , rootData = None):

        if(rootData != None):
            self.root = Node(rootData)
        else:
            self.root = None


    def maxDepth(self , node):
        if node is None:
            return 0
    
        else :
    
            # Compute the depth of each subtree
            lDepth = self.maxDepth(node.left)
            rDepth = self.maxDepth(node.right)
    
            # Use the larger one
            if (lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1

    
    def balancingFactorCalc(self , Node):
        """Balancing factor = heigth of left Tree - heigth of right Tree"""

        currentNode = Node

        leftH = 0
        
        leftH = self.maxDepth(currentNode.left)

        rightH = 0
        currentNode = Node

        rightH = self.maxDepth(currentNode.right)


        bFactor  = leftH - rightH

        return bFactor

    

    def checkBalanceFactor(self , insertedNode):
        noneCorrected = True

        nodesList = self.inOrderTraversal()

        for i in nodesList:
            bFactor = self.balancingFactorCalc(i)

            if(bFactor not in [-1,0,1]):
                noneCorrected = False
                self.correctNode(i , insertedNode)

        return noneCorrected
                

    
    def correctNode(self , Node , insertedNode):

        # calculating path to Node from the inserted Node

        currentNode = insertedNode

        # "left , right"
        pathList = []

        while(True):

            if(currentNode.parent.left == currentNode):
                pathList.append("left")
            else:
                pathList.append("right")

            currentNode = currentNode.parent

            if(currentNode == Node):
                break

        pathList.reverse()

        firstTwo = pathList[:2]

        if((firstTwo[0] == "left") and (firstTwo[1] == "left")):
            self.llRotation(Node)
        elif((firstTwo[0] == "right") and (firstTwo[1] == "right")):
            self.rrRotation(Node)
        elif((firstTwo[0] == "left") and (firstTwo[1] == "right")):
            self.lrRotation(Node)
        elif((firstTwo[0] == "right") and (firstTwo[1] == "left")):
            self.rlRotation(Node)
        else:
            raise RuntimeError("could not correct node with path = {}".format(pathList))
            


    
    def llRotation(self , Node):

        parent = Node.parent

        leftChild = Node.left

        if(parent.left == Node):
            parent.left = leftChild
            leftChild.parent = parent

            leftChild.right = Node
            Node.parent = leftChild

            Node.left = None

        elif(parent.right == Node):
            parent.right = leftChild
            leftChild.parent = parent


            leftChild.right = Node
            Node.parent = leftChild

            Node.left = None

        else:
            raise RuntimeError("could not perform LL rotation, parent child dispute found")



    def rrRotation(self , Node):
        parent = Node.parent
        rightChild = Node.right

        if(parent.right == Node):
            parent.right = rightChild
            rightChild.parent = parent

            rightChild.left = Node
            Node.parent = rightChild

            Node.right = None

        elif(parent.left == Node):
            parent.left = rightChild
            rightChild.parent = parent


            rightChild.left = Node
            Node.parent = rightChild

            Node.right = None
        else:
            raise RuntimeError("could not perform RR rotation, parent child dispute found")


    def lrRotation(self , Node):
        parent = Node.parent
        leftChild = Node.left
        left_rightChild = Node.left.right

        if(parent.left == Node):
            parent.left = left_rightChild
            left_rightChild.parent = parent

            left_rightChild.left = leftChild
            leftChild.parent = left_rightChild

            tempNode = left_rightChild.right
            leftChild.right = None

            left_rightChild.right = Node
            Node.parent = left_rightChild

            Node.left = tempNode
            
            if(tempNode != None):
                tempNode.parent = Node
        
        
        elif(parent.right == Node):
            parent.right = left_rightChild
            left_rightChild.parent = parent

            left_rightChild.left = leftChild
            leftChild.parent = left_rightChild

            tempNode = left_rightChild.right
            leftChild.right = None

            left_rightChild.right = Node
            Node.parent = left_rightChild

            Node.left = tempNode
            
            if(tempNode != None):
                tempNode.parent = Node

        else:
            raise RuntimeError("could not perform LR rotation, parent child dispute found")


    def rlRotation(self , Node):
        parent = Node.parent
        rightChild = Node.left
        right_leftChild = Node.left.right

        if(parent.left == Node):
            parent.left = right_leftChild
            right_leftChild.parent = parent

            right_leftChild.right = rightChild
            rightChild.parent = right_leftChild

            tempNode = right_leftChild.right
            rightChild.left = None

            right_leftChild.left = Node
            Node.parent = right_leftChild

            Node.right = tempNode
            
            if(tempNode != None):
                tempNode.parent = Node
        
        
        elif(parent.right == Node):
            parent.right = right_leftChild
            right_leftChild.parent = parent

            right_leftChild.right = rightChild
            rightChild.parent = right_leftChild

            tempNode = right_leftChild.right
            rightChild.left = None

            right_leftChild.left = Node
            Node.parent = right_leftChild

            Node.right = tempNode
            
            if(tempNode != None):
                tempNode.parent = Node


        else:
            raise RuntimeError("could not perform RL rotation, parent child dispute found")



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

            toDoCheck = False
            while(toDoCheck == False):
                toDoCheck = self.checkBalanceFactor(newNode)

            return True



    # function to do the inoder traversal
    def inOrderTraversal(self):
        currentRoot = self.root
        result = []

        # inner recursive function
        def traverse(currentNode):
            nonlocal result

            # we need to print in this way
            """left , root , right"""
            if(currentNode != None):

                traverse(currentNode.left)

                result.append(currentNode)

                traverse(currentNode.right)


        traverse(currentRoot)

        return result


    
    # function to do the pre order traversal
    def preOrderTraversal(self):
        currentRoot = self.root
        result = []

        # inner recursive function
        def traverse(currentNode):
            nonlocal result

            # we need to print in this way
            """root , left , right"""
            if(currentNode != None):
                
                result.append(currentNode)

                traverse(currentNode.left)

                traverse(currentNode.right)

        traverse(currentRoot)

        return result

    
    # function to do the post order traversal
    def postOrderTraversal(self):
        currentRoot = self.root
        result = []

        # inner recursive function
        def traverse(currentNode):
            nonlocal result

            # we need to print in this way
            """left , right , root"""
            if(currentNode != None):

                traverse(currentNode.left)

                traverse(currentNode.right)

                result.append(currentNode)


        traverse(currentRoot)

        return result


    # function to do the inoder traversal
    def inOrderTraversalData(self):
        currentRoot = self.root
        result = []

        # inner recursive function
        def traverse(currentNode):
            nonlocal result

            # we need to print in this way
            """left , root , right"""
            if(currentNode != None):
                traverse(currentNode.left)
                
                result.append(currentNode.data)

                traverse(currentNode.right)

        traverse(currentRoot)

        return result


    
    # function to do the pre order traversal
    def preOrderTraversalData(self):
        currentRoot = self.root
        result = []

        # inner recursive function
        def traverse(currentNode):
            nonlocal result

            # we need to print in this way
            """root , left , right"""
            if(currentNode != None):
                
                result.append(currentNode.data)

                traverse(currentNode.left)

                traverse(currentNode.right)

        traverse(currentRoot)

        return result

    
    # function to do the post order traversal
    def postOrderTraversalData(self):
        currentRoot = self.root
        result = []

        # inner recursive function
        def traverse(currentNode):
            nonlocal result

            # we need to print in this way
            """left , right , root"""
            if(currentNode != None):

                traverse(currentNode.left)

                traverse(currentNode.right)

                result.append(currentNode.data)


        traverse(currentRoot)

        return result


    
    # function to delete a node
    def deleteNode_data(self , data , deleteAll = True , method = "inorder_predecessor"):

        toDelete = None

        # inner recursive function
        # function to traverse a tree and find the the node to delete by comparing the data
        def traverse(currentNode):

            nonlocal toDelete

            if(currentNode != None):
                
                # if the node is found
                if(currentNode.data == data):
                    toDelete = currentNode
                    return
                else:
                    traverse(currentNode.left)

                    # if the node is found in left tree then no need to traverse the right tree
                    if(toDelete == None):
                        traverse(currentNode.right)

        # call the finder function
        traverse(currentNode = self.root)

        return self.deleteNode(toDelete , deleteAll , method)



    # function to delete a node
    def deleteNode(self , node , deleteAll = True , method = "inorder_predecessor"):

        toDelete = node

        # if the node is not found return None
        if(toDelete == None):
            return None

        # if the user does not require to delete the entire node i.e only delete one instance
        if(not(deleteAll) and (toDelete.frequency > 1)):

            # just decreament the frequency
            toDelete.frequency = toDelete.frequency - 1
            return False

        # if the node has 0 child
        if((toDelete.left == None) and (toDelete.right == None)):

            parent = toDelete.parent

            # set the parent left or right to None according to were toDelete is
            if(parent.left == toDelete):
                parent.left = None
            else:
                parent.right = None

            # rm node from memory
            del toDelete

        # if the node as 1 node
        elif((toDelete.left == None) or (toDelete.right == None)):
            
            parent = toDelete.parent

            # if the parent left is node to delete
            if(parent.left == toDelete):

                # then set the toDelete's child as parent left
                if(toDelete.left != None):
                    parent.left = toDelete.left
                    toDelete.left.parent = parent
                else:
                    parent.left = toDelete.right
                    toDelete.right.parent = parent



            else:
                # then set the toDelete's child as parent right
                if(toDelete.left != None):
                    parent.right = toDelete.left
                    toDelete.left.parent = parent

                else:
                    parent.right = toDelete.right
                    toDelete.right.parent = parent


            del toDelete


        # if the node as two childs
        else:

            # find the largest from left - inorder_predecessor
            if(method == "inorder_predecessor"):

                currentNode = toDelete.left

                whileLoop = False

                # finding the largest from left i.e go to left and then right right right
                while(currentNode.right != None):
                    currentNode = currentNode.right
                    whileLoop = True


                currentNodeData = currentNode.data
                currentNodeParent = currentNode.parent

                # remove the largest node from its parent
                # if we traversed while loop even one time means the smallest node is on right side
                if(whileLoop):
                    currentNodeParent.right = None
                else:
                    currentNodeParent.left = None

                # copy the largest node data to the node to delete
                toDelete.data = currentNodeData

                del currentNode

            else:
                currentNode = toDelete.right
                whileLoop = False

                # finding the smallest from right - inorder_successor i.e go to right and then left left left
                while(currentNode.left != None):
                    whileLoop = True
                    currentNode = currentNode.left

                currentNodeData = currentNode.data
                currentNodeParent = currentNode.parent

                # remove the smallest node from its parent
                # if we traversed while loop even one time means the smallest node is on left side
                if(whileLoop):
                    currentNodeParent.left = None
                else:
                    currentNodeParent.right = None

                # copy the smallest node data to the node to delete
                toDelete.data = currentNodeData

                del currentNode

        return True


    # function to return a node object 
    def returnNode(self , data):
        node = None

        # inner recursive function
        # function to traverse a tree and find the the node to return by comparing the data
        def traverse(currentNode):

            nonlocal node

            if(currentNode != None):
                
                # if the node is found
                if(currentNode.data == data):
                    node = currentNode
                    return
                else:
                    traverse(currentNode.left)

                    # if the node is found in left tree then no need to traverse the right tree
                    if(node == None):
                        traverse(currentNode.right)

        # call the finder function
        traverse(currentNode = self.root)

        return node




            



# for testing purpose only
if __name__ == "__main__":

    obj = AVLTree()

    obj.insertIntoTree(14)
    obj.insertIntoTree(17)
    obj.insertIntoTree(11)
    obj.insertIntoTree(7)
    obj.insertIntoTree(53)
    obj.insertIntoTree(4)
    obj.insertIntoTree(13)
    obj.insertIntoTree(12)
    obj.insertIntoTree(4)
    obj.insertIntoTree(8)
    obj.insertIntoTree(13)
    obj.insertIntoTree(60)
    obj.insertIntoTree(19)
    obj.insertIntoTree(16)
    obj.insertIntoTree(20)



    for i in obj.inOrderTraversal():
        try:
            print( i.data , i.parent.data)
        except AttributeError:
            print(i.data , None)

    print(obj.returnNode(16))

