import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while (l <= r):
            mid = math.floor((l + r)/2)

            """
            [9,10,11,12]
             l    r
            """

            cur = nums[mid]
            if (cur == target):
                return mid
            elif (cur > target):
                r = mid - 1
            else:
                l = mid + 1
            
        return -1