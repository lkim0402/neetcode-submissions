class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict_num = {}
        for num in nums:
            dict_num[num] = 1 + dict_num.get(num, 0)
        
        list = []
        
        while(k>0):
            max_num = 0
            # getting for current max value 
            for key in dict_num:
                if dict_num[key] > max_num:
                    max_num = dict_num[key]
            
            # iterating through dict_num if value is max_value
            for key in dict_num:
                if dict_num[key] == max_num:
                    list.append(key)
                    dict_num[key] = 0
                    k -= 1

        """
        [1,2,2,3,3,3]

        1:1, 2:2, 3:3
        [3]
        max_num = 3
        k=2

        1:1, 2:0, 3:0
        max_num = 2
        [3,2]
        k=1
        """

        return list
            