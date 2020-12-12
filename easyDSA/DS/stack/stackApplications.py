from stack import StackUsingLinkedList , stackOperations

class stackApplications:

    # method to check for balanced paranthesis
    @classmethod
    def balancedParanthesis(cls , string):

        sll = StackUsingLinkedList()

        string = str(string)

        for i,j in enumerate(string):

            # if the opening bracket is found then push it
            if((j == "(") or (j == "[") or (j == "{")):
                sll.push(j)

            # if closing bracket is found then compare it to stack top
            elif(j == ")"):
                data = sll.pop()

                if(data[0] != "("):
                    return i

            elif(j == "]"):
                data = sll.pop()

                if(data[0] != "["):
                    return i

            elif(j == "}"):
                data = sll.pop()

                if(data[0] != "{"):
                    return i
                
            else:
                pass
        
        return None


    # method to convert the infix expression to post fix expression
    @classmethod
    def infixToPostfix(cls , infixExpression):

        # expression should have balanced parenthesis
        if(cls.balancedParanthesis(infixExpression) != None):
            raise Exception("invalid expression passed , parenthesis are not balanced")



        """ scan from left to right
            if operand , output it

            else

                if stack empty push it
                elif top of stack is "(" then push it
                elif scanned = "("
                elif scanned = ")" , pop until "(" and remove both bracket
                elif precedence order of scanned is greator than predence order of peek() , push it
                else  while stack is not empty - peek - if peek = "(" break , elif precedence of peek is greator than or equal to predence of scanned pop() and output

            empty stack  
        """

        sll = StackUsingLinkedList()

        result = ""

        # presedence order of opeartors
        precedence = {'+' : 1 , 
                      '-' : 1 ,
                      '*' : 2 ,
                      '/' : 2 , 
                      '^' : 3 ,}


        for i in infixExpression:

            # if operand
            if((precedence.get(i , None) == None) and (i != "(") and (i != ")")):
                result = result + i
            
            else:

                if(sll.isEmpty()):
                    sll.push(i)
                
                # if stack top is "("
                elif(sll.peek()[0] == "("):
                    sll.push(i)

                elif(i ==  "("):
                    sll.push(i)

                # pop till "(" is encountered 
                elif(i ==  ")"):
                    
                    while(not(sll.isEmpty())):
                        
                        data = sll.peek()[0]
                        
                        if(data == "("):

                            # as the "(" is to be also removed
                            sll.pop()
                            break

                        result = result + str(data)

                        sll.pop()

                elif(precedence.get(i) > precedence.get(sll.peek()[0])):
                    sll.push(i)
                
                else:

                    while(not(sll.isEmpty())):
                        
                        data = sll.peek()[0]

                        if(data == "("):
                            break

                        elif(precedence.get(data) >= precedence.get(i)):

                            result = result + data

                            sll.pop()
                        
                        else:
                            break

                    sll.push(i)

        while(not(sll.isEmpty())):

            result = result + sll.pop()[0]

        return result 

    

    # method to evaluate the postfix expression
    # if more than single digit numbers as to be passed then all the numbers and operands must be seperated by space
    @classmethod
    def postfixEvaluator(cls , postfixExpression):

        sll = StackUsingLinkedList()

        # if the multidigit is passed the the expression is converted to a list
        if(" " in postfixExpression):
            postfixExpression = postfixExpression.split()

        """ scan 
            if isnumeric , push
            elif x = pop , y = pop , eval y (i) x
        """

        for i in postfixExpression:

            if(i.isnumeric()):
                sll.push(i)

            else:
                x = sll.pop()[0]
                y = sll.pop()[0]

                sll.push(str(eval(y + i + x)))

        return int(sll.pop()[0])


    # function to get the next greator elements for a array
    @classmethod
    def nextGreatorElement(cls , array):

        """
        Algo - 
        Push the first element to stack.
        Pick rest of the elements one by one and follow the following steps in loop.
            Mark the current element as next.
            If stack is not empty, compare top element of stack with next.
            If next is greater than the top element,Pop element from stack. next is the next greater element for the popped element.
            Keep popping from the stack while the popped element is smaller than next. next becomes the next greater element for all such popped elements
        Finally, push the next in the stack.
        After the loop in step 2 is over, pop all the elements from stack and print -1 as next element for them.
        """

        sll = StackUsingLinkedList()

        resultList = []

        sll.push(array[0])

        for i in array[1:]:
            next = i

            while(True):
                if(not(sll.isEmpty())):
                    if(next > sll.peek()[0]):
                        resultList.append([sll.pop()[0] , next])
                    else:
                        break
                else:
                    break
            
            sll.push(next)

        while(not(sll.isEmpty())):
            resultList.append([sll.pop()[0] , -1])

        return resultList



        



                










if __name__ == "__main__":
    
    # print(stackApplications.infixToPostfix("a + b * c"))
    # print(stackApplications.postfixEvaluator("10 20 30 * +"))
    print(stackApplications.infixToPostfix("(A – B) / (C * D) ^ (E + F * G)"))
    




