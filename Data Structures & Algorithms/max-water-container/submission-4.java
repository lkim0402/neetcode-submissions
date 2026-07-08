class Solution {
    public int maxArea(int[] heights) {
        /*
            Moving the taller (doesnt help)
              - if its bigger, the area will still be determined by the min (doesnt matter)
              - if its smaller, the area will be smaller
            Moving the shorter 
              - if its bigger, the area will be bigger
              - if its smaller, the area will be smaller
            Then the only option that can maximize the area is moving the shorter
        */
        int l = 0; 
        int r = heights.length - 1;
        int maxArea = 0;

        while (l < r) {
            int width = r - l;
            int area = width * Math.min(heights[l], heights[r]);
            maxArea = Math.max(area, maxArea);
            if (heights[l] < heights[r]) {
                l++;
            } else {
                r--;
            }
        }

        return maxArea;
    }
}
