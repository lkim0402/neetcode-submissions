class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        total = 0

        def backtracking(i, subset, total):
            # base case
            if total == target: 
                res.append(subset.copy())
                return
            if i >= len(nums) or total > target:
                return
                        
            cur = nums[i]

            # retain the index
            subset.append(cur)
            backtracking(i, subset, total + cur)

            # move the index
            subset.pop()
            backtracking(i + 1, subset, total)
        
        backtracking(0, [], 0)
        return res