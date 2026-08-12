class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(opened, closed, path):
            if closed == opened == n:
                res.append(path)
                return
            
            # add (
            if opened < n:
                dfs(opened + 1, closed, path + "(")

            # add )
            if closed < opened <= n:
                dfs(opened, closed + 1, path + ")")

        dfs(0,0,"")
        return res