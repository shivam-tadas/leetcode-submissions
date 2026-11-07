class Solution {
    public int[] findDegrees(int[][] matrix) {
        int n = matrix.length, count, i, j;
        int ans[] = new int[n];
        for (i = 0; i < n; ++i)
            ans[i] = Arrays.stream(matrix[i]).sum();
        
        return ans;
    }
}