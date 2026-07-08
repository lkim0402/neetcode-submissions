class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        """
        [1,0,9,1] -> [0,9,0,0]
        [0,8,0] -> [0,0,0]
        [0,0] -> [0,0]

        0 zero -> prod // num (in loop)
        1 zero -> output is all 0s except where 0 is
        2+ zeroes -> output is all 0s
        """
        # prod = 1
        # zero_count = 0
        # num_list = []
        # for num in nums:
        #     if num != 0:
        #         prod = prod * num
        #     else:
        #         zero_count += 1
        
        # for num in nums:
        #     if zero_count > 1:
        #         num_list.append(0)
        #     elif zero_count == 1:
        #         if num == 0:
        #             num_list.append(prod)
        #         else:
        #             num_list.append(0)
        #     else:
        #         num_list.append(prod // num)

        """
        W/o using the division operator
        """

        result = [1] * len(nums)
        
        # [1,4,3,5]
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix # result = [1,1,4,12]
            prefix *= nums[i] #prefix = 70

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            result[i] *= postfix #result = [60,15,20,12]
            postfix *= nums[i] #postfix = 60

        return result

