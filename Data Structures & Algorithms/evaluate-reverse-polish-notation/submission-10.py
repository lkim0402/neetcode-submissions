import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        ["1","2","+","3","*","4","-"]
        """
        numStack = []
        for t in tokens:
            if t in "+-*/":
                num1 = numStack.pop()
                num2 = numStack.pop()
                if t == "+":
                    val= num1 + num2
                elif t == "-":
                    val = num2 - num1
                elif t == "/":
                    val = int(float(num2) / num1)
                elif t =="*":
                    val = num1 * num2
                numStack.append(val) 
            else:
                numStack.append(int(t))
        
        return numStack[0]
