
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        Map<Character, Character> pair = new HashMap<>();
        pair.put('(',')');
        pair.put('{','}');
        pair.put('[',']');

        for (Character c : s.toCharArray()) {
            if (pair.containsKey(c)) {
                stack.push(c);
            } else {
                if (stack.isEmpty()) return false;
                Character left = stack.pop();
                if (c != pair.get(left)) return false;
            }
        }
        return stack.isEmpty();
    }
}
