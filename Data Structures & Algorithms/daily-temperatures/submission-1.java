class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int totalLength = temperatures.length;
        int[] res = new int[totalLength];
        Stack<int[]> stack = new Stack<>(); // [temp, index]

        for (int i = 0; i < totalLength; i++) {
            int t = temperatures[i];
            while (!stack.isEmpty() && t > stack.peek()[0]) {
                int[] pair = stack.pop();
                res[pair[1]] = i - pair[1];
            }
            stack.push(new int[]{t, i});
        }

        return res;
        
    }
}
