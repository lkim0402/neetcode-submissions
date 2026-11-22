class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while (l <= r):
            midIdx = l + (r - l) // 2
            mid = nums[midIdx]
            if mid < target:
                l = midIdx + 1
            elif mid > target:
                r = midIdx - 1
            else:
                return midIdx
        return -1