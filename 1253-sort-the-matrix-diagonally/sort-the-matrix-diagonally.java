class Solution {
    int ans[][], currMat[][];
    public int[][] diagonalSort(int[][] mat) {
        int m = mat.length, n = mat[0].length, i, step;
        ans = new int[m][n];
        currMat = mat;

        // Perform sort considering every diagonal
        for (i=1; i<m; ++i) {
            // column 0 elements except the first one
            step = Math.min(m-i, n);
            diagSortHelper(i, 0, step);
        }

        for (i=0; i<n; ++i) {
            // row 0 elements
            step = Math.min(m, n-i);
            diagSortHelper(0, i, step);
        }

        return ans;
    }

    private void diagSortHelper(int baseRow, int baseCol, int step) {
        System.out.println(step);
        List<Integer> currDiag = new ArrayList<>();
        for (int i=0; i<step; ++i) {
            System.out.println((baseRow+i) + " " + (baseCol+i));
            currDiag.add(currMat[baseRow+i][baseCol+i]);
        }
        
        Collections.sort(currDiag);

        for (int i=0; i<step; ++i)
            ans[baseRow+i][baseCol+i] = currDiag.get(i);
    }
}