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
        # {1: 1, 2: 2, 3: 4}

        print(count)

        # populating the bucket
        for num, c in count.items():
            bucket[c].append(num)
            print(bucket)

        print(bucket)

        ans = []
        # now getting the final answer
        for i in range(len(bucket) - 1, -1, -1):
            curr_list = bucket[i]
            if len(curr_list) > 0:
                while(len(curr_list) > 0 and k > 0):
                    ans.append(curr_list.pop())
                    k -= 1
        
        return ans
        

