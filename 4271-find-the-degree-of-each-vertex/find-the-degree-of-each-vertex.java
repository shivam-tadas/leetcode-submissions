class Solution {
    public int[] findDegrees(int[][] matrix) {
        int n = matrix.length, count, i, j;
        int ans[] = new int[n];
        for (i = 0; i < n; ++i) {
            count = 0;
            for (j = 0; j < n; ++j)
                if (matrix[i][j] == 1) ++count;
            ans[i] = count;
        }
        return ans;
    }
}