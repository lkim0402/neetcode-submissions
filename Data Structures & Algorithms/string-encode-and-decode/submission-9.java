class Solution {

    /*
        hello -> 5#hello
    */
    public String encode(List<String> strs) {
        String res = "";
        for (String s : strs) {
            int len = s.length();
            res += len + "#" + s;
        }
        System.out.print(res);
        return res;
    }

    public List<String> decode(String str) {
        int i = 0;
        List<String> res = new ArrayList<>();

        while (i < str.length()) {
            // get the number (n digits)
            int j = i;
            while (str.charAt(j) != '#') {
                j++;
            }
            int length = Integer.parseInt(str.substring(i, j));
            i = j + 1;
            j = i + length;
            res.add(str.substring(i,j));
            i = j;
            //  01234
            //  3#two4#food
            //    i  j
        }
        return res;
    }
}
