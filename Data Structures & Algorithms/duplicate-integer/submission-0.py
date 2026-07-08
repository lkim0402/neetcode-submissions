class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:   
        num = len(nums)
        for i in range(num):
            for j in range(i + 1, num):
                if (nums[i] == nums[j]):
                    return True
        
        return False
        