class Solution:
    def isPalindrome(self, s: str) -> bool:

        start = 0
        back = len(s) - 1

        # s =

        while (start < back):
            valid = True
            if not s[start].isalnum():
                start += 1
                valid = False
            if not s[back].isalnum():
                back -= 1
                valid = False
            if valid:
                if s[start].lower() != s[back].lower():
                    return False
                else:
                    start += 1
                    back -= 1

        return True
        