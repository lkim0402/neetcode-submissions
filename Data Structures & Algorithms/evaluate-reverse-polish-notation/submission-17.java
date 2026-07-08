class Solution {
    public int evalRPN(String[] tokens) {
        /*
        Things to remember:
          - each input is a String, so use .equals instead of == (which is for char)
          - order of operation matters since we pop it, the later one is the one to go first
            - b - a, not a - b
          - O(N) - it's O(2N) because max of 2 pops per token but 2 is removed 
        */
        Stack<Integer> stack = new Stack<>();
        for (String t : tokens) {
            if (t.equals("+")) {
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b + a);
            } else if (t.equals("-")) {
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b - a);
            } else if (t.equals("*")) {
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b * a);
            } else if (t.equals("/")) {
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b / a);
            } else {
                stack.push(Integer.parseInt(t));
            }
        }
        return stack.pop();
    }
}
