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

            if(parent != None):

                # set the parent left or rigth to None according to were toDelete is
                if(parent.left == toDelete):
                    parent.left = None
                else:
                    parent.right = None

            else:
                self.root = None

            # rm node from memory
            del toDelete

        # if the node as 1 node
        elif((toDelete.left == None) or (toDelete.right == None)):
            
            parent = toDelete.parent

            if(parent != None):

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

            else:
                # then set the toDelete's child as parent left
                if(toDelete.left != None):
                    self.root = toDelete.left
                    self.root.parent = None
                else:
                    self.root = toDelete.right
                    self.root.parent = None

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

    # obj = BinaryTree()

    # obj.insertIntoTree(11)
    # obj.insertIntoTree(6)
    # obj.insertIntoTree(4)
    # obj.insertIntoTree(5)
    # obj.insertIntoTree(9)
    # obj.insertIntoTree(10)
    # obj.insertIntoTree(20)
    # obj.insertIntoTree(17)
    # obj.insertIntoTree(42)
    # obj.insertIntoTree(30)
    # obj.insertIntoTree(50)







    # print(obj.inOrderTraversalData())
    # print(obj.preOrderTraversalData())
    # print(obj.postOrderTraversalData())

    # print()

    # for i in obj.inOrderTraversal():
    #     try:
    #         print( i.data , i.parent.data)
    #     except AttributeError:
    #         print(i.data , None)

    # print()

    # obj.deleteNode_data(11 , method="inorder_successor")
    # obj.deleteNode_data(9 , method="inorder_predecessor")
    # obj.deleteNode_data(42 , method="")

    # print()

    # print(obj.inOrderTraversalData())
    # print(obj.preOrderTraversalData())
    # print(obj.postOrderTraversalData())

    # print()

    # for i in obj.inOrderTraversal():
    #     try:
    #         print( i.data , i.parent.data)
    #     except AttributeError:
    #         print(i.data , None)

    # print()

    # print(obj.returnNode(5).parent.data)






    uperror = 0
    delerror = 0
    import random
    import copy

    for i in range(1000):

        obj = BinaryTree()

        added = []

        for j in range(100):
            randomNo = random.randint(0,100)
            print("\rj = {}".format(j) , end="")
            obj.insertIntoTree(randomNo)
            
            if(randomNo not in added):
                added.append(randomNo)

            resultList = sorted(obj.inOrderTraversalData())
            added = sorted(added)

            if(resultList != added):
                uperror = uperror + 1

        
        for k in list(range(len(added))):
            delRes = obj.deleteNode_data(added[k])

            resultList = sorted(obj.inOrderTraversalData())
            delAdded = sorted(added[k+1:])

            # print()
            if((resultList != delAdded) or (delRes != True)):
                delerror = delerror + 1

        print("\n")
        print(i, uperror , delerror)



