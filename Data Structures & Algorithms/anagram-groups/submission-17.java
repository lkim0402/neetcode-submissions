class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        /*
            abc
            - [1,1,1,0,....(26)] -> to string:"1110....0"
            - string used as key in hashmap
        */

        Map<String, List<String>> res = new HashMap<>();
        for (String s : strs) {
            int[] count = new int[26];
            for (char c : s.toCharArray()) {
                count[c - 'a']++;
            }
            String key = Arrays.toString(count);
            res.putIfAbsent(key, new ArrayList<>());
            res.get(key).add(s);
        }
        return new ArrayList<>(res.values());
    }
}
