class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        bucketsort
        [1,2,2,3,3,3,3]
        """

        count = {}
        bucket = [[] for _ in range(len(nums) + 1)]

        # creating the count hashmap
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # populating the bucket
        for num, c in count.items():
            bucket[c].append(num)

        ans = []
        # now getting the final answer
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        
        return ans
        

