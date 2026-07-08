class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        ["act","pots","tops","cat","stop","hat"]

        list of dictionaries
        [{a:1, c:1, t:1}, {p:1, o:1, t:1, s:1}]

        ans = [[]]
        1st word "act"
        -> create dict: {a:1, c:1, t:1}
        -> check if dict exists,
            -> yes: get the index of dict 
            -> no: add to array [{a:1, c:1, t:1}]
                -> get current index = 0
                -> add to ans[0]

        2nd word "cat"
        -> create dict: [{a:1, c:1, t:1}]
        -> check if dict exists,
            -> yes: get the index of dict ( 0 in this case)
                -> add word to ans[0]
                    -> if ans[0] == null
                        -> ans[0] = [word]
                    -> else
                        -> ans[0].append(word)
            -> no: add to array [{a:1, c:1, t:1}]
        """

        check = [] # list of dicts
        ans = []

        for i, word in enumerate(strs):
            count_set = {}
            for c in word:
                count_set[c] = count_set.get(c, 0) + 1
            
            print(count_set)

            if count_set in check:
                index = check.index(count_set)
                # if ans[index] != null:
                #     ans[index].append(word)
                # else:
                #     ans[index] == [word]
                ans[index].append(word)
            else:
                check.append(count_set)
                ans.append([word])
        
        return ans
                

