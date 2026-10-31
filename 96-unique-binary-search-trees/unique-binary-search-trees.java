class Solution {
    public int numTrees(int n) {
        Map<Integer, Integer> nt = new HashMap<>();
        nt.put(0, 1);
        nt.put(1, 1);
        nt.put(2, 2);
        if (n < 3) return nt.get(n);

        int ans = 0, i, k;
        for (i = 3; i < n+1; ++i) {
            ans = 0;
            for (k = 1; k < i+1; ++k)
                ans += nt.get(k-1) * nt.get(i-k);
            nt.put(i, ans);
        }
        return ans;
    }
}