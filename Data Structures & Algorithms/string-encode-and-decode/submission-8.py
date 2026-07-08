# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         encoded = ""
#         for s in strs:
#             encoded += f"{len(s)}#{s}"
#         return encoded

#     """
#     ["neet","code","love","you"]
#     "4#neet4#code4#love3#you"
#     """

#     def decode(self, s: str) -> List[str]:     
        
#         i = 0
#         str_len = 0
#         ans = []
#         while i < len(s):
            
#             num = ""
#             # looping over the num until we see #
#             while s[i] != "#":
#                 num += s[i]
#                 i += 1
             
#             # convert num string to int, (ex. "6" -> 6)
#             str_len = int(num) 

#             # to move beyond the #
#             i += 1 

#             # get the word & append it
#             word = s[i:i+str_len]
#             ans.append(word)

#             # move i to past the string (to the next number)
#             i += str_len

#         return ans

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for st in strs:
            s = "\""
            for c in st:
                if c == "\"":
                    s += "\\\""
                elif c == "\\":
                    s += "\\\\"
                else:
                    s += c
            result += s + "\""
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        opened = False
        escaped = False
        buf = ""
        for c in s:
            if c == "\\":
                escaped = True
            elif escaped:
                buf += "\\" + c
                escaped = False
            elif not opened and c == "\"":
                opened = True
            elif opened and c == "\"":
                result.append(buf)
                buf = ""
                opened = False
            else:
                buf += c
        return result