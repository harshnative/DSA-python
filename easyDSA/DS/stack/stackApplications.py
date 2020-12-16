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

                if(data != "("):
                    return i + 1 

            elif(j == "]"):
                data = sll.pop()

                if(data != "["):
                    return i + 1 

            elif(j == "}"):
                data = sll.pop()

                if(data != "{"):
                    return i + 1
                
            else:
                pass

        if(stackOperations.getLength(sll) != 0):
            return len(string)
        
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
                result = result + i + " "
            
            else:

                if(sll.isEmpty()):
                    sll.push(i)
                
                # if stack top is "("
                elif(sll.peek() == "("):
                    sll.push(i)

                elif(i ==  "("):
                    sll.push(i)

                # pop till "(" is encountered 
                elif(i ==  ")"):
                    
                    while(not(sll.isEmpty())):
                        
                        data = sll.peek()
                        
                        if(data == "("):

                            # as the "(" is to be also removed
                            sll.pop()
                            break

                        result = result + str(data) + " "

                        sll.pop()

                elif(precedence.get(i) > precedence.get(sll.peek())):
                    sll.push(i)
                
                else:

                    while(not(sll.isEmpty())):
                        
                        data = sll.peek()

                        if(data == "("):
                            break

                        elif(precedence.get(data) >= precedence.get(i)):

                            result = result + data + " "

                            sll.pop()
                        
                        else:
                            break

                    sll.push(i)

        while(not(sll.isEmpty())):
            result = result + sll.pop() + " "

        return result 


    
    # method to convert the infix expression to post fix expression
    @classmethod
    def infixToPostfix2(cls , infixExpression):

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

            
        infixExpression = infixExpression.split(" ")

        print(infixExpression)
        input()


        for i in infixExpression:

            # if operand
            if((precedence.get(i , None) == None) and (i != "(") and (i != ")")):
                result = result + i + " "
            
            else:

                if(sll.isEmpty()):
                    sll.push(i)
                
                # if stack top is "("
                elif(sll.peek() == "("):
                    sll.push(i)

                elif(i ==  "("):
                    sll.push(i)

                # pop till "(" is encountered 
                elif(i ==  ")"):
                    
                    while(not(sll.isEmpty())):
                        
                        data = sll.peek()
                        
                        if(data == "("):

                            # as the "(" is to be also removed
                            sll.pop()
                            break

                        result = result + str(data) + " "

                        sll.pop()

                elif(precedence.get(i) > precedence.get(sll.peek())):
                    sll.push(i)
                
                else:

                    while(not(sll.isEmpty())):
                        
                        data = sll.peek()

                        if(data == "("):
                            break

                        elif(precedence.get(data) >= precedence.get(i)):

                            result = result + data + " "

                            sll.pop()
                        
                        else:
                            break

                    sll.push(i)

        while(not(sll.isEmpty())):
            result = result + sll.pop() + " "

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
            stackOperations.traverse(sll)

            # if the string is decimal or floating point number
            if((i.isdecimal()) or (i.replace('.', '', 1).isdigit())):
                sll.push(i)

            else:
                x = sll.pop()
                y = sll.pop()

                sll.push(str(eval(y + i + x)))

        return float(sll.pop())


    # method to convert the infix expression to prefix expression
    @classmethod
    def infixToPrefix(cls , infixExpression):

        result = ""

        for i in infixExpression[::-1]:

            if(i == "("):
                result = result + ")"
            elif(i == ")"):
                result = result + "("
            else:
                result = result + str(i)

        tempExp = cls.infixToPostfix(result)

        postfixExp = tempExp[::-1]

        return postfixExp


    
    # method to convert the infix expression to prefix expression
    @classmethod
    def infixToPrefix2(cls , infixExpression):

        result = ""

        infixExpression = infixExpression.split(" ")

        for i in infixExpression[::-1]:

            if(i == "("):
                result = result + ")" + " "
            elif(i == ")"):
                result = result + "(" + " "
            else:
                result = result + str(i) + " "

        tempExp = cls.infixToPostfix(result)

        tempExp = tempExp.split(" ")

        postfixExp = ""

        for i in tempExp[::-1]:
            if(i != ""):
                postfixExp = postfixExp + str(i) + " "

        return postfixExp





    
        



                










if __name__ == "__main__":
    # print(stackApplications.balancedParanthesis("[[()]"))
    print(stackApplications.infixToPostfix2("7 ^ 2 * ( 25 + 10 / 5 ) - 13"))
    print(stackApplications.postfixEvaluator("7 2 ^ 25 10 5 / + * 13 -"))
    # print(stackApplications.infixToPostfix("(A – B) / (C * D) ^ (E + F * G)"))
    # print(stackApplications.infixToPrefix2("78 + ( 30 - 0.5 ( 28 + 8 ) ) / 6"))
    




