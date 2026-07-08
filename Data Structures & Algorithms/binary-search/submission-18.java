class Solution {
    public int search(int[] nums, int target) {
        return binarySearch(0, nums.length-1, nums, target);
    }

    /* 
    [-1,0,2,4,6,8], target = 4
      0 1 2 3 4 5 
     
    binarySearch(0, 5)
      mid = 2, num = 2 -> 2 < 4
      binarySearch(3, 5)
        mid = 4, num = 6 -> 6 > 4
        binarySearch(3,3)
        mid = 3, num = 4 -> return 4
      
    */
    public int binarySearch(int l, int r, int[] nums, int target) {
        if (l > r) return -1;
        int mid = (l + r) / 2;
        if (nums[mid] == target) return mid;

        if (nums[mid] < target) {
            return binarySearch(mid + 1, r, nums, target);
        } else {
            return binarySearch(l, mid - 1, nums, target);
        }
    }
}
