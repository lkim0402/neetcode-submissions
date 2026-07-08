class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
             1   2   3  4
        pre  1   1   2  6
        post 24  12  4  1
             24  12  8  6

             1    2    3  4
        pre  24   12   8  6
        post = 24
        """

        ans = []
        # post = []
        prefix = 1
        postfix = 1

        for n in nums:
            ans.append(prefix)
            prefix = n * prefix
        
        print(ans)
        
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        
        print(ans)
        return ans

