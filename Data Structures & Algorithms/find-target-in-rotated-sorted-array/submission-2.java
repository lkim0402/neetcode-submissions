class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;

        // find pivot index
        // designed to converge at single index (l = r = mid = pivot)
        while (l < r) {
            int mid = (l + r) / 2;
            if (nums[mid] > nums[r]) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        int pivotIndex = l;
        l = 0;
        r = nums.length - 1;

        // If target is the pivot or larger AND smaller than the very last element
        // It MUST be in the right half (from pivot to end)
        if (target >= nums[pivotIndex] && target <= nums[r]) {
            l = pivotIndex;
        } else {
            r = pivotIndex - 1;
        }

        while (l <= r) {
            int mid = (l + r) / 2;
            if (nums[mid] < target) {
                l = mid + 1;
            } else if (nums[mid] > target) {
                r = mid - 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
}
