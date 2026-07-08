class Solution {
    public int[] twoSum(int[] nums, int target) {
        /*
        nums = [3,4,5,5], target = 7
        {3:0, 4:1, 5:[2,3]}
        */
        // Map<Integer, Integer> numMap = new HashMap<>();
        // for (int i = 0; i < nums.length; i++) {
        //     numMap.put(nums[i], i);
        // }
        // for (int i = 0; i < nums.length; i++) {
        //     int diff = target - nums[i];
        //     if (numMap.containsKey(diff) && numMap.get(diff) != i) {
        //         return new int[] {i, numMap.get(diff)};
        //     }
        // }
        // return new int[0];

        // [1,3,3] , target = 6

        Map<Integer, Integer> numMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (numMap.containsKey(diff)) {
                return new int[] {numMap.get(diff), i};
            }
            numMap.put(nums[i], i);
        }
        return new int[0];
    }
}
