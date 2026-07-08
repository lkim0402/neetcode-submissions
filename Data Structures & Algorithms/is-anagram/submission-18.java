class Solution {
    public boolean isAnagram(String s, String t) {
        /*
         racecar = {r:2, a:2, c:2, e:1}
         carrace = {r:2, a:2, c:2, e:1}
        */

        Map<Character, Integer> firstMap = new HashMap<>();
        Map<Character, Integer> secondMap = new HashMap<>();

        for (Character c: s.toCharArray()) {
            firstMap.put(c, firstMap.getOrDefault(c, 0) + 1);
        }

        for (Character c: t.toCharArray()) {
            secondMap.put(c, secondMap.getOrDefault(c, 0) + 1);
        }

        return firstMap.equals(secondMap);
    }
}
