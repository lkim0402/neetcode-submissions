class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")

        final = "".join(encoded)
        print(final)
        return final

    """
    ["neet","code","love","you"]
    "4#neet4#code4#love3#you"
    """

    def decode(self, s: str) -> List[str]:
        
        i = 0
        str_len = 0
        ans = []
        while i < len(s):
            
            num = ""
            # looping over the num until we see #
            while s[i] != "#":
                num += s[i]
                i += 1
            
            i += 1 # to move beyond the #
            print(f"i: {i}")
            print(f"num: {num}")
            """
            ["neet","code","love","you"]
            "4#neet4#code4#love3#you"
             012345
               i
            """     
            str_len = int(num) # convert num string to int
            word = s[i:i+str_len]
            print(f"str_len: {str_len}")
            print(f"word: {word}")
            i += str_len
            ans.append(word)


        return ans
