class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        ArrayList<Integer> ans = new ArrayList<>();
        int ptr1 = 0, ptr2 = 0;
        while (ptr1 < m && ptr2 < n) {
            if (nums1[ptr1] == nums2[ptr2]) {
                ans.add(nums1[ptr1++]);
                ans.add(nums2[ptr2++]);
            }
            else if (nums1[ptr1] < nums2[ptr2])
                ans.add(nums1[ptr1++]);
            else
                ans.add(nums2[ptr2++]);
        }
        while (ptr1 < m)
            ans.add(nums1[ptr1++]);
        while (ptr2 < n)
            ans.add(nums2[ptr2++]);
        for (int i = 0; i < m+n; i++)
            nums1[i] = ans.get(i);
    }
}