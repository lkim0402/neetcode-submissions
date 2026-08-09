class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # go left in the decision tree (add)
            subset.append(nums[i])
            backtrack(i + 1)

            # go right in the decision tree (exclude)
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res