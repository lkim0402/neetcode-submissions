class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        /*
        The trick is to use a decreasing monotonic stack

         0  1  2  3  4  5  6  7
        [30,29,38,30,36,35,40,28]

        [(30,0),(29,1),() ]
        
        res = [2,1]
        */

        // Stack<int[]> stack = new Stack<>();
        // int[] res = new int[temperatures.length]; 
        // stack.push(new int[] {temperatures[0], 0}); // number, int

        // for (int i = 0; i < temperatures.length; i++) {
        //     int t = temperatures[i];
        //     while (!stack.isEmpty() && t > stack.peek()[0]) {
        //         int[] pair = stack.pop();
        //         int numIndx = pair[1];
        //         res[numIndx] = i - numIndx;
        //     }
        //     stack.push(new int[] {t, i});
        // }

        // return res;


        int len = temperatures.length;
        Stack<int[]> stack = new Stack<>(); // num, index
        int[] res = new int[len];

        for (int i = 0; i < len; i++) {
            int t = temperatures[i];
            while (!stack.isEmpty() && t > stack.peek()[0]) {
                int[] pair = stack.pop();
                int index = pair[1];
                res[index] = i - index;
            }
            stack.push(new int[] {t, i});
        }

        return res;
    }
}
