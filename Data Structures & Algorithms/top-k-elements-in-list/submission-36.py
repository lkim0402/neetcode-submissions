class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        """
        bloat solution lmao
        """
        # dict_num = {}
        # for num in nums:
        #     dict_num[num] = 1 + dict_num.get(num, 0)
        
        # list = []
        
        # while(k>0):
        #     max_num = 0
        #     # getting for current max value 
        #     for key in dict_num:
        #         if dict_num[key] > max_num:
        #             max_num = dict_num[key]
            
        #     # iterating through dict_num if value is max_value
        #     for key in dict_num:
        #         if dict_num[key] == max_num:
        #             list.append(key)
        #             dict_num[key] = -float('inf') #"marking" as completed
        #             k -= 1

        # return list

        """
        new solution
        """
        """
        [1,2,2,3,3,3]
         0 1 2 3 4 5 6
        """
        res = []

        # counting the occurences of each value
        count = {} 
        res = []
        freq = [[] for i in range(len(nums) + 1)]
    
        # [1:[], 2:[].....]

        #getting count first
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, count in count.items(): #key, value pair in count
            freq[count].append(num)
            #ex: {1: [2,5]} -> 2 and 5 appeared once
            #    {1: [2,5], 2:[3], 3:[4]}
 
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res       

            