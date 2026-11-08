class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int gp = 0, sp = 0, ans = 0;
        while (gp < g.length && sp < s.length) {
            System.out.println(g[gp] + ' ' + s[sp]);
            if (g[gp] <= s[sp]) {
                ++ans;
                ++gp;
                ++sp;
            } else if (g[gp] > s[sp])
                ++sp;
        }
        return ans;
    }
}