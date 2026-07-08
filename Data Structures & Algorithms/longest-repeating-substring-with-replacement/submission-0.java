class Solution {
    public int characterReplacement(String s, int k) {
        int maxLen = 0;
        int maxFreq = 0;
        int[] charCount = new int[26];
        int L = 0;
        for (int R = 0; R < s.length(); R++) {
            int i = s.charAt(R) - 'A';
            charCount[i]++;
            // update max requency
            maxFreq = Math.max(maxFreq, charCount[i]);

            if ((R - L + 1 - maxFreq > k)) {
                charCount[s.charAt(L) - 'A']--;
                L++;   
            } 
            maxLen = Math.max(maxLen, R - L + 1);
        }
        return maxLen;
    }
}
