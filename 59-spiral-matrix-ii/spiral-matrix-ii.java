class Solution {
    public int[][] generateMatrix(int n) {
        int ans[][] = new int[n][n], l = 0, r = n-1, t = 0, b = n-1, i = 0, j = 0, counter = 1;
        while (l <= r && t <= b) {
            while (j <= r) ans[i][j++] = counter++;
            --r;
            --j;
            ++i;
            while (i <= b) ans[i++][j] = counter++;
            --b;
            --i;
            --j;
            while (j >= l) ans[i][j--] = counter++;
            ++l;
            ++j;
            --i;
            while (i > t) ans[i--][j] = counter++;
            ++t;
            ++i;
            ++j;
        }
        return ans;
    }
}