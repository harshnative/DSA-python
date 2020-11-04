from stack import StackUsingLinkedList

class stackApplications:

    @classmethod
    def balancedParathesis(cls , string):

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


if __name__ == "__main__":
    
    print(stackApplications.balancedParathesis("[[]{}}]"))




