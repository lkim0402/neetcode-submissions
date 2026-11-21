class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            "]":"[",
            "}":"{",
            ")":"("
        }

        for c in s:
            if c in "[{(": # opening
                stack.append(c)
            else: # closing
                if not stack:
                    return False
                p = stack.pop()
                if d[c] != p:
                    return False
        
        return not stack