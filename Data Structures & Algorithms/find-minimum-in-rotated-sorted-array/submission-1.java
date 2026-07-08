class Solution {
    public int findMin(int[] nums) {
        int min = nums[0];
        int l = 0;
        int r = nums.length - 1;

        while (l <= r) {
            // in a sorted section
            if (nums[l] < nums[r]) {
                min = Math.min(min, nums[l]);
                break;
            }

            int mid = (l + r) / 2;
            min = Math.min(min, nums[mid]);
            if (nums[mid] >= nums[l]) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return min;
    }
}
