class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # num : count
        numCount = {}
        for n in nums:
            numCount[n] = numCount.get(n, 0) + 1
            if numCount[n] > (len(nums)/2):
                return n
        
        # for k,v in numCount.items():
        #     if v > (len(nums)/2):
        #         return k
        
        return 0