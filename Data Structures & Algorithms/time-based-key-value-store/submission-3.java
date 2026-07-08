class TimeMap {
    /*
        { "alice" : [("happy", 1), ("sad", 3)]
        - map computeIfAbsent
        - Pair class in Java
    */
    private Map<String, List<Pair<String, Integer>>> map;

    public TimeMap() {
        map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        Pair<String, Integer> pair = new Pair<>(value, timestamp);
        map.computeIfAbsent(key, k -> new ArrayList<>()).add(pair);
    }
    
    public String get(String key, int timestamp) {
        if (!map.containsKey(key)) return "";
        List<Pair<String, Integer>> list = map.get(key);

        // binary search on the list
        int l = 0;
        int r = list.size() - 1;
        String closest = "";
        while (l <= r) {
            int mid = (l + r) / 2;
            Pair<String, Integer> p = list.get(mid);
            Integer t = p.getValue();
            if (t < timestamp) {
                l = mid + 1;
                closest = p.getKey(); // the key is updating this only here
            } else if (t > timestamp) {
                r = mid - 1;
            } else {
                return p.getKey();
            }
        }
        return closest;
    }
}
