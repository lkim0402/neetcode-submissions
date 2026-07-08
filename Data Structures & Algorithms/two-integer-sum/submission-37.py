class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
        1. Create new list to store the answer
        2. Make a duplicate copy of list -> dict named dup_dict
            - key:value => num:index
        3. Loop through the original list
            - if current num - target is in dup_dict
                return num index and value from dup_dict
            - add the values in list from 1
            - return
        """

        #1
        ans = []

        #2
        dup_dict = {}
        for index, num in enumerate(nums):
            dup_dict[num] = index
        
        for index, num in enumerate(nums):
            dict_num = target - num
            # ensure i != j
            if (dict_num) in dup_dict and dup_dict[dict_num] != index:
                ans.append(index)
                ans.append(dup_dict[dict_num])
                break
        
        return ans


        """
        Official answer (wtf?)
        """
        
            