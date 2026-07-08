class Solution {
    public int longestConsecutive(int[] nums) {
        /*
        [2,20,4,10,3,4,5]
        
        2 3 4 5
        10 20

        if there is a sequence that starts with n, then n - 1 doesn't exist

        1. put all the nums in a set
        2. loop over nums
          - check if num - 1 is in set
            - if in set - skip
            - if not in set (sequence) - while loop n + 1
            - set that as the length
        */

        Set<Integer> numSet = new HashSet<>();
        
        for (int num : nums) {
            numSet.add(num);
        }

        int len = 0;
        for (int num : nums) {
            if (!numSet.contains(num - 1)) {
                int check = num;
                int i = 1;
                while (numSet.contains(check + i)) {
                    i++;    
                }
                len = Math.max(i, len);
            }
        }
        return len;
    }
}
