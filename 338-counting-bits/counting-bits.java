class Solution {
    public int[] countBits(int n) {
        int[] ans = new int[n+1];
        ans[0] = 0;
        if (n > 0) {
            ans[1] = 1;
            for (int i = 2; i < n+1; ++i)
                ans[i] = ans[i>>1] + i%2;
        }
        return ans;
    }
}