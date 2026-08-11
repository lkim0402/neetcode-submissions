class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sortednums = sorted(nums)
        
        def dfs(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # include
            cur = sortednums[i]
            subset.append(cur)
            dfs(i + 1, subset)

            # exclude
            subset.pop()
            while i + 1 < len(sortednums) and sortednums[i] == sortednums[i + 1]:
                i += 1
            dfs(i + 1, subset)
        
        dfs(0, [])
        return res