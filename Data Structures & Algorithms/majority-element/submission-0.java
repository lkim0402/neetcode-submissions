class Solution {
    public int majorityElement(int[] nums) {
        /*
        [5,5,1,1,1,5,5]
        map = {5:4, 1:3}
        
        */
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }

        int maxCount = 0;
        int res = 0;
        // map = {5:4, 1:3}
        for (Map.Entry<Integer, Integer> entry: map.entrySet()) {
            Integer key = entry.getKey();
            Integer value = entry.getValue();
            System.out.println("key: "+ key + ", value: " + value);
            if (value > maxCount) {
                maxCount = value;
                res = key;
            }
        }
        return res;
    }
}