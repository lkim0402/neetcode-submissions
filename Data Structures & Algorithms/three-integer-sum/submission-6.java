class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        /*
        nums = [-1,0,1,2,-1,-4,-4]
        nums = [-4,-4,-1,-1,0,1,2]

        - on index 1 we already know that we looked at all combinations for -4
          - checking n - 1

        Time: O(n log n) for sorting + O(n^2) for 2 loops -> O(n^2)
        */

        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
          // this means that onwards all nums will be pos
          if (nums[i] > 0) break;
          // skipping 
          if (i > 0 && nums[i] == nums[i - 1]) continue;

          int l = i + 1;
          int r = nums.length - 1;
          while (l < r) {
            int sum = nums[i] + nums[l] + nums[r];
            if (sum > 0) {
              r--;
            } else if (sum < 0) {
              l++;
            } else {
              res.add(List.of(nums[i], nums[l], nums[r]));
              
              // get off the current nums
              l++;
              r--;
              while (l < r && nums[l - 1] == nums[l]) {
                l++;
              }
            }
          }
        }
        return res;
    }
}
