class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} # num: index
        for idx, n in enumerate(nums):
            val = target - n
            if val in d:
                return [d[val], idx]
            d[n] = idx