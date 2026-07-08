class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        [1, 2, 3, 10, 11, 12]
        ->
        {1, 2, 3, 10, 11, 12}
        """
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # check if start of sequence
            if num - 1 not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest