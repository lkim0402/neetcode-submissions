class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)

        for s in strs:
            # get the alpha num count
            a = [0] * 26
            for c in s:
                a[ord(c) - ord('a')] += 1
            
            # if a not in freq:
            freq[tuple(a)].append(s)
        
        res = list(freq.values())
        return res
