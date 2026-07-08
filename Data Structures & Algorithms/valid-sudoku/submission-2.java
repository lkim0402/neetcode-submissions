class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<String, Set<Character>> squares = new HashMap<>();

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char cur = board[r][c];
                if (cur == '.') continue;

                String key = r/3 + "," + c/3;
                if (rows.computeIfAbsent(r, k -> new HashSet<>()).contains(cur) ||
                    cols.computeIfAbsent(c, k -> new HashSet<>()).contains(cur) ||
                    squares.computeIfAbsent(key, k -> new HashSet<>()).contains(cur)
                ) {
                    return false;
                }

                rows.get(r).add(cur);
                cols.get(c).add(cur);
                squares.get(key).add(cur);
            }
        }
        return true;
    }
}
