class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<>();
        int maxLen = 0;
        int A = 0;
        for (int B = 0; B < s.length(); B++) {
            while (set.contains(s.charAt(B))) {
                set.remove(s.charAt(A));
                A++;
            }
            set.add(s.charAt(B));
            maxLen = Math.max(maxLen, B - A + 1);
        }
        return maxLen;
    }
}
