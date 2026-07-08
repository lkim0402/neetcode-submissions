class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0] * len(temperatures)
        stack = [] # holds pairs: [temp, index]

        """
            [30,38,30,36,35]
        stack= [[]]
        ans [0,0,0,0,0]
        """
        
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, ind = stack.pop()
                ans[ind] = (i - ind)
            stack.append([t,i])
        
        return ans