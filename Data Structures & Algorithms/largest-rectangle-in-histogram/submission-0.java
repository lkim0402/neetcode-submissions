class Solution {
    public int largestRectangleArea(int[] heights) {
         int maxArea = 0;
         Stack<int[]> stack = new Stack<>(); // index, height

         for (int i = 0; i < heights.length; i++) {
            int start = i;
            while (!stack.isEmpty() && stack.peek()[1] > heights[i]) { 
                // prev > cur -> taller ends here, but shorter extends left to taller's index
                int[] top = stack.pop();
                int index = top[0];
                int height = top[1];
                maxArea = Math.max(maxArea, height * (i - index));
                // move the "shorter" wall's index to the back because 
                // it could have extended until there
                start = index;
            }
            stack.push(new int[]{start, heights[i]});
         }

        // bars that extended all the way to the end of the array without 
        // finding a shorter bar to stop them
         for (int[] pair : stack) {
            int index = pair[0];
            int height = pair[1];
            maxArea = Math.max(maxArea, height * (heights.length - index));
         }
         return maxArea;
    }
}
