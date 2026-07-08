class Solution {
    public int[] getConcatenation(int[] nums) {
        int len = nums.length;
        int[] res = new int[len * 2];
        for (int i = 0; i < len; i++) {
            res[i] = nums[i];
        }
        for (int i = 0; i < len; i++) {
            res[len + i] = nums[i];
        }
        return res;
    }
}