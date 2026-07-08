class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] A = nums1;
        int[] B = nums2;
        int total = A.length + B.length;
        // int half = total / 2;
        int half = (total + 1) / 2; // we + 1 to make sure the median is always on the left partition

        // make A the shorter one
        if (B.length < A.length) {
            int[] tmp = A;
            A = B;
            B = tmp;
        }

        int l = 0;
        int r = A.length;
        while (l <= r) {
            int i = (l + r) / 2; // start of ARight
            int j = half - i; // start of BRight

            int Aleft = i > 0 ? A[i - 1] : Integer.MIN_VALUE;
            int Aright = i < A.length ? A[i] : Integer.MAX_VALUE;
            int Bleft = j > 0 ? B[j - 1] : Integer.MIN_VALUE;
            int Bright = j < B.length ? B[j] : Integer.MAX_VALUE;

            if (Aleft <= Bright && Bleft <= Aright) {
                if (total % 2 != 0) { // total is odd, return the max of the lefts
                    return Math.max(Aleft, Bleft);
                } else { // total is even, we get the middle (max of lefts + min of rights) / 2
                    return (Math.max(Aleft, Bleft) + Math.min(Aright, Bright)) / 2.0;
                }
            } else if (Aleft > Bright) {
                r = i - 1;
            } else {
                l = i + 1;
            }
        }
        return -1;
    }
}
