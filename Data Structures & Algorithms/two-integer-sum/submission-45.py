class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        [3,4,5,6]
        {0:3, 1:4, 2:5, 3:6}

        """
        a = {}
        for i, n in enumerate(nums):
            a[n] = i # it will hold the most recent index (highest)
            
        print(a)

        for i, n in enumerate(nums):
            num = target - n
            if num in a and a[num] != i:
                return [i, a[num]]
