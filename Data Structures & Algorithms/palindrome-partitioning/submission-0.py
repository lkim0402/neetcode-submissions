class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(start):
            if start == len(s):
                res.append(part.copy())
                return
            
            for end in range(start, len(s)):
                cur = s[start: end + 1]
                if self.isPali(cur):
                    # if substring is a palindrome do dfs
                    part.append(cur)
                    dfs(end + 1)
                    part.pop()
        dfs(0)
        return res
    
    def isPali(self, substring):
        l,r = 0, len(substring) - 1
        while l < r:
            if substring[l] != substring[r]:
                return False
            l += 1
            r -= 1
        return True
