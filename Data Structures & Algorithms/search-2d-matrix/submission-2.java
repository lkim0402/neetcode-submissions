class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        /*
            target = 12

            1. binary search on all rows using the 1st num
            2. binary search on the specific row
        */

        int l = 0;
        int r = matrix.length - 1;
        int m = matrix.length - 1; // row
        int n = matrix[0].length - 1; // col
        int foundRow = 0;

        while(l <= r) {
            int mid = (l + r) / 2;
            // if (matrix[mid][0] < target && matrix[mid][n] < target) {
            if (matrix[mid][n] < target) {
                l = mid + 1;
            // } else if (matrix[mid][0] > target && matrix[mid][n] > target) {
            } else if (matrix[mid][0] > target) {
                r = mid - 1;
            } else {
                foundRow = mid;
                break;
            }
        }

        int[] row = matrix[foundRow];
        l = 0; 
        r = row.length - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (row[mid] < target) {
                l = mid + 1;
            } else if (row[mid] > target) {
                r = mid - 1;
            } else {
                return true;
            }
        }
        return false;
                    
    }
}
