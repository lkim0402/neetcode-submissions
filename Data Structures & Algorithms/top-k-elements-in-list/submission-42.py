class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        [1,2,2,3,3,3]
        {
        1:1,
        2:2,
        3:3
        }

        [[1],[],[2],[3],[],[],[]]
          0   1  2   3   4  5  6 count
        """

        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        count = [[] for _ in range(len(nums)+1)]
        for num,v in freq.items():
            count[v].append(num)
        
        res = []
        for i in range(len(count)-1, -1, -1):
            l = count[i]
            while l and k > 0:
                res.append(l.pop())
                k -= 1
        
        return res
