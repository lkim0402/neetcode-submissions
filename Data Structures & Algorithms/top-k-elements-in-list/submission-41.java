class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // array of lists
        /*
            nums = [1,1,3,3,3,4,4]
            countMap = {1:2, 3:3} # num : count
            bucket = [[],[1,4],[],[3],[],[],[],[]] # index: count, value: nums
        */
        List<Integer>[] bucket = new List[nums.length + 1];
        Map<Integer, Integer> countMap = new HashMap<>();
        
        // initializing bucket
        for (int i = 0; i < nums.length + 1; i++) {
            bucket[i] = new ArrayList<>();
        }
        // initializing countMap
        for (int i = 0; i < nums.length; i++) {
            countMap.put(nums[i], countMap.getOrDefault(nums[i], 0) + 1);
        }
        // use countMap to add to bucket
        for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
            Integer num = entry.getKey();
            Integer count = entry.getValue();
            bucket[count].add(num);
        }

        // iterate bucket reverse
        int[] res = new int[k];
        int index = 0;
        for (int i = bucket.length - 1; i > 0; i--) {
            List<Integer> counts = bucket[i];
            for (int n : counts) {
                res[index++] = n;
                if (index == k) {
                    return res;
                }
            }
        }
        return res;
    }
}
