class Solution {
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        int dVal = 0, i, l, r, mid, curr, upper, lower, m;
        Arrays.sort(arr2);
        for (i = 0; i < arr1.length; ++i) {
            curr = arr1[i];
            upper = curr + d;
            lower = curr - d;
            l = 0;
            mid = 0;
            r = arr2.length-1;
            while (l < r) {
                mid = (l+r) / 2;
                m = arr2[mid];
                if (m > upper)
                    r = mid;
                else if (m < lower)
                    l = mid+1;
                else if (m <= upper && m >= lower)
                    break;
            }
            if (l == r) mid = (l+r) / 2;
            System.out.println();
            if (arr2[mid] > upper || arr2[mid] < lower)
                ++dVal;
        }
        return dVal;
    }
}