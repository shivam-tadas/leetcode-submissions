class Solution {
    public String countAndSay(int n) {
        if (n == 1) return "1";
        
        int i = 1;
        String ans = "", tmp = "11";
        for (i = 1; i < n; ++i) {
            ans = tmp;
            tmp = RLE(ans);
        }
        return ans;
    }

    private String RLE(String n) {
        StringBuilder ret = new StringBuilder("");
        char curr = n.charAt(0);
        int freq = 1;
        for (int i = 1; i < n.length(); ++i) {
            if (n.charAt(i) != curr) {
                ret.append(freq).append(curr);
                curr = n.charAt(i);
                freq = 1;
            } else ++freq;
        }
        ret.append(freq).append(curr);
        return ret.toString();
    }
}