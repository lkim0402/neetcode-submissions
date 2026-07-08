class Solution {
    public int majorityElement(int[] nums) {
        /*
        [5,5,1,1,1,5,5]
        map = {5:4, 1:3}
        
        */
        Map<Integer, Integer> map = new HashMap<>();
        int maxCount = 0;
        int res = 0;
        for (int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
            if (map.get(n) > maxCount) {
                maxCount = map.get(n);
                res = n;
            }
        }
        return res;
    }
}