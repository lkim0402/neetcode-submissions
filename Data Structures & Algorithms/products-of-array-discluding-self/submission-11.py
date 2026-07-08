class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        """
        [1,0,9,1] -> [0,9,0,0]
        [0,8,0] -> [0,0,0]
        [0,0] -> [0,0]

        0 zero
        1 zero
        2+ zeroes
        """
        prod = 1
        zero_count = 0
        num_list = []
        for num in nums:
            if num != 0:
                prod = prod * num
            else:
                zero_count += 1
        
        for num in nums:
            if zero_count > 1:
                num_list.append(0)
            elif zero_count == 1:
                if num == 0:
                    num_list.append(prod)
                else:
                    num_list.append(0)
            else:
                num_list.append(prod // num)

        return num_list
        
        return num_list

