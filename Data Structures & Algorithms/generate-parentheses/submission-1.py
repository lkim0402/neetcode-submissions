class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def dfs(opened, closed, stack):
            if closed == opened == n:
                res.append("".join(stack))
                return
            
            # add (
            if opened < n:
                stack.append("(")
                dfs(opened + 1, closed, stack)
                stack.pop()

            # add )
            if closed < opened:
                stack.append(")")
                dfs(opened, closed + 1, stack)
                stack.pop()

        dfs(0,0,stack)
        return res