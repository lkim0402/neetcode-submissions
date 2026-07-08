class Solution {
    public int[] productExceptSelf(int[] nums) {

        /**

        nums =   [1,2,4,6]
        prefix = [1,1,2,8]
        suffix = [48,24,6,1]
        (prefix[i] * suffix[i])
        output = [48,24,12,8]
        **/
        int n = nums.length;
        int[] prefix = new int[n];
        int[] suffix = new int[n];
        int[] res = new int[nums.length];

        // prefix
        prefix[0] = 1;
        for (int i = 1; i < n; i++) {
            prefix[i] = nums[i - 1] * prefix[i - 1];
        }

        // suffix
        suffix[n - 1] = 1;
        for (int i = nums.length - 2; i >= 0; i--) {
            suffix[i] = nums[i + 1] * suffix[i + 1];
        }

        for (int i = 0; i < nums.length; i++) {
            res[i] = prefix[i] * suffix[i];
        }
        return res;
    }
}  
