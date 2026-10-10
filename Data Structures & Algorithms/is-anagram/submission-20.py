class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False
        
        counta = {}
        countb = {}

        for string in s:
            counta[string] = counta.get(string, 0) + 1
        
        for string in t:
            countb[string] = countb.get(string, 0) + 1
        
        print(f"counta: {counta}")
        print(f"countb: {countb}")

        return counta == countb