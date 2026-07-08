class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """
        hashmap
        {[] the list with count per index (alphabet) : list of words}
        
        using defaultdict:
         A defaultdict automatically creates a default value (in this case, a list) 
         for any new key, so you don’t have to explicitly check if the key already 
         exists in the dictionary before adding to it.
        """
        res = defaultdict(list)
        # not res = {} 

        for s in strs:
            count = [0] * 26
        
            for c in s:
                # we want to map a -> 0, z -> 26
                count[ord(c) - ord("a")] += 1
            
            # we're not just doing res[count] 
            # because lists can't be keys in python
            res[tuple(count)].append(s)
        
        return res.values()

