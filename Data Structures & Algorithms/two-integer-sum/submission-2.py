class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # target = 10
        # 1 4 5 6
        # ^
        #   ^

        list = []

        # Easy solution: 2 for loops
        # for i in range(len(nums)):
        #     for j in range(1, len(nums)):
        #         if (nums[i] + nums[j] == target):
        #             list.append(i)
        #             list.append(j)
        #     break

        # More efficient solution
        # key: int, value: index

        dict = {}

        for i, n in enumerate(nums):
            num = target - n 
            if (num in dict):
                return [dict[num], i] #you wanna return the 2 indexes

            dict[n] = i
