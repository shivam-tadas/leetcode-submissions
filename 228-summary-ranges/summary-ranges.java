class Solution {
    public List<String> summaryRanges(int[] nums) {
        if (nums == null || nums.length == 0)
            return new ArrayList<>();

        List<String> ans = new ArrayList<>();
        int n = nums.length, i = 0, start = nums[0], end = nums[0];
        for (; i < n; ++i) {
            if (nums[i] == end + 1)
                end = nums[i];
            else if (start != end) {
                ans.add(start + "->" + end);
                start = nums[i];
                end = nums[i];
            }
            else if (i != 0) {
                ans.add(Integer.toString(start));
                start = nums[i];
                end = nums[i];
            }
        }
        if (start != end)
            ans.add(start + "->" + end);

        else
            ans.add(Integer.toString(start));

        return ans;
    }
}