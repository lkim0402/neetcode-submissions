class Solution {
    public int[] productExceptSelf(int[] nums) {
        /*
        num = [1,2,4,6]
        prefix = [1,1,2,8] -> before index
        suffix = [48,24,6,1] -> after index
        */
        int len = nums.length;
        int[] prefix = new int[len];
        int[] suffix = new int[len];
        int[] result = new int[len];

        prefix[0] = 1;
        for (int i = 1; i < len; i++) {
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }

        suffix[len - 1] = 1;
        for (int i = len - 2; i >= 0; i--) {
            suffix[i] = suffix[i + 1] * nums[i + 1];
        }

        for (int i = 0; i < len; i++) {
            result[i] = prefix[i] * suffix[i];
        }
        return result;

    }
}  
