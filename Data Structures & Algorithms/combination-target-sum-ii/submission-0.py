class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sortedlist = sorted(candidates)
        res = []

        def dfs(i, subset, total):
            # base case
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur = sortedlist[i]
            subset.append(cur)
            dfs(i + 1, subset, total + cur)

            subset.pop()
            while i + 1 < len(sortedlist) and sortedlist[i] == sortedlist[i + 1]:
                i += 1
            dfs(i + 1, subset, total)

        dfs(0,[],0)
        return res