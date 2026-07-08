class Solution {
    public boolean checkInclusion(String s1, String s2) {
    
        if (s1.length() > s2.length()) return false;

        int[] s1String = new int[26];
        int[] s2String = new int[26];

        for (int i = 0; i < s1.length(); i++) {
            s1String[s1.charAt(i) - 'a']++;
            s2String[s2.charAt(i) - 'a']++;
        }
        
        int matches = 0;
        for (int i = 0; i < 26; i++) {
            if (s1String[i] == s2String[i]) matches++;
        }

        for (int l = 0, r = s1.length(); r < s2.length(); l++, r++) {
            if (matches == 26) return true; // early return
            
            // adding the new value
            int index = s2.charAt(r) - 'a';
            s2String[index]++;
            // if match
            if (s1String[index] == s2String[index]) {
                matches++;
            } else if (s1String[index] + 1 == s2String[index]) { // broke a match
                matches--;
            }

            // removing the old value
            index = s2.charAt(l) - 'a';
            s2String[index]--;
            if (s1String[index] == s2String[index]) {
                matches++;
            } else if (s1String[index] - 1 == s2String[index]) { // broke a match
                matches--;
            }
        }
        return matches == 26;
    }
}
