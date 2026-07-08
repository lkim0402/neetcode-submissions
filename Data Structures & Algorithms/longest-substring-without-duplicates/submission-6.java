class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<>();
        int maxLen = 0;
        int A = 0;
        int B = 0;
        while (B < s.length()) {
            if (!set.contains(s.charAt(B))) {
                set.add(s.charAt(B));
                maxLen = Math.max(maxLen, B - A + 1);
                B++;
            }
            else {
                set.remove(s.charAt(A));
                A++;
            }
        }
        return maxLen;
    }
}
