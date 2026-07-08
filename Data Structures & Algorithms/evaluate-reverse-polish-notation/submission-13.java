class Solution {
    public int evalRPN(String[] tokens) {
        Stack<String> myStack = new Stack<>();

        for (String c : tokens) {
            if (c.equals("+")) {
                int num1 = Integer.parseInt(myStack.pop());
                int num2 = Integer.parseInt(myStack.pop());
                myStack.push(String.valueOf(num2 + num1));
            } else if (c.equals("-")) {
                int num1 = Integer.parseInt(myStack.pop());
                int num2 = Integer.parseInt(myStack.pop());
                myStack.push(String.valueOf(num2 - num1));
            } else if (c.equals("/")) {
                int num1 = Integer.parseInt(myStack.pop());
                int num2 = Integer.parseInt(myStack.pop());
                myStack.push(String.valueOf(num2 / num1));
            } else if (c.equals("*")) {
                int num1 = Integer.parseInt(myStack.pop());
                int num2 = Integer.parseInt(myStack.pop());
                myStack.push(String.valueOf(num2 * num1));
            } else { // number
                myStack.push(c);
            }
        }
        return Integer.parseInt(myStack.pop());
    }
}
