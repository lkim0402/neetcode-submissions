class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
            # example: "4#book"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 #index of char
        
        while i < len(s):
            j = i
            while s[j] != "#": #getting the length of the word
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            #j is the delimiter character '#', so we start with j+1

            i = j + 1 + length
        
        return res
