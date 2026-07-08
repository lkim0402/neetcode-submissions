class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        l = 0
        res = 0

        # pkpew
        #    r
        #  l
        # r = 3
        # l = 1
        # set = k,p,e
        # res = 3
        for r in range(len(s)):
            # removing duplicates in the set to shrink the substring
            while s[r] in my_set:
                my_set.remove(s[l])
                l += 1
            # adding to set
            my_set.add(s[r])
            res = max(res, len(my_set))
        return res




        


        