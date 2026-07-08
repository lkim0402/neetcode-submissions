class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;

        while (left < right) {
            int leftNum = numbers[left];
            int rightNum = numbers[right];
            System.out.println("leftnum: " + leftNum);
            System.out.println("rightnum: " + rightNum);

            if (target > (leftNum + rightNum)) {
                left++;
            } else if (target < (leftNum + rightNum)) {
                right--;
            } else {
                return new int[] {left + 1, right + 1};
            }
        }

        return new int[] {};
    }
}
