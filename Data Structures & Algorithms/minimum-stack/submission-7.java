class MinStack {

    Stack<Integer> stack;
    Stack<Integer> minStack;

    public MinStack() {
        stack =  new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int val) {
       /*
        when you push, peek from stack. if smaller than stack then add to min stack.
       */ 
        stack.push(val);
        
        if (minStack.isEmpty()) {
            minStack.push(val);
        } else {
            int peek = minStack.peek();
            if (val < peek) {
                minStack.push(val);
            } else {
                minStack.push(peek);
            }
        }
    }
    
    public void pop() {
        if (!stack.isEmpty()) {
            stack.pop();
            minStack.pop();
        }
    }
    
    public int top() {
        if (!stack.isEmpty()) return stack.peek();
        return 0;
    }
    
    public int getMin() {
        if (!minStack.isEmpty()) return minStack.peek();
        return 0;
    }
}
