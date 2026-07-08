import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while (l <= r):
            mid = math.floor((l + r)/2)

            """
            nums = [-1,0,2,4,6,8]
                           l r
            target = 4
            cur = 4
            

            """

            cur = nums[mid]
            if (cur == target):
                return mid
            elif (cur > target):
                r = mid - 1
            else:
                l = mid + 1
            
        return -1