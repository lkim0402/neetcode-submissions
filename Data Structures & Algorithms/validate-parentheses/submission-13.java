
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        char[] charArray = s.toCharArray();

        java.util.Map<Character, Character> myMap = new java.util.HashMap<>();
        myMap.put('}', '{');
        myMap.put(']', '[');
        myMap.put(')', '(');

        for (char c : charArray) {
            if (myMap.containsKey(c) && !stack.empty()) { // }, ] , )
                if (stack.peek() == myMap.get(c)) {
                    stack.pop();
                } else {
                    return false;
                }
                
            } else { // {, [, (
                stack.push(c);
            }
        }

        return stack.empty();
    }
}
