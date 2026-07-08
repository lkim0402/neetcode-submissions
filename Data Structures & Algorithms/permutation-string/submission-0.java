class Solution {
    public boolean checkInclusion(String s1, String s2) {
        /*
        - make a hashmap out of s1 (key = char, value = count)
          - "abcc" -> {"a" : 1, "b" : 1, "c" : 2}
        - sliding window
          - size is s1.length()
          - make a hashmap per iteration and compare to s1's map
        */

        Map<Character, Integer> s1Map = new HashMap<>();
        for (Character c : s1.toCharArray()) {
            s1Map.put(c , s1Map.getOrDefault(c, 0) + 1);
        }

        // sliding window
        int r = s1.length() - 1;
        int l = 0;
        while (r < s2.length()) {
            String substring = s2.substring(l,r+1);
            System.out.println(substring);
            Map<Character, Integer> map = new HashMap<>();
            for (Character c : substring.toCharArray()) {
                map.put(c , map.getOrDefault(c, 0) + 1);
            }
            if (map.equals(s1Map)) return true;
            l++;
            r++;
        }
        return false;        
    }
}
