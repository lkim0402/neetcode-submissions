class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
        9 8 6 1
        0 1 2 3 -> length 4
        """

        index = []
        dict_num = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in dict_num:
                index.append(dict_num[diff])
                index.append(i)
            dict_num[num] = i
            
        return index