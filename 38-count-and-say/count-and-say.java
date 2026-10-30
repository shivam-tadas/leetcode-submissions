class Solution {
    public String countAndSay(int n) {
        if (n == 1) return "1";
        
        int i = 1;
        String ans = "", tmp = RLE("1");
        for (i = 1; i < n; ++i) {
            ans = tmp;
            tmp = RLE(ans);
        }
        return ans;
    }

    private String RLE(String n) {
        String ret = "";
        char curr = n.charAt(0);
        int freq = 0;
        for (int i = 0; i < n.length(); ++i) {
            if (n.charAt(i) != curr) {
                ret = ret + "" + freq + "" + curr;
                curr = n.charAt(i);
                freq = 1;
            } else ++freq;
        }
        ret = ret + "" + freq + "" + curr;
        return ret;
    }
}