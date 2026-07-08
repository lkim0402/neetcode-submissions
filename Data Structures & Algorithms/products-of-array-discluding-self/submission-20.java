class Solution {
    public int[] productExceptSelf(int[] nums) {
        /*
        num =    [1, 2, 4, 6]
        prefix = [1, 1, 2, 8] -> before index
        suffix = [48,24,6, 1] -> after index
        output = [48,24,12,8]
        */
        int len = nums.length;
        int[] result = new int[len];

        result[0] = 1;
        for (int i = 1; i < len; i++) {
            result[i] = result[i - 1] * nums[i - 1];
        }
        
        int postfix = 1;
        for (int i = len - 1; i >= 0; i--) {
            result[i] *= postfix;
            postfix *= nums[i];
        }
        return result;

    }
}  
