class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        [1,2,4,6]
        [1,1,2,8]
        [48,24,12,8]
        """
        ans = [1] #default
        pre = 1

        # first storing the prefix mult
        for i in range(len(nums) - 1):
            pre *= nums[i]
            ans.append(pre)
        
        post = 1

        # now replacing the prefix mult values
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= post
            post *= nums[i]

        return ans

