class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set(nums)

        # 1,2,3,4,5
        for n in nums:
            if n - 1 not in s:
                seq = 1
                while n + 1 in s:
                    seq += 1
                    n += 1
                res = max(res, seq)
        
        return res