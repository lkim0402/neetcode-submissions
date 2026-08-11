class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sortedlist = sorted(candidates)
        res = []
        total = 0
    
        def backtrack(i, sublist, total):
            if total == target:
                res.append(sublist.copy())
                return 
            if i >= len(candidates) or total > target:
                return
            
            cur = sortedlist[i]
            # path 1: just keep doing i + 1
            sublist.append(cur) 
            backtrack(i + 1, sublist, total + cur)

            # path 2: while loop until there is no duplicates found
            sublist.pop()
            while i + 1 < len(sortedlist) and sortedlist[i] == sortedlist[i + 1]:
                i += 1
            backtrack(i + 1, sublist, total)
        
        backtrack(0, [], total)
        return res
