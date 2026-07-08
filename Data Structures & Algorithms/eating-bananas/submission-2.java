class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 0; 
        int r = Arrays.stream(piles).max().getAsInt();
        int min = r;

        while (l <= r) {
            int k = (l + r) / 2;

            int totalTime = 0;
            for (int p : piles) {
                totalTime += Math.ceil((double) p / k);
            }
            if (totalTime <= h) {
                min = Math.min(min, k);
                r = k - 1;
            } else {
                l = k + 1;
            }
        }
        return min;

    }
}
