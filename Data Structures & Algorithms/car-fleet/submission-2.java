class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int[][] pair = new int[position.length][2];
        for (int i = 0; i < position.length; i++) {
            pair[i][0] = position[i];
            pair[i][1] = speed[i];
        }

        Arrays.sort(pair, (a,b) -> Integer.compare(b[0], a[0]));
        Stack<Double> stack = new Stack<>();

        // time = distance / speed
        for (int[] p : pair) {
            double time = (double) (target - p[0]) / p[1];
            stack.push(time);
            if (stack.size() >= 2 && stack.peek() <= stack.get(stack.size() - 2)) {
                stack.pop();
            }
        }
        return stack.size();
    }

    /*
    time complexity:
    - O(N): Building the pair array takes linear time.
    - O(N log N): Sorting the pair array. This is the dominant operation in your algorithm.
    - O(N): The final loop iterates through the N cars. 
      - All stack operations inside the loop (push, pop, peek, get, size) are O(1) on average.
    Therefore, the sorting step (O(N log N)) determines the overall time complexity.    
    */
}
