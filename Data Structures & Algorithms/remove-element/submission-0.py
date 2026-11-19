class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        count = 0
        for i,n in enumerate(nums):
            if n == val:
                nums[i] = "_"
                count += 1
            
        l, r = 0, len(nums) - 1
        while (l < r):
            if nums[r] == "_":
                r -= 1
            else:
                if nums[l] == "_":
                    nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
        return len(nums) - count
