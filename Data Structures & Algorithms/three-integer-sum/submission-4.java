class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        /*
        nums = [-1,0,1,2,-1,-4,-4]
        nums = [-4,-4,-1,-1,0,1,2]

        - on index 1 we already know that we looked at all combinations for -4
          - checking n - 1
        */

        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
          int main = i;
          if (i > 0 && nums[i] == nums[i - 1]) continue;

          int l = main + 1;
          int r = nums.length - 1;
          while (l < r) {
            int sum = nums[main] + nums[l] + nums[r];
            if (sum > 0) {
              r--;
            } else if (sum < 0) {
              l++;
            } else {
              res.add(List.of(nums[main], nums[l], nums[r]));
              
              // these nums are used up alr, so we move the pointers
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
