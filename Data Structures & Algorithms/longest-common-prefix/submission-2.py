class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]

        prefix = ""
        for i, cur in enumerate(word):
            # iterate thru each word
            for w in strs:
                if (i > len(w) - 1 or w[i] 
                != cur):
                    return prefix
            prefix += cur
        
        return prefix