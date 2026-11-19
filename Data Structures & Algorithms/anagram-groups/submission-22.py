class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """
        dictionary
        "11100...." : ["abc", "cba", "acb"]
        """

        d = defaultdict(list)
        res = []
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            d[tuple(key)].append(s)
        
        for v in d.values():
            res.append(v)
        
        return res