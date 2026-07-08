class Solution {
    public int findDuplicate(int[] nums) {
        Set<Integer> values = new HashSet<>();
        int duplicate = 0;
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (values.contains(num)) {
                // return the value
                duplicate = num;
            } else {
                values.add(num);
            }
        }
        return duplicate;
    }
}
