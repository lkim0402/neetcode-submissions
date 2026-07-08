class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenSet = {"{":"}", "[":"]", "(":")"}
        i = 0
        if len(s) < 2: return False

        """
        ()[]
        {{}}
        }{
        ([{}])
        once its not in parenSet, we check if its the last elem in stack
        """
        
        for c in s:
            if c in parenSet:
                stack.append(c)
            else:
                if stack and c == parenSet[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
 