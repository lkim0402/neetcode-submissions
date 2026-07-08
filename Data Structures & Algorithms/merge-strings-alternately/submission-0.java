class Solution {
    public String mergeAlternately(String word1, String word2) {
        String res = "";
        
        int cur = 0;
        int minLength = Math.min(word1.length(), word2.length());
        while (cur < minLength) {
            res += word1.charAt(cur);
            res += word2.charAt(cur);
            cur++;
        }

        if (cur < word1.length()) { // word1 is longer
            res += word1.substring(cur);
        } else if (cur < word2.length()) {
            res += word2.substring(cur);
        }
        return res;
    }
}