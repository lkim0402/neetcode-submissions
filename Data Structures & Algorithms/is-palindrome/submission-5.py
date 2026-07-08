class Solution:
    def isPalindrome(self, s: str) -> bool:

        start = 0
        back = len(s) - 1

        while (start < back):
            if not s[start].isalnum():
                start += 1
                continue
            if not s[back].isalnum():
                back -= 1
                continue
            
            if s[start].lower() != s[back].lower():
                return False
            # else: # only move when its valid
            start += 1
            back -= 1

        return True
        