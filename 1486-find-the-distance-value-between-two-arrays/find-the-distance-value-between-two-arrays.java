class Solution {
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        int dVal = 0, i, j;
        boolean flag;
        for (i = 0; i < arr1.length; ++i) {
            flag = false;
            for (j = 0; !flag && j < arr2.length; ++j)
                if (Math.abs(arr1[i] - arr2[j]) <= d)
                    flag = true;

            if (!flag) ++dVal;
        }
        return dVal;
    }
}