class Solution {
    public int maxProfit(int[] prices) {
        int minVal = Integer.MAX_VALUE;
        int res = 0;
        for (int price : prices) {
            if (price < minVal) {
                minVal = price;
            } else if (price > minVal) {
                res = Math.max(price - minVal, res);
            }
        }
        return res;
    }
}
