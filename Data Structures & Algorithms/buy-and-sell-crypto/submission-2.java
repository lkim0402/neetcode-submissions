class Solution {
    public int maxProfit(int[] prices) {
        int minVal = Integer.MAX_VALUE;
        int minInx = 0;
        int res = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minVal) {
                minVal = prices[i];
                minInx = i;
            }
            if (prices[i] > minVal && i > minInx) {
                res = Math.max(prices[i] - minVal, res);
            }
        }
        return res;
    }
}
