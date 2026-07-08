class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        l = 0
        longest = 0
        # s = "xzyzxyz"
        #         r
        #        l
        # my_set = {y}

        for r in range(len(s)):
            # some code that cleans up the set when theres duplicate
            while s[r] in my_set:
                my_set.remove(s[l])
                l += 1
            
            my_set.add(s[r])
            longest = max(longest, len(my_set))
        
        return longest

