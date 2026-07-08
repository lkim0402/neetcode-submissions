class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """

        dict of dicts
        word : dict => 
        str_dict = {{h:1, a:1, t:1}:[], {a:1,c:1,t:1}:[], ...}

        list_ans = []

        1. iterate through strs
            - anagram = #make anagram
            - check if anagram exists in str_dict
                - if not
                    - str_dict[anagram].append([str])
                - if yes
                    - find the value in the list
                    - add str to list
        """

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)

        return res.values()


