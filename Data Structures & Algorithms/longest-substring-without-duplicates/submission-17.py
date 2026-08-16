class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        p = 0 # pointer
        res = 0

        for cur in range(len(s)):
            while s[cur] in charSet:
                charSet.remove(s[p])
                p += 1
                # p will always catch up to be after cur
            charSet.add(s[cur])
            res = max(res, len(charSet))

        return res

        


        