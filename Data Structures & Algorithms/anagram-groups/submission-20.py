class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        {
            tuple([1,1,2]) = ["/", "ccab"]
            ....
            tuple([2,1,2]) = ["aabcc", "cacab"]
        }
        """

        freq = defaultdict(list)

        for s in strs:
            count = [0] * 26 
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            freq[tuple(count)].append(s)
        
        return list(freq.values())
